# Exercício 1 – Criando suas primeiras variáveis
# Crie um programa para armazenar algumas informações sobre uma seleção:

# nome da seleção;
# quantidade de títulos;
# posição no ranking;
# se está classificada para a Copa.


selecao_nome = "Brasil"
quant_titulo = 5
posicao_ranking = 11
classificado = True

print(f"\nNome da selecao: {selecao_nome}")
print(f"Quantidade de Titulos: {quant_titulo}")
print(f"Posicao do Ranking FIFA: {posicao_ranking}")

if classificado and posicao_ranking <= 10:
    print(f"\nSeleção classificada e entre as 10 melhores.\n")

elif classificado:
    print(f"\nClassificado, mas fora do TOP 10.\n")
    
else:
    print(f"\nA seleção não foi classificada.\n")
    

