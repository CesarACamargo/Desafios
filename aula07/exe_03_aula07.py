# Conte quantos valores distintos existem na lista
def distintos(valores: list[int]) -> int:
    uniq: list[int] = []

    for item in valores:

        if item not in uniq:
            uniq.append(item)
            
    return len(uniq)

# Programa
valores: list[int] = [1, 2, 3, 2, 1, 4]

print(f"\nValores distintos: {distintos(valores)}")
