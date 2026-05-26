# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. 
# Imprima cada informação.

livros: dict = {
    "titulo":"Python for Dummies",
    "autor":"Fulano de Beltrano",
    "ano":"2026"
}

for k, v in livros.items():
    print(f'{k}: {v}')
