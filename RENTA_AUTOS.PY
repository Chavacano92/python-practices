# 1. Definimos la función con la lógica de costos
def calcular(tiempo):
    if tiempo < 3:
        total = tiempo * 500
    elif tiempo < 7:
        total = 1200 + (tiempo - 3) * 400
    elif tiempo < 15:
        total = 3000 + (tiempo - 7) * 350
    else:
        total = 6000 + (tiempo - 15) * 300
    return total

# 2. Mensaje inicial
print('Programa para realizar estimaciones de renta de vehículos')

# 3. El ciclo principal (exactamente como lo tiene tu profe)
while True:
    tiempo = int(input('Dime la cantidad de día para la renta: '))
    
    # Condición de salida: si es 0 o menor, el break "rompe" el ciclo
    if tiempo <= 0:
        print("Saliendo del programa...")
        break
    
    # Llamamos a la función y guardamos el resultado
    costo = calcular(tiempo)
    
    # Mostramos el resultado antes de que el ciclo vuelva a empezar
    print(f'El costo total es: ${costo}')
    print('-' * 20)
