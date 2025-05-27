import os

CAMINHO_ARQUIVO = "./quem_e_esse_pokemon/dados/jogadores.txt"


def carregar_jogadores():
    jogadores = {}
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "r") as arquivo:
            for linha in arquivo:
                nome, saldo, rank = linha.strip().split(",")
                jogadores[nome] = {
                    "moedas": int(saldo),
                    "rank": int(rank)
                }
    return jogadores


def salvar_jogadores(jogadores):
    os.makedirs(os.path.dirname(CAMINHO_ARQUIVO), exist_ok=True)
    with open(CAMINHO_ARQUIVO, "w") as arquivo:
        for nome, dados in jogadores.items():
            arquivo.write(f"{nome},{dados['moedas']},{dados['rank']}\n")
