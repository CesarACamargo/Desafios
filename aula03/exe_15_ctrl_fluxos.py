### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

mlista = [10, 20, 30, 999, 40, 50]

vl_stop = 999

for v in mlista :
    if v == vl_stop:
        print(f"\nValor de parada {v}...\n")
        break

    print(v)

