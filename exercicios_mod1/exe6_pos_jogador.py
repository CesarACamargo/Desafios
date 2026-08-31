# Utilizando o input(), peça ao usuário para informar a posição de um jogador. As opções esperadas são:

# goleiro
# defesa
# meio
# ataque
# Armazene a resposta em uma variável chamada posicao.

# Depois, utilize match case para verificar a posição informada e mostrar uma mensagem correspondente à função daquele jogador em campo.

# Por exemplo: Digite a posição do jogador: ataque

# Saída esperada: Responsável principalmente pela criação e finalização das jogadas ofensivas.

# Crie também um caso para quando o usuário digitar uma posição diferente das opções esperadas. Nesse caso, mostre: Posição inválida.

print("\nPosições: \n")
print("Goleiro")
print("Defesa")
print("Meio")
print("Ataque\n")

posicao = input("Informe a posição do jogador: ")

match posicao:
    case "Goleiro":
        print(f"\n{posicao} -> Responsavel final de evitar o gol do time adversário.")
    case "Defesa":
        print(f"\n{posicao} -> Responsavel de proteger a área e impedir que os atacantes adversários marquem gols.")
    case "Meio":
        print(f"\n{posicao} -> Responsável pela criação e distribuição de jogadas.")
    case "Ataque":
        print(f"\n{posicao} -> Responsável principalmente pela criação e finalização das jogadas ofensivas.")
    case _:
        print("\nPosição Inválida!")
