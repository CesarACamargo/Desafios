import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:

    lista = []
    with open(nome_do_arquivo_csv, mode="r", encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            lista.append(linha)
    return lista

vendas_itens: list[dict]

vendas_itens = ler_csv(path_arquivo)
print(vendas_itens)
