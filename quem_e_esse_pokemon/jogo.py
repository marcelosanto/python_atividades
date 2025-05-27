import time
from ascii import imagem_url_para_ascii
from pokemon import obter_pokemon_aleatorio
from jogador import carregar_jogadores, salvar_jogadores
import random


def mostrar_progresso(nome, dicas):
    return ''.join([letra if i in dicas else '_' for i, letra in enumerate(nome)])


def jogo():
    jogadores = carregar_jogadores()
    nome_jogador = input("Digite seu nome: ").strip().lower()

    if nome_jogador in jogadores:
        print(f"\n🔄 Bem-vindo de volta, {nome_jogador}!")
        moedas = jogadores[nome_jogador]['moedas']
        rank = jogadores[nome_jogador]['rank']
    else:
        print(f"\n👋 Olá, {nome_jogador}! Vamos começar.")
        moedas = 50
        rank = 0
        jogadores[nome_jogador] = {"moedas": moedas, "rank": rank}

    print("\n🎮 Bem-vindo ao 'Quem é esse Pokémon?'!")

    while moedas > 0:
        nome, id = obter_pokemon_aleatorio()
        if not nome:
            print("Erro ao obter Pokémon. Tentando novamente...")
            continue

        dicas = set()
        print("\n🔍 Quem é esse Pokémon?")
        imagem_url_para_ascii(
            f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png")

        while True:
            print(f"\n{mostrar_progresso(nome, dicas)}")
            print(f"💰 Moedas: {moedas}")
            acao = input(
                "Digite uma letra, palpite completo ou [pular | dica | desistir]: ").strip().lower()

            if acao == "dica":
                if moedas <= 0:
                    print("❌ Sem moedas suficientes!")
                    continue
                letras_possiveis = [i for i in range(
                    len(nome)) if i not in dicas]
                if letras_possiveis:
                    dicas.add(random.choice(letras_possiveis))
                    moedas -= 1
                else:
                    print("✅ Todas as letras já foram reveladas!")

            elif acao == "pular":
                if moedas <= 0:
                    print("❌ Sem moedas suficientes!")
                    continue
                moedas -= 1
                print(f"⏩ Pulando... O nome era: {nome}")
                time.sleep(1)
                break

            elif acao == "desistir":
                print(f"👋 Você desistiu. O Pokémon era: {nome}")
                jogadores[nome_jogador]['moedas'] = moedas
                jogadores[nome_jogador]['rank'] = rank
                salvar_jogadores(jogadores)
                return

            elif len(acao) == 1:  # tentativa de letra
                indices = [i for i, letra in enumerate(
                    nome) if letra == acao and i not in dicas]
                if indices:
                    dicas.update(indices)
                    print(f"✅ A letra '{acao}' está no nome!")
                else:
                    moedas -= 1
                    print(f"❌ A letra '{acao}' não está no nome. -1 moeda")

            elif acao == nome:
                print(f"🎉 Acertou! Era o {nome.upper()}!")
                moedas += 1
                rank += 1
                break

            else:
                moedas -= 1
                print("❌ Palpite incorreto. -1 moeda")

            if set(range(len(nome))) == dicas:
                print(f"🎉 Você completou o nome! Era {nome.upper()}!")
                moedas += 1
                rank += 1
                break

    print("\n💀 Fim de jogo. Você ficou sem moedas!")
    jogadores[nome_jogador]['moedas'] = 0
    jogadores[nome_jogador]['rank'] = rank
    salvar_jogadores(jogadores)
