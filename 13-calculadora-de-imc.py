# == == == == == == == == == == == == == == == == == == == == == =
# 6. CALCULADORA DE IMC
# == == == == == == == == == == == == == == == == == == == == == =

# Enunciado:
# Desenvolva um programa que calcule o Indice de Massa Corporal(IMC) de uma pessoa.
# O programa deve solicitar o peso(em kg) e a altura(em metros), calcular o IMC e informar a classificacao de acordo com a tabela padrao.

# Instrucoes:
# - Solicite os dados do usuario: peso e altura.
# - Calcule o IMC usando a formula: IMC = peso / (altura ** 2).
# - Exiba o valor do IMC com uma casa decimal e a respectiva classificacao(ex: abaixo do peso, normal, sobrepeso etc.).

# Explicacao:
# - O exercicio envolve entrada de dados numericos com ponto flutuante, calculos matematicos e estruturas condicionais.
# - A classificacao deve seguir os intervalos padrao definidos para o IMC.
# - Apresente o resultado de forma clara e arredondado corretamente.

print("Olá seja bem vinda/o a calculadora de IMC")
peso = float(input("Poderia me informa seu peso: "))
altura = float(input("Poderia me informa sua altura em cm: "))

imc = peso / ((altura/100) ** 2)

print(f"\nSeu IMC é: {imc:.2f}")


if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com o peso normal.")
elif imc < 30:
    print("Você está com sobrepeso.")
elif imc < 35:
    print("Obesidade grau I.")
elif imc < 40:
    print("Obesidade grau II (severa).")
else:
    print("Obesidade grau III (mórbida).")
