import os

os.system("/usr/bin/clear")

## Definir constante
CONSTANTE_BONUS = 1000

# Solicite ao usuario que digite o seu nome
nm = input("Insira o seu nome: ")

# Solicite ao usuario que digite o valor do salario recebido
# Converte a entrada para um numero de ponto flutuante
salario = float(input("Informe o salario: R$ "))

# Solicite ao usuario que digite o valor do bonus recebido
# Converte a entrada para um numero de ponto flutuante
bonus = float(input("Informe o bonus: "))

# Calcule o valor do bonus final
valor_bonus = CONSTANTE_BONUS + salario * bonus

# Imprime a mensagem personalizada incluindo o nome do usuario e o valor do bonus
print(f"O usuario {nm} possui o bonus de {valor_bonus}\n")
