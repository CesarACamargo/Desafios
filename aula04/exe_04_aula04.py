# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um 
# dicionário.

# Cria um dicionario vazio
contador: dict = {}   

texto = str(input('\nDigite alguma palavra: '))

# Percorrer cada caractere da string
for caractere in texto :

    # Verifica se a letra já apareceu antes
    if caractere in contador:

        # Incrementa a quantidade
        contador[caractere] += 1

    else:
        # Senão cria a primeira ocorrencia
        contador[caractere] = 1

print(f'\n {contador} \n')

