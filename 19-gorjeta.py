# == == == == == == == == == == == == == == == == == == == == == =
# 12. GORJETA
# == == == == == == == == == == == == == == == == == == == == == =

# Enunciado:
# Crie uma funcao que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.
# Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.â€‹

# â€‹ParÃ¢metros: â€‹

# - valor_conta(float): O valor total da contaâ€‹
# - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15 %)â€‹

# â€‹Retorna: â€‹
# O valor da gorjeta calculadaâ€‹â€‹

valor_conta = int(input("Informe o valor da conta: "))
porcentagem = int(input("Informe a porcentagem da gorjeta: "))

valor_da_gorjeta = (porcentagem/100) * valor_conta

print(
    f"A porcentagem da gorjeta sobre o valor da conta: {valor_conta} é {valor_da_gorjeta}")
