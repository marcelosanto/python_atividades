# == == == == == == == == == == == == == == == == == == == == == =
# 13. PALINDROMO
# == == == == == == == == == == == == == == == == == == == == == =

# Crie uma funcao que verifique se uma palavra ou frase e um palindromo
# (le-se igual de tras para frente, ignorando espacos e pontuacao).
# Se o resultado E True, responda â€œSimâ€, se o resultado for False, responda â€œNao"

texto = input("Digite uma plavra ou uma frase: ")
palindromo = ""

for x in reversed(texto):
    palindromo += x.lower()

if palindromo == texto.lower():
    print(f"'{texto}' é um palindromo")
else:
    print(f"'{texto}' não é um palindromo")
