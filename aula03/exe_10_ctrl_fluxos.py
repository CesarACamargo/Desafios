### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"produto": "Notebook", "categoria": "Eletrônicos", "valor": 3500},
    {"produto": "Mouse", "categoria": "Eletrônicos", "valor": 120},
    {"produto": "Teclado", "categoria": "Eletrônicos", "valor": 250},

    {"produto": "Camiseta", "categoria": "Roupas", "valor": 80},
    {"produto": "Calça Jeans", "categoria": "Roupas", "valor": 150},
    {"produto": "Tênis", "categoria": "Roupas", "valor": 300},

    {"produto": "Arroz", "categoria": "Alimentos", "valor": 40},
    {"produto": "Feijão", "categoria": "Alimentos", "valor": 25},
    {"produto": "Macarrão", "categoria": "Alimentos", "valor": 15},

    {"produto": "Livro Python", "categoria": "Livros", "valor": 90},
    {"produto": "Livro SQL", "categoria": "Livros", "valor": 70}
]

tot_categories = {}

for v in vendas:
    cat = v["categoria"]
    valor = v["valor"]
    if cat in tot_categories:
        tot_categories[cat] += valor
    else:
        tot_categories[cat] = valor

print(tot_categories)

