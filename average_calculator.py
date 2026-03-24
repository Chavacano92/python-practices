cantidad = int(input("¿Cuántos alumnos hay?: "))

suma = 0
contador = 0

while contador < cantidad:
    calificacion = float(input(f"Ingresa la calificación {contador + 1}: "))
    suma += calificacion
    contador += 1

promedio = suma / cantidad

print(f"El promedio es: {promedio:.2f}")
