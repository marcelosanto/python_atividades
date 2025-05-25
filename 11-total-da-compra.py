# == == == == == == == == == == == == == == == == == == == == == =
# 4. TOTAL DA COMPRA
# == == == == == == == == == == == == == == == == == == == == == =

# Objetivo:
# Calcular o valor total a ser pago por um determinado numero de unidades de um produto.

# Instrucoes:
# - Escreva um programa que armazene o nome de um produto, seu preco unitario e a quantidade comprada.
# - Calcule o valor total da compra e apresente uma descricao detalhada da transacao.

# Explicacao:
# - O valor total e obtido multiplicando o preco unitario pela quantidade comprada.
# - Alem do calculo, a clareza na apresentacao das informacoes e essencial para a compreensao do usuario.
# - O programa deve fornecer uma visao geral da compra, como se fosse um recibo simples.

nome_produto = "Apple iPhone 15 (128 GB) - Preto"
preco_unitario = 7.209
qtd_comprada = 15
subtotal = preco_unitario * qtd_comprada


print("="*45)
print("        SHOPPING DA NUVEM DO JOSÉ")
print("-"*45)
print(f"1. {nome_produto[:30]:33} {preco_unitario:7.2f}")
print(f"2. Quantidade comprada{'':12} {qtd_comprada:7}")
print(f"3. Subtotal{'':27} {subtotal:7.2f}")
print("-"*45)
print("          #123445557932BR")
print("="*45)
