from pytube import YouTube

def main():
    videoURL = input('Cole aqui o link do vídeo desejado: ')
    videoFormat = int(input('Certo, qual formato deseja fazer o download?\n1- MP4 (Formato de vídeo)\n2- WEBM (Formato de vídeo sem áudio)\n-> '))
    
    if (videoFormat > 2):
        print('[Error] Fomato Inválido.')
        return main()

    DowloadVideo(videoURL,videoFormat)


def DowloadVideo(link,format):
    objYoutube = YouTube(link)

    if format == int(1):
        objYoutube = objYoutube.streams.filter(file_extension='mp4')
    else:
        objYoutube = objYoutube.streams.filter(only_audio=True)

    try:
        print('Ok, iniciando Download...')
        objYoutube.first().download()
    except:
        print('[Error] Erro ao fazer download.')
        return main()

    print('[Success] Download concluído!')
    
    return main()

main()