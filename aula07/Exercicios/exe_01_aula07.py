# Calcular Média de Valores em uma lista
# def media(valor: float) -> float:
#     return sum(valor) / len(valor)

# # Programa
# lista: list[float] = [1, 31, 23, 12, 44]

# print(f"A media dos valores {lista} é {media(lista)}")


def media(lista: list[float]) -> float:
    valor: float = 0
    contador: int = 0

    for item in lista:
        valor += item
        contador += 1

    return valor / contador

# Programa
lista: list[float] = [1, 31, 23, 12, 44]

print(f"A media dos valores é {media(lista)}.")
