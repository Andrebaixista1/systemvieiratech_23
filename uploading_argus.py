from time import sleep
from datetime import datetime
import os
from tkinter import Tk, filedialog
import requests


def limp():
    os.system('cls')

def abrir_janela_arquivo(op, qt_base):
    limp()
    print('Selecione um arquivo...')
    # Abre a janela de seleção de arquivo e obtém os nomes dos arquivos selecionados
    file_paths = filedialog.askopenfilenames()
    if qt_base == 2:
        if file_paths is None or len(file_paths) == 0:
            os.system('cls')
            print('Nenhum arquivo foi selecionado')
            sleep(3)
            return
        else:
            limp()
            num_vezes = int(input('Digite a quantidade '))
            c = 1
            while c <= num_vezes:
                # Enviar um arquivo de cada vez para a API
                for file_path in file_paths:
                    enviar_arquivo(file_path, op)

                c += 1
    else:
            if file_paths is None or len(file_paths) == 0:
                limp()
                print('Nenhum arquivo foi selecionado')
                sleep(3)
                return
            else:
                for file_path in file_paths:
                    enviar_arquivo(file_path, op)
    
    limp()
    return
    
def enviar_arquivo(file_path, n):
    
    empresa = {'1': 'vieiracred_sl1', '2': 'vieiracred_sl3', '3': 'prado_api',
               '4': 'gbr_api', '5': 'kr_api', '6': 'tk_api', '7': '3p_api', '8': 'vision_api','9':'2a_api', 
               15: 'vieira_teste'}
    
    token = { 15: 'oLbJS3hu6s2tquHTFAFMUwwEL9KKTXw28d3QzJ4AX4AYDxUN6uHP30gIEAAsECMM',  #Vieira 23243
             '1': 'oLbJS3hu6s2tquHTFAFMUwwEL9KKTXw28d3QzJ4AX4AYDxUN6uHP30gIEAAsECMM',   #Vieira 23243
             '2': 'oLbJS3hu6s2tquHTFAFMUwwEL9KKTXw28d3QzJ4AX4AYDxUN6uHP30gIEAAsECMM',   #Vieira 23243
             '3':'c6a1d7d5b09814ef65bfd9b0c0c66ad6198898d432e1c26eb245743041374636',   #Prado 23241
             '4':'d7a91c4f25907ab3ed1661f600bae6ee545d87dd78a121dbdf43a3074ea2db45',   #GBR 23232
             '5':'c6a1d7d5b09814ef65bfd9b0c0c66ad6198898d432e1c26eb245743041374636',   #KR 23241
             '6':'459ad52bc2851fcf283dc7da847408236ebcf0a54b4bf9826821e2add7a15f2c',   #TK 23248
             '7':'ac6d5a6fabe7f0458a7a0aafa12f68b3f3f8c725cf52ea3703a5abe6c3bbcdf8',   #3P 23451
             '8':'cffff8c98d8518a51ea24490434b01ba4b9fc5c1f131df47ef3aa004d7a43385',   #Vision 23316
             '9':'9eee6954b11ae11798c3839236a1444111c2b63d0296a229a4dc4a3a875d08df'}   #2A 23435
    
    api_link = { 15: 'http://apioci.argus.app.br:23243/apiargus/',  #Vieira 23243
                '1': 'http://apioci.argus.app.br:23243/apiargus/',   #Vieira 23243
                '2': 'http://apioci.argus.app.br:23243/apiargus/',   #Vieira 23243
                '3': 'http://apioci.argus.app.br:23241/apiargus/',   #Prado 23241
                '4': 'http://apioci.argus.app.br:23232/apiargus/',   #GBR 23232
                '5': 'http://apioci.argus.app.br:23241/apiargus/',   #KR 23241
                '6': 'http://apioci.argus.app.br:23248/apiargus/',   #TK 23248
                '7': 'http://apioci.argus.app.br:23451/apiargus/',   #3P 23451
                '8': 'http://apioci.argus.app.br:23316/apiargus/',   #Vision 23316
                '9': 'http://apioci.argus.app.br:23435/apiargus/'}   #2A 23435

    if n in empresa:

        texto = empresa[n]
        url_nm = texto.split(':')[-1].strip()
        api_link = api_link[n]

        # URL da API para onde será enviado o arquivo
        url = f'{api_link}{url_nm}/uploadmailing'

        # Informações de autenticação
        token_signature = token[n]
        usuario = 'planejamento'
        senha = 'vieira@10'

        # Abrir o arquivo em modo binário
        with open(file_path, 'rb') as file:
            # Obter o número de linhas do arquivo
            num_lines = sum(1 for line in file)

            # Obter o tamanho do arquivo em MB
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)

            # Voltar para o início do arquivo
            file.seek(0)

            # Construir o cabeçalho de autenticação
            headers = {
                'Token-Signature': token_signature,
                'Usuario': usuario,
                'Password': senha
            }


            # Enviar a requisição POST com o arquivo como payload e o cabeçalho de autenticação
            response = requests.post(
                url, files={'arquivo': file}, headers=headers)


            # Verificar a resposta
            if response.status_code == 200:
                response_data = response.json()  # Obter os dados da resposta em formato JSON

                # Exibir informações sobre o upload
                print('Arquivo enviado com sucesso!')
                print(f'Número de linhas do arquivo: {num_lines}')
                print(f'Tamanho do arquivo: {file_size_mb:.2f} MB')
                print(f'Nome do arquivo: {os.path.basename(file.name)}',)
                # Obter o nome do arquivo local
            else:
                print(
                    f'Erro na requisição: {response.status_code} - {response.reason}')


    else:
        print(f'Número {n} não encontrado no dicionário.')
    sleep(5)
    return


