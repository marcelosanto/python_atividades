import requests

url = 'https://economia.awesomeapi.com.br/last'

print("Qualo moeda, você gostaria de consultar? USD - EUR - BTC")
moeda = input("Olá, qual moeda, você gostaria de consultar: ").upper()

response = requests.get(f"{url}/{moeda}-BRL")

sigla_moeda = f"{moeda}BRL"
if response.status_code == 200:
    dados = response.json()
    print(dados)
    print(f"alta: {dados[f'{sigla_moeda}']['high']}")
    print(f"baixa: {dados[f'{sigla_moeda}']['low']}")
    print(f"atual: {dados[f'{sigla_moeda}']['bid']}")
else:
    print(f'Erro: {response.status_code}')
