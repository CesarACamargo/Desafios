### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

qtd = int(input("Informe a quantidade: "))
prc = int(input("Informe preco: "))

if qtd > 0 and prc > 0 :
    print("Dados válidos !!!")
else:
    print("Dados inválidos !!!")
