# Filtrar Dados Acima de um Limite

def filtrar_acima_de(valores: list[float], limite: float) -> list[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado

# Programa
lista: list[float] = [5, 12, 30, 8, 25]
limite: float = 10

print(f"O limite é {filtrar_acima_de(lista,limite)}.")
