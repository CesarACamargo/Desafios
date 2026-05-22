# 23: Calculadora Simples
try:

    n1 = float(input("Insira um numero: "))
    n2 = float(input("Insira outro numero: "))

    print("Escolha a operação que deseja realizar: ")
    opc = int(input("1-Soma  2-Subtracao  3-Divisao  4-Multiplicao  5-Percentual: "))

    def soma(n1,n2):
        return n1 + n2

    def subt(n1,n2):
        return n1 - n2

    def div(n1,n2):
        return n1 / n2

    def mult(n1,n2):
        return n1 * n2

    def perc(n1,n2):
        return n1 * n2 / 100

    if opc == 1:
        print(soma(n1,n2))

    elif opc == 2:
        print(subt(n1,n2))

    elif opc == 3:
        print(div(n1,n2))

    elif opc == 4:
        print(mult(n1,n2))

    elif opc == 5:
        print(perc(n1,n2))

except ValueError:
    print("Erro: digite apenas números.")

