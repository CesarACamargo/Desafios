### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

try:

    idade = int(input("\nDigite a sua idade: "))

    if idade >= 18 and idade <= 65 :
        print("\nDados de usuário válidos !!")

    else:
        print("\nIdade não permitida para recomendação !")
        exit()

except ValueError:
    print("\nErro: Digite apenas números.")


email = input("\nDigite o seu e-mail: ")

if "@" in email and "." in email :
    print("\nE-mail válido !")

else:
    print("\nE-mail inválido !")