def up_mailing(qt_base):
    # print('Hello World!',end='\n')
    # print(f'Opção selecionada {op}')
    while True:
        limp()
        if qt_base == 1:
            title = 'Você optou por subir uma \033[32munica\033[0m vez a base'
            
        elif qt_base ==2:
            title = 'Você optou por subir a base \033[32mvarias\033[0m vezes'
        
        menu = f'''
            Parceiros e Vieira:
            
            1. Vieiracred SL1
            2. Vieiracred SL3
            3. Prado
            4. GBR
            5. KR
            6. TK
            7. 3P
            8. Vision
            9. 2A            
            0. Sair
            
            
            1001. \033[37mMudar a quantidade de uploading\033[0m
        '''
        
        print(title)
        print(menu)
        op = int(input('Digite a opção desejada: '))
        if op == 0:
            limp()
            return
        elif op == 1001:
            limp()
            tipos = {1:'\033[32mvarias\033[0m', 2:'\033[32munica\033[0m'}
            if qt_base in tipos:
                print(f'Mudando para {tipos[qt_base]}')
                sleep(3)
                if qt_base == 1:
                    qt_base = 2
                    up_mailing(qt_base)
                elif qt_base == 2:
                    qt_base = 1
                    up_mailing(qt_base)
            return
            
        elif op == 1:
            limp()
            abrir_janela_arquivo(op, qt_base)
            limp()
        elif op == 2:
            limp()
            abrir_janela_arquivo(op, qt_base)
            limp()
        elif op == 3:
            limp()
            abrir_janela_arquivo(op, qt_base)
            limp()
        elif op == 4:
            limp()
            abrir_janela_arquivo(op, qt_base)
            limp()
        elif op == 5:
            limp()
            abrir_janela_arquivo(op, qt_base)
            limp()
        elif op == 6:
            limp()
            abrir_janela_arquivo(op, qt_base)
            limp()
        elif op == 7:
            limp()
            abrir_janela_arquivo(op, qt_base)
            limp()
        elif op == 8:
            limp()
            abrir_janela_arquivo(op, qt_base)
            limp()
        elif op == 9:
            limp()
            abrir_janela_arquivo(op, qt_base)
            limp()
        elif op == 15:
            limp()
            abrir_janela_arquivo(op, qt_base)
            limp()
        else:
            print('Digite uma opção valida')
            sleep(5)
            limp() 
    
    
    
    
    