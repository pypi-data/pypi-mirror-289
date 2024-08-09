## BSD 2-Clause License
# 
# Copyright (c) 2023, Coltec do PCO <coltecpco@skiff.com>
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# # # # #

# =======================================================================================
#  Header
# =======================================================================================

import os
import sh
import sys
from pathlib import Path
import ffmpeg
import click
from googletrans import Translator
import cv2
import numpy as np
from subprocess import Popen, PIPE

# import argostranslate.package
# import argostranslate.translate

# checar whisper_cpp e ffmpeg
# Baixar o whisper_cpp, compilar e instalar no .local/bin

# =======================================================================================
#  Functions
# =======================================================================================

def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# =======================================================================================
#  Class Video
# =======================================================================================

class Video:
    def __init__(self):
        self.video_mp4 = ""
        self.audio_wav = ""
        self.audio_txt = ""
        self.video_url = ""
        self.font_size = 14

    def from_web(self, url: str):
        self.video_url = url
        url_path_name = Path(url).name     # url_path_name = "https://www.youtube.com/watch?v=X7MFKVaK6E8"
        url_path_name = url_path_name      # url_path_name = watch?v=X7MFKVaK6E8
        if url_path_name[0:8] == "watch?v=":
            url_path_name = url_path_name.split('=')[1]       # url_path_name = X7MFKVaK6E8
        else:
            url_path_name = url_path_name.split('?')[0]

        log(url_path_name)
        self.video_id = url_path_name
        self.video_dir = f"tmp_yt_{self.video_id}"
        self.video_mp4 = f"{self.video_dir}/video.mp4"
        self.audio_wav = f"{self.video_dir}/audio.wav"
        self.audio_txt = f"{self.video_dir}/audio.txt"
        Path(self.video_dir).mkdir(parents=True, exist_ok=True)


    def from_filesystem(self, video_path: str):
        # Geral
        video_path = Path(video_path)
        if ( not video_path.exists() ):
            raise Exception(f"File {video_path} not exists")

        self.video_mp4 = video_path
        self.video_id = video_path.stem
        self.video_dir = "tmp_"+self.video_id
        self.audio_wav = f"{self.video_dir}/audio.wav"
        self.audio_txt = f"{self.video_dir}/audio.txt"
        Path(self.video_dir).mkdir(parents=True, exist_ok=True)

    def download(self):
        if not Path(self.video_mp4).exists():
            log(f"Baixando o video {self.video_url}")
            sh.yt_dlp("-f", 18, self.video_url, "-o", self.video_mp4)
            # sh.yt_dlp(self.video_url, "-o", self.video_mp4)

    def converte_mp4_para_wav(self):
        audio_wav_path = Path(self.audio_wav)
        if not audio_wav_path.exists():
            log(f"Convertendo o video para wav")
            sh.ffmpeg("-i", self.video_mp4, "-ac", 1, "-ar", 16000, self.audio_wav)

    def transcreve(self, spoke_language):
        self.spoke_language = spoke_language
        text = []

        # Case audio.txt is not exists
        if not Path(self.audio_txt).exists():
            log(f"Transcrevendo o video apartir do wav")
            # with open(self.audio_txt, "w") as fd:
                # sh.whisper_cpp("-m", "/home/user/.whisper/ggml-large.bin", "-l", spoke_language, "-f", self.audio_wav, _err=sys.stderr, _out=fd)

            ggml_path = Path.home() / ".whisper/ggml-large.bin"
            whisper = Popen(["whisper_cpp", "-m", str(ggml_path), "-l", spoke_language, "-f", self.audio_wav], stdout=PIPE, stderr=None)

            fd = open(self.audio_txt, 'w')
            for line in whisper.stdout:
                # decode and check if line is bigger than 2 characters
                line = line.decode('utf-8')
                if len(line) < 2:
                    continue

                # add in the text, file, stdout and flush the stdout
                text.append(line)
                fd.write(line)
                print(line, end='')
                sys.stdout.flush()
            fd.close()

        # le do arquivo gerado pelo whisper e convert para um dicionario
        else:
            # read whole file and split it by each line
            with open(self.audio_txt, "r") as fd:
                text = fd.read().split('\n')

            # print all the lines
            for line in text:
                print(line)

        # retorna vetor de legendas
        self.legendas = Video.__convert_txt_to_dict(text)
        return self.legendas


    def convert_to_srt(self, target_language):
        video_srt = f"{self.video_dir}/video-{target_language}.srt"
        self.video_srt = video_srt

        if self.spoke_language == target_language:
            if not Path(video_srt).exists():
                log(f"Salvando as legendas em {video_srt}")
                self.__save_srt(video_srt, self.legendas)
        
        else:
            if not Path(video_srt).exists():
                log(f"Salvando as legendas em {video_srt}")
                dict_legenda = self.__traduz(target_language)
                self.__save_srt(video_srt, dict_legenda)

    def to_mobile(self, background_path):
        log("Criando o video para mobile")
        self.video_mp4_mobile = f"{self.video_dir}/tmp_mobile.mp4"

        # converte o video horizontal para vertical
        cap = cv2.VideoCapture( str(self.video_mp4) )

        background = None
        if background_path != "":
            background = cv2.imread(background_path)

        out_frame = np.zeros((640, 360, 3), np.uint8)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out_video = cv2.VideoWriter(self.video_mp4_mobile, fourcc, 30, (360,640))
        while True:
            ret, cap_frame = cap.read()
            if ret == True:
                cap_frame_360 = cv2.resize(cap_frame, dsize=(360, 202), interpolation=cv2.INTER_CUBIC)
                if background != None:
                    out_frame = background
                out_frame[219:421, 0:360, 0:3] = cap_frame_360
                out_video.write( out_frame )
                # print(i)
            else:
                break
        out_video.release()
        cap.release()

        # coloca o audio no video mobile
        video = ffmpeg.input(self.video_mp4)
        audio = video.audio
        video2 = ffmpeg.input(self.video_mp4_mobile)

        # atualiza o atributo video
        self.video_mp4 = f"{self.video_dir}/mobile.mp4"
        ffmpeg.concat(video2, audio, v=1, a=1).output(self.video_mp4).run()


    def __traduz(self, linguagem_destino):
        dict_legendas = []
        translator = Translator()
        fd = open( Path(self.video_dir) / f"audio-{linguagem_destino}.srt", "w")
        for line in self.legendas:
            line_text = line['text']
            print(line_text)
            traduzido = translator.translate(line_text, src=self.spoke_language, dest=linguagem_destino)
            dict_legendas.append({'time': line['time'], 'text': traduzido.text})
            
            # text_en = argostranslate.translate.translate(line_text, "ru", "en")
            # text_pt = argostranslate.translate.translate(text_en, "en", "pt")
            # dict_legendas.append({'time': line['time'], 'text': text_pt})
            # fd.write(f"[{line['time']}] {text_pt}")
	    
        fd.close()
        return dict_legendas

    def legenda(self, nome_video_legendado, language):
        if type(language) == str:
            if not Path(f"video-{language}.srt").exists():
                self.convert_to_srt(language)
            self.__legenda(self.video_mp4, nome_video_legendado, language, 2)
        elif type(language) == list:
            # cria os srt de cada linguagem
            for lang in language:
                if not Path(f"video-{lang}.srt").exists():
                    self.convert_to_srt(lang)

            # legenda os videos
            if len(language) == 1:
                self.__legenda(self.video_mp4, nome_video_legendado, language[0], 2)
            elif len(language) == 2:
                self.__legenda(self.video_mp4, f"{self.video_dir}/video_passo_1.mp4", language[0], 2)
                self.__legenda(f"{self.video_dir}/video_passo_1.mp4", nome_video_legendado, language[1], 6)
            elif len(language) == 3:
                self.__legenda(self.video_mp4, f"{self.video_dir}/video_passo_1.mp4", language[0], 2)
                self.__legenda(f"{self.video_dir}/video_passo_1.mp4", f"{self.video_dir}/video_passo_2.mp4", language[1], 4, 7)
                self.__legenda(f"{self.video_dir}/video_passo_2.mp4", nome_video_legendado, language[2], 7, 7)

    def __legenda(self, video_original, nome_video_legendado, language, position):
        log("Legenda o video")
        output_path = Path(nome_video_legendado)
        if output_path.exists():
            os.remove(output_path)

        # audio_file = ffmpeg.input(f"{self.video_dir}/audio.mp4")

        style = f"Alignment={position},Fontsize={self.font_size},Outline=2"
        video = ffmpeg.input(video_original)
        audio = video.audio
        ffmpeg.concat(video.filter("subtitles", f"{self.video_dir}/video-{language}.srt", force_style=style), audio, v=1, a=1).output(nome_video_legendado).run()

    def __save_srt(self, filename, dict_legendas):
        text_srt = ''
        count = 1
        for line in dict_legendas:
            time = line['time']
            text = line['text']
            text_srt += f"{count}\n{time}\n{text}\n\n"
            count += 1

        fd = open(filename, "w")
        fd.write(text_srt)
        fd.close()

    def __convert_txt_to_dict(text_in_lines):
        # convert de "[time] text" to SRT format
        ret_dict = []
        for _line in text_in_lines:
            if len(_line) == 0:
                continue
            
            line = _line.split('] ', 1)
            time = line[0].replace('[','')
            try:
                text = line[1].strip()
            except:
                text = ""

            line = {'time': time, 'text': text}
            ret_dict.append(line)
        return ret_dict

