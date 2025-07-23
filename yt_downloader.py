from yt_dlp import YoutubeDL
import os

opts = {
    'formato' : 'bestaudio',
}

lista = []
url_nome = []

def pega_url(url):
    opcoes = {
        'skip_download' : True,
    }

    with YoutubeDL(opcoes) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get('title')
    
while True:
    print('Selecione uma opção')
    opcao = input('[i]inserir [a]apagar [l]listar [u]update [d]Download: ')

    if opcao.lower() == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao.lower() == 'a':
        indice_str = input('Escolha o indice a apagar: ')
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possivel apagar este indice!')
    
    elif opcao.lower() == 'u':
        os.system('cls')
    
        if len(lista) == 0:
            print('Lista vazia')
        
        for i, valor in enumerate(lista):
            nome_url = pega_url(valor)
            url_nome.append(nome_url)
            print(i,nome_url)
            print(f'URL =', valor)

    elif opcao.lower() == 'l':
        os.system('cls')
    
        if len(url_nome) == 0:
            print('Lista vazia')
        
        for i, valor in enumerate(url_nome):
            print(i,valor)