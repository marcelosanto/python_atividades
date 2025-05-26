import random
import string

def gerar_senha():
    while True:
        try:
            qtd = int(input("Digite o número de caracteres da senha (maior que 0): "))
            if qtd <= 0:
                raise ValueError("A quantidade precisa ser maior que zero.")
            break
        except ValueError as e:
            print(f"Erro: {e}")

    letras = string.ascii_letters       
    numeros = string.digits            
    especiais = string.punctuation      
    
    todos_caracteres = letras + numeros + especiais

    senha = ''.join(random.choices(todos_caracteres, k=qtd))

    print(f"Senha gerada: {senha}")

gerar_senha()
