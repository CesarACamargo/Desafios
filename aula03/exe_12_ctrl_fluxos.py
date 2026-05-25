### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

while True :
    num = int(input("\nDigite um numero entre 1 e 10: "))
    if num >= 1 and num <= 10:
        print("\nNumero válido.")
        break

    else:
        print("\nNumero invalido! ")
        