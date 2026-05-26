# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
# calcule o preço total da lista de compras.

frutas: list = ["maçã", "banana", "cereja"]
precos: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

# Começa com o total zerado
total = 0

# Percorre cada fruta
for fruta in frutas :

    # Busca o preço correspondente
    pf = precos[fruta]
    
    # Soma o acumulador
    total += pf

# Mostra o resultado
print(f'\nTotal da lista de compra: R$ {total}\n')

