data = [
    "Marcelo, marcelo@gg.com",
    "Alice, alice@gg.com",
    "maquerle, mq@gg.com",
    "gabriel, gabriel@gg.com"
]


def limpar_data(linhas):
    resultado = []
    for linha in linhas[1:]:
        nome, email = [partir.strip() for partir in linha.split(",")]
        resultado.append({"nome": nome, "email": email})
    return resultado


print(limpar_data(data))
