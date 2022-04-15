import requests
import os
from colorama import Fore, Style
os.system('clear')

def Main():

    try:
        CEP = input('DIGITE UM CEP: ')
        CEP = CEP.replace('-', '')
        CEP = int(CEP)
        print('\n')

    except:
        os.system('clear')
        print('Digite um número de cep válido! (Ex: 01001000) ou (Ex: 01001-000)')
        exit()

    digit_count = str(CEP)

    if len(digit_count) == 8:
        r = requests.get(f'https://viacep.com.br/ws/{CEP}/json/')
        json_data = r.json()
        arrays = ['cep', 'logradouro', 'complemento', 'bairro', 'localidade', 'uf', 'ibge', 'gia', 'ddd', 'siafi']

        def Response(ArraysItem):
            print(f'{Fore.GREEN}{arrays[ArraysItem].upper()}:{Style.RESET_ALL} {json_data[arrays[ArraysItem]]}')

        for item in range(9):
            Response(item+1)

    else:
        print(digit_count)
        os.system('clear')
        print('Voce não digitou um cep com 8 dígitos! (Ex: 01001000) ou (Ex: 01001-000)')
        
Main()