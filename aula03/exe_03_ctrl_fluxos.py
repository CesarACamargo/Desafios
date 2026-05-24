### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

logs = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
#logs = {'timestamp': '2021-06-23 10:00:00', 'level': 'INFO', 'message': 'Processo iniciado'}

if logs['level'] == 'ERROR':
    print(logs['message'])


# print(logs)
# print(logs.values())    # Mostrando todos os valores
# print(logs.keys())      # Mostrando todas as chaves  
# print(logs.items())     # Mostrando chaves e valores

# print(logs['level'])    # Mostrando a chave 'level'
# print(logs['message'])  # Mostrando o valor 'message'

# for k,v in logs.items():
#     print(f"\nO {k} é {v}.")

