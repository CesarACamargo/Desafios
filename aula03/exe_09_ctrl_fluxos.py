### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = [3, 8, 15, 22, 7, 10, 31, 44, 19, 50, 27, 62, 13, 18]

# Nova lista vazia
lista_par = []

# Percorre a lista
for n in numeros:

    # Verifica se o numero é par
    if n % 2 == 0 :

        # Adiciona os pares em outra lista
        lista_par.append(n)
        
# Ordena os resultados        
lista_par.sort()

# imprime a lista final
print(lista_par)


