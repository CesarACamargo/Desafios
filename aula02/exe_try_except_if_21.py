# 21: Conversor de Temperatura
try:
    tmp = float(input("Digite a temperatura em Celsius: "))

    f = (tmp * 1.8) + 32

    print(f"{tmp:.2f}°C é igual a {f:.2f}°F")

except ValueError:
    print("Erro: digite apenas números.")

