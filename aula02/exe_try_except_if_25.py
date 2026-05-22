# 25: Conversão de Tipo com Validação
try:
    numero = int(input("Digite um numero: "))
    print(numero)

except ValueError:
    print("Digite apenas numeros.")