# =======================================================================================
#  Comandos
# =======================================================================================

@click.command()
@click.argument('url', nargs=1)
@click.option('--language', '-l', default='en', help='linguagem falada no video')
@click.option('--to', '-t', default='', help='linguagem da legenda')
@click.option('--mobile',  is_flag=True, help='faz o video na horizontal com um fundo dado como parametro')
@click.option('--background', '-bg', default='', help='fundo para a versao de celulares')
@click.option('--dubbing', '-d', default='', help='linguagem para dublagem')
@click.option('--font', '-f', default='14', help='tamanho da fonte')
def legenda(url, language, to, mobile, background, dubbing, font):
    # verifica se ffmpeg esta instalado no sistema
    ffmpeg_path = sh.whereis("ffmpeg").split(':')[1]
    if len(ffmpeg_path) <= 1:
        print("ffmpeg nao encontrado em /usr/bin ou /usr/local/bin")
        print(" - instale o ffmpeg usando apt-get or yum")
        exit(1)

    # verifica se whisper_cpp esta no sistema
    whiper_cpp_path = sh.whereis("whisper_cpp").split(':')[1]
    if len(whiper_cpp_path) <= 1:
        print("whisper_cpp nao encontrado em /usr/bin ou /usr/local/bin")
        print(" - baixe o repositorio https://github.com/ggerganov/whisper.cpp")
        print(" - compile e renomeie o aplicativo main para whisper_cpp e coloque no /usr/bin do sistema")
        exit(1)

    # verifica se o modelo do whisper esta na pasta ~/.whisper/ggml-large.bin
    ggml_path = Path.home() / ".whisper/ggml-large.bin"
    if not ggml_path.exists():
        print("O modelo ggml-large.bin nao estah presente na pasta ~/.whisper/")
        print(" - baixe o repositorio https://github.com/ggerganov/whisper.cpp")
        print(" - execute o script models/download-ggml-model.sh que baixa o arquivo ggml-large.bin na mesma pasta")
        print(" - entao mova o arquivo ggml-large.bin para o local ~/.whisper")
        exit(1)

    # cria o objeto video, transcreve e legenda
    video = Video()
    video.font_size = int(font)

    if url[0:8] == "https://" or url[0:7] == "http://":
        video.from_web(url)
        video.download()
    else:
        video.from_filesystem(url)

    if mobile == True:
        video.to_mobile(background)

    video.converte_mp4_para_wav()
    video.transcreve(language)

    if to != '':
        to_languages = to.split(',')
        video_output_name = f"{video.video_id}_{'_'.join(to_languages)}.mp4"
        video.legenda(video_output_name, to_languages)

# =======================================================================================
#  Main
# =======================================================================================

if __name__ == '__main__':
    legenda()
    exit(0)
