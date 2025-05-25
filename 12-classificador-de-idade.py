# == == == == == == == == == == == == == == == == == == == == == =
# 5. CLASSIFICADOR DE IDADE
# == == == == == == == == == == == == == == == == == == == == == =

# Enunciado:
# Crie um programa que solicite a idade do usuario e classifique-o em uma das seguintes categorias:
# - Crianca(0 a 12 anos)
# - Adolescente(13 a 17 anos)
# - Adulto(18 a 59 anos)
# - Idoso(60 anos ou mais)

# Instrucoes:
# - Solicite que o usuario digite sua idade.
# - O programa deve interpretar o valor digitado e classifica-lo de acordo com as faixas etÃ¡rias.
# - O resultado da classificacao deve ser exibido de forma clara.

# Explicacao:
# - Esse exercicio utiliza estruturas condicionais para tomar decisoes baseadas em faixas numericas.
# - Importante tratar casos invalidos, como idades negativas.
# - A logica deve garantir que nenhuma faixa se sobreponha ou fique sem cobertura.

print("Bem vindo ao classificador de idade")
idade = int(input("Poderia me informa a sua idade: "))
classificacao = ""

if idade <= 12:
    classificacao = "uma Crianca"
elif idade > 12 and idade < 18:
    classificacao = "um Adolescente"
elif idade > 18 and idade < 59:
    classificacao = "um Adulto"
else:
    classificacao = "um Idoso"


print(f"Com base na idade fornecida, você é {classificacao}.")
