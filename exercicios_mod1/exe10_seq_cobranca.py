gols = 0
chance = 0

for chance in range(5):
    chance += 1
    cobranca = input(f"Resultado da cobrança-{chance}: gol ou perdeu? ")
    
    match cobranca:
        case "gol":
            gols += 1
        case "perdeu":
            pass
        case _:
            print("\nOpção invalida !!!")

print(f"\nTotal de gols: {gols}")
            
if gols >= 4:
    print(f"\nÓtimo desempenho nos pênaltis!")
        
elif gols >= 2:
    print(f"\nDesempenho regular nos pênaltis.")

else:
    print(f"\nDesempenho ruim nos pênaltis.")

