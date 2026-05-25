### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

dados = list()
entrada = ""

while entrada.lower() != "sair":
    entrada = input("Digite um valor ou 'sair' para terminar: ")
    dados.append(entrada)
    if entrada.lower() == "sair":
        dados.pop()
 
print(dados)
