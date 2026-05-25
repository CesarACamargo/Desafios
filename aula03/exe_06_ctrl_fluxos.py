### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "O rato roeu a roupa do rei de Roma rato"

texto_tratado = texto.replace(",","")
palavras = texto.split()

print(palavras)

contagem_de_palavras = {}

for p in palavras:
    if p in contagem_de_palavras:
        contagem_de_palavras[p] = +1
    else:
        contagem_de_palavras[p] = 1

print(contagem_de_palavras)
