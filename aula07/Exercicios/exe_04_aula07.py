# Converter Celsius para Fahrenheit em uma Lista
def fahrenheit(temp_celsius: list[float]) -> list[float]:
    temp_fahr: list[float] = []

    for valor in temp_celsius:
        temperatura = (valor * 9 / 5) + 32
        temp_fahr.append(temperatura)

    return temp_fahr

# Programa
temp_celsius: list[float] = [0, 20, 30]

print(f"\n{fahrenheit(temp_celsius)}", end='\n')