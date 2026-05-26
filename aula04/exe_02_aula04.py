# 2) Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

languages: list = ["Python", "Java", "C++", "JavaScript"]

## Mudando itens da lista
# languages[2] = "Ruby"

## Remove um item especificado, no caso "C++"
# languages.remove("C++")

## Remove um item atraves do index
languages.pop(2)

## Adiciona um item
languages.append("Ruby")

print(languages)