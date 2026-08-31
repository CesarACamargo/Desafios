
pontos = 7
vitorias = 2
saldo_gols = 4

expressao1 = pontos > 5
print(f"\nA seleção possui mais de {pontos} pontos? {expressao1}")

expressao2 = vitorias == 3
print(f"A seleção possui exatamente {vitorias} vitorias? {expressao2}")

expressao3 = saldo_gols >= 0
print(f"Saldo de gols é maior ou igual a 0? {expressao3}")

expressao4 = pontos > 5 and saldo_gols > 0
print(f"A seleção possui mais de 5 pontos e saldo de gols positivo? {expressao4}")

expressao5 = vitorias == 3 or pontos > 6
print(f"A seleção possui 3 vitórias ou mais de 6 pontos? {expressao5}\n")
