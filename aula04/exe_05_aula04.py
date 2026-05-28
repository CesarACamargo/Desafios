# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
# calcule o preço total da lista de compras.

frutas: list = ["maçã", "banana", "cereja"]
precos: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

# Começa com o total zerado
total = 0

# Percorre cada fruta
for fruta in frutas :

    # Busca o preço correspondente
    preco_fruta = precos[fruta]

    # Mostrando item por item
    print(f'\n{fruta}: R$ {preco_fruta}')
    
    # Soma o acumulador
    total += preco_fruta

# Mostra o resultado
print(f'\nTotal da lista de compra: R$ {total}\n')

