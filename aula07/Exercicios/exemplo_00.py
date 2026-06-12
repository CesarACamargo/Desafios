# Minha primeira função

numero1: float = float(input("\nDigite o 1o numero: "))
numero2: float = float(input("Digite o 2o numero: "))

def soma(numero1, numero2) -> float:
    """
    Uma função simples de soma de valores do tipo float que retorna float
    """
    resultado = numero1 + numero2
    return resultado

resultado = soma(numero1, numero2)
print(f"\nA soma é {resultado}")
