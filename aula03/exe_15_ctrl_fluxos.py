### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

mlista = [1, 2, 3, 999, 4, 5]

vl_stop = 999

for v in mlista :
    if v == vl_stop:
        print(f"\nValor de parada {v}...\n")
        break

    print(f'Processando item: {v}')


# itens = [1, 2, 3, "parar", 4, 5]

# i = 0
# while i < len(itens):
#     if itens[i] == "parar":
#         print("Parada encontrada, encerrando o processamento.")
#         break
#     # Processa o item
#     print(f"Processando item: {itens[i]}")
#     i += 1