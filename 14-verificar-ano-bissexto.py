# == == == == == == == == == == == == == == == == == == == == == =
# 7. VERIFICADOR DE ANO BISSEXTO
# == == == == == == == == == == == == == == == == == == == == == =

# Enunciado:
# Faca um programa que determine se um ano inserido pelo usuario e bissexto ou nao.
# Lembre-se:
# - Um ano e bissexto se for divisivel por 4
# - Mas anos divisiveis por 100 so sao bissextos se tambem forem divisiveis por 400.

# Instrucoes:
# - Solicite que o usuario digite um ano.
# - Verifique se ele e bissexto ou nao, de acordo com as regras descritas.
# - Exiba uma mensagem informando se o ano e bissexto.

# Explicacao:
# - Este exercicio explora o uso de operadores logicos e condicionais compostos.
# - Trata-se de uma aplicacao classica que ajuda a desenvolver o raciocinio para multiplas condicoes encadeadas.
# - Teste com diferentes anos para validar a logica.

print("Me informe o ano para verificar se é bissexto")
ano = int(input("Ano: "))
def bissexto(x): return x % 4 == 0 and (x % 100 != 0 or x % 400 == 0)


if bissexto(ano):
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")
