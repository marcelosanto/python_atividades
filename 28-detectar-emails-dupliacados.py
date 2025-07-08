emails = [
    "ana.silva@gmail.com",
    "carlos.mendes@outlook.com",
    "beatriz.costa@yahoo.com.br",
    "joao.pereira@hotmail.com",
    "daniel.oliveira@gmail.com",
    "ana.silva@gmail.com",  # Duplicado
    "eduarda.ferreira@empresa.com.br",
    "fabio.souza@hotmail.com",
    "lucas.rodrigues@yahoo.com.br",
    "gabriela.santos@gmail.com",
    "rafael.carvalho@outlook.com",
    "joao.pereira@hotmail.com",  # Duplicado
    "heitor.almeida@outlook.com",
    "isabela.lima@yahoo.com.br",
    "sofia.ribeiro@hotmail.com",
    "pedro.barbosa@gmail.com",
    "ana.silva@gmail.com",  # Duplicado
    "laura.martins@empresa.com.br",
    "felipe.azevedo@gmail.com",
    "mariana.gomes@hotmail.com"
]


def find_duplicados(lst):
    seen = set()
    duplicados = set()
    for email in lst:
        if email in seen:
            duplicados.add(email)
        seen.add(email)
    return list(duplicados)


print(find_duplicados(emails))


contagem_de_emails = {}

# Itera sobre cada e-mail na lista original
for email in emails:
    # Verifica se o e-mail JÁ É UMA CHAVE no nosso dicionário de contagem
    if email in contagem_de_emails:
        # Se sim, apenas incrementa o valor (a contagem)
        contagem_de_emails[email] += 1
    else:
        # Se não, adiciona o e-mail como uma nova chave com o valor inicial 1
        contagem_de_emails[email] = 1

print(contagem_de_emails)
