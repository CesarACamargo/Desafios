### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# Define os dados
num = [10, 20, 30]

# Descobrir limites
nr_maior = max(num)
nr_menor = min(num)

# Descobrir o tamanho do intervalo
intervalo = nr_maior - nr_menor

nova_lista = []

# Percorre cada elemento
for n in num :

    # Aplica a normalização
    p1 = (n - nr_menor) / intervalo

    # Guarda os novos valores
    nova_lista.append(p1)

# Imprime a lista final
print(nova_lista)