# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
tmp = float(input("Digite a temperatura em Celsius: "))

c = tmp * 1.8
f = c + 32

print(f"{tmp:.2f}°C é igual a {f:.2f}°F")
