# == == == == == == == == == == == == == == == == == == == == == =
# 8. CALCULADORA
# == == == == == == == == == == == == == == == == == == == == == =
# Desenvolva uma calculadora em Python que realize as quatro operacoes basicas entre dois numeros.
# A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operacao. Siga as especificacoes abaixo: â€‹

# - A calculadora deve solicitar ao usuario que insira dois numeros e uma operacao.â€‹
# - As operacoes validas sao: + (adicao), - (subtracao), * (multiplicacao) e / (divisao).â€‹
# - O programa deve continuar solicitando entradas ate que uma operacao valida seja concluida.â€‹

# Trate os seguintes erros: â€‹

# - Entrada invalida(nÃ£o numerica) para os numerosâ€‹
# - Divisao por zeroâ€‹
# - Operacao invalidaâ€‹

# - Use try / except para capturar e tratar os erros apropriadamente.â€‹
# - Apos cada erro, o programa deve informar o usuario sobre o erro e solicitar nova entrada.â€‹
# - Quando uma operacao e concluida com sucesso, exiba o resultado e encerre o programa.â€‹

print("Informe dois numeros e uma operação")
numero_x = 0
numero_y = 0
operacao = 0

while True:
    try:
        if numero_x == 0:
            numero_x = int(input("Informe o primeiro numero: "))

        if numero_y == 0:
            numero_y = int(input("Informe o segundo numero: "))

        if operacao == 0:
            operacao = int(input(
                "Informe a operação: 1) Somar - 2) Subtrair - 3) Multiplicar - 4) Dividir:  "))

        if operacao == 1:
            print(f"A soma do {numero_x} + {numero_y} = {numero_x+numero_y}")
            break
        elif operacao == 2:
            print(
                f"A subtração do {numero_x} - {numero_y} = {numero_x-numero_y}")
            break
        elif operacao == 3:
            print(
                f"A multiplicação do {numero_x} * {numero_y} = {numero_x*numero_y}")
            break
        elif operacao == 4:
            print(
                f"A divisão do {numero_x} / {numero_y} = {numero_x/numero_y}")
            break
        else:
            operacao = 0

    except ValueError:
        print("Valor digitado errado, digite um numero inteiro valido.")
