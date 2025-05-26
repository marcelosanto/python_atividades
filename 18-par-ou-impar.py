# == == == == == == == == == == == == == == == == == == == == == =
# 11. PAR OU IMPAR
# == == == == == == == == == == == == == == == == == == == == == =

# Crie um programa que solicite ao usuario que insira numeros inteiros.
# O programa deve continuar solicitando numeros ate que o usuario digite 'fim'.
# Para cada numero inserido, o programa deve informar se e par ou impar.
# Se o usuario inserir algo que nao seja um numero inteiro, o programa deve informar o erro e continuar.
# No final, o programa deve exibir a quantidade de numeros pares e impares inseridos.

pares = 0
impares = 0

print("Digite um numero ou 'fim' para sair do programa")
while True:
    try:
        valor = input("Informe um numero: ")
        if valor.lower() == "fim":
            break
        else:
            if int(valor) % 2 == 0:
                print(f"{valor} é par")
                pares += 1
            else:
                print(f"{valor} é impar")
                impares += 1

    except ValueError:
        print("Digite um numero valido")
        continue


print(f"A qtd de numeros pares é: {pares} e impares é: {impares}")
