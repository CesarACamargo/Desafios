# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, 
# imprima o dia, o mês e o ano separadamente.

dt = input("Digite uma data no formato DD/MM/AAAA: ")

if len(dt) == 0 :
    print("Erro: Não foi digitado nada !!")

else:
        
    separa = dt.split("/")

    print(f"Dia: {separa[0]}")
    print(f"Mes: {separa[1]}")
    print(f"Ano: {separa[2]}")
