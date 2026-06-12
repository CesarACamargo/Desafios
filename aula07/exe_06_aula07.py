# Encontrar Valores Ausentes em uma Sequência
def encontra_ausentes(lista: list[int]) -> list[int]:
    ausentes: list[int] = []

    number_max = max(lista)
    number_min = min(lista)

    sequencia = range(number_min, number_max + 1)

    for numero in sequencia:
        if numero not in lista:
            ausentes.append(numero)

    return ausentes

# Programa
numeral: list[int] = [1, 2, 4, 7, 9]

print(f'\nOs valores ausentes são {encontra_ausentes(numeral)}', end='\n')
