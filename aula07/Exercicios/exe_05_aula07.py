# Calcular desvio padrão de uma lista
def calcular_media(lista: list[float]) -> float:
    return sum(lista) / len(lista)
    
def diferenca_ao_quadrado(lista: list[float]) -> list[float]:
    media = calcular_media(lista)

    diferencas = []

    for elemento in lista:
        diferencas.append((elemento - media) ** 2)

    return diferencas

def calcular_devio_padrao(lista: list[float]) -> float:
    quadrados = diferenca_ao_quadrado(lista)

    variantes = sum(quadrados) / len(quadrados)
    
    return variantes ** 0.5


# Programa
lista_c: list[float] = [2, 4, 6, 8]

print(f'\nDesvio padrão: {calcular_devio_padrao(lista_c):.2f}')
