import requests

url = 'https://viacep.com.br/ws'

cep = input("Olá me informe seu cep: ")

response = requests.get(f"{url}/{cep}/json")

if response.status_code == 200:
    dados = response.json()
    print(dados)
    print(f"Rua: {dados['logradouro']}")
else:
    print(f'Erro: {response.status_code}')
