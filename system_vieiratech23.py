import pandas as pd
import os
from time import sleep
from datetime import datetime
from uploading_argus import up_mailing

def limp():
    os.system('cls')

def main():
    while True:
        limp()    
        sleep(3)
        
        title = f'''
            Sistema interativo VieiraTech - Beta v1.3.2504
        '''
        menu = f'''           
            1. Subir base            
            2. Uploading em Loop
            3. Formatar Maciça
            0. Sair
        '''
        print(title)
        print(menu)
        try:
            op = int(input('Digite a opção desejada: '))
            break
        except ValueError:
            print('Digite um número inteiro válido.')
        if op == 0:
            limp()
            print('Obrigado por utilizar nosso aplicativo em fase BETA v3.5.2504')
            sleep(3)
            limp()
            return
        elif op == 1:
            limp()
            up_mailing(op)
            limp()
            print('Voltando ao menu inicial...')
            sleep(3)
            limp()
        elif op == 2:
            limp()
            up_mailing(op)
            limp()
            print('Voltando ao menu inicial...')
            sleep(3)
            limp()
        elif op == 3:
            limp()
            print('Estamos em desenvolvimento....', end='\n')
            sleep(2)
            limp()
            print('Voltando ao menu inicial...')
            sleep(3)
            limp()
        
        else:
            print('Digite uma opção valida')
            sleep(2)
            limp()


main()