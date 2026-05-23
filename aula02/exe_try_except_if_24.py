# 24: Classificador de Números
try:

    num = int(input("Insira um numero: "))

    if num % 2 == 0 :
        print(f"O numero {num} eh par.")

    else:
        print(f"O numero {num} eh impar.")

    if num >= 0 :
        print(f"O numero {num} eh positivo.")

    else:
        print(f"O numero {num} eh negativo.")

except ValueError:
    print("Erro: Digite apenas números inteiros válidos.") 

