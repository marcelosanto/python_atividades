# == == == == == == == == == == == == == == == == == == == == == =
# 10. VERIFICADOR DE SENHAS
# == == == == == == == == == == == == == == == == == == == == == =

# - Crie um programa que verifique se uma senha e forte.
# - Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um numero.
# - O programa deve continuar pedindo senhas ate que uma senha valida seja inserida ou o usuario digite 'sair'.

sair = ""
digito = ""
while True:

    if sair == "sair":
        break
    else:
        print("Informe a senha ou digite 'sair' para terminar o programa")
        digito = input(": ")

    if digito.lower() == "sair":
        break
    elif len(digito) >= 8:
        for senha in digito:
            if senha.isdigit():
                print("Essa senha é válida, atè mais.")
                sair = "sair"
                break
