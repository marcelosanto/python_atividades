import random
import requests


def obter_pokemon_aleatorio():
    id = random.randint(1, 151)
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        nome = dados['name'].lower()
        return nome, id
    else:
        return None, None
