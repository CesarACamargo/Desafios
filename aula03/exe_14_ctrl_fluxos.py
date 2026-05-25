### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# tentativas = 1

# max_tentativas = 5

# while tentativas <= max_tentativas :
#     print(f"\nTentativa {tentativas} de {max_tentativas}.")
   
#     if True:
#         print("\nConectado.")
#         print()
#         break
#     tentativas += 1
# else:
#     print("\nFalhou após varias tentativas.")

tentativas = 1
max_tentativas = 5

while tentativas <= max_tentativas:
    print(f"\nTentativa {tentativas} de {max_tentativas}.")

    conectado = False  # simulação da conexão

    # Simulando sucesso apenas na terceira tentativa
    if tentativas == 3:
        conectado = True

    if conectado:
        print("\nConectado com sucesso.")
        break
    else:
        print("\nFalha na conexão.")

    tentativas += 1

else:
    print("\nFalhou após várias tentativas.")