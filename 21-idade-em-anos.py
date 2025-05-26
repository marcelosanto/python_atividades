# == == == == == == == == == == == == == == == == == == == == == =
# 14. IDADE EM ANOS
# == == == == == == == == == == == == == == == == == == == == == =

# Crie uma funcao que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

ano = int(input("Digite seu ano de nascimento: "))
dias_estimados = (2025 - ano) * 365

print(f"Você viveu aproximadamente {dias_estimados} dias.")
