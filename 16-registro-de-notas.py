# == == == == == == == == == == == == == == == == == == == == == =
# 9. REGISTRO DE NOTAS
# == == == == == == == == == == == == == == == == == == == == == =

# - Crie um programa que permita a um professor registrar as notas de uma turma.
# - O programa deve continuar solicitando notas ate que o professor digite 'fim'.
# - Notas vÃ¡lidas sÃ£o de 0 a 10.
# - O programa deve ignorar notas invalidas e continuar solicitando.
# - No final, deve exibir a mÃ©dia da turma. Notas = [] -> len(Notas)â€‹

notas = []
print("Informe as notas, para calculo da média ou digite 'fim' pra sair")
nota = 0

while True:
    try:
        digitado = input(": ")

        if digitado == "fim":
            break
        else:
            nota = int(digitado)

        if nota >= 0 and nota <= 10:
            notas.append(nota)
        else:
            continue
    except ValueError:
        continue

if len(notas) > 0:
    print(f"A média das notas é: {sum(notas)/len(notas)}")
else:
    print("Nenhuma nota adicionada.")
