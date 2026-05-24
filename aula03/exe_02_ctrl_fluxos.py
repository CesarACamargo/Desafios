### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

try:
    tmp = int(input("\nDigite a temperatura em Celsius: "))

    print(f"\nTemperatura atual: {tmp:.2f}°C")

    if tmp < 18:
        print("\nClassificação BAIXA.")

    elif tmp >= 18 and tmp < 28 :
        print("\nClassificação NORMAL.")

    else:
        print("\nClassificação ALTA.")

except ValueError:
    print("\nErro: Digite apenas números.")

