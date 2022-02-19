import requests
import os
os.system('clear')

# Verifica se a api está online
def Main():
    url = 'https://viacep.com.br/ws/01001000/json/'
    r = requests.get(url)

    if r.status_code != 200:
        print('Api offline!')

    # Faz a consulta do cep na api
    else:
        CEP = input(str('Digite o CEP: '))
        r2 = requests.get(f'https://viacep.com.br/ws/{CEP}/json/')

        if r2.status_code != 200:
            print('Erro ao fazer a consulta! Verifique a númeração.')

        else:
            data = r2.json()
            print('\nCEP:', data['cep'])
            print('LOGRADOURO:', data['logradouro'])
            print('COMPLEMENTO:', data['complemento'])
            print('BAIRRO:', data['bairro'])
            print('LOCALIDADE:', data['localidade'])
            print('UF:', data['uf'])
            print('IBGE:', data['ibge'])
            print('GIA:', data['gia'])
            print('DDD:', data['ddd'])
            print('SIAFI:', data['siafi'])
Main()
