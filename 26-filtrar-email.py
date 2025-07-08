print("Filtrando emails")

empregados = [
    {
        "nome": "Ana Silva",
        "email": "ana.silva@example.com",
        "departamento": "Recursos Humanos"
    },
    {
        "nome": "Carlos Mendes",
        "email": "carlos.mendes@example.com",
        "departamento": "Recursos Humanos"
    },
    {
        "nome": "Beatriz Costa",
        "email": "beatriz.costa@example.com",
        "departamento": "Tecnologia da Informação"
    },
    {
        "nome": "Daniel Oliveira",
        "email": "daniel.oliveira@example.com",
        "departamento": "Tecnologia da Informação"
    },
    {
        "nome": "Eduarda Ferreira",
        "email": "eduarda.ferreira@example.com",
        "departamento": "Marketing"
    },
    {
        "nome": "Fábio Souza",
        "email": "fabio.souza@example.com",
        "departamento": "Marketing"
    },
    {
        "nome": "Gabriela Santos",
        "email": "gabriela.santos@example.com",
        "departamento": "Vendas"
    },
    {
        "nome": "Heitor Almeida",
        "email": "heitor.almeida@example.com",
        "departamento": "Vendas"
    },
    {
        "nome": "Isabela Lima",
        "email": "isabela.lima@example.com",
        "departamento": "Financeiro"
    },
    {
        "nome": "João Pereira",
        "email": "joao.pereira@example.com",
        "departamento": "Financeiro"
    }
]


def filtrar_email(dados, dep):
    return sorted([emp["email"] for emp in dados if emp["departamento"] == dep])


print(filtrar_email(empregados, "Tecnologia da Informação")
      )
