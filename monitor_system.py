def monitor_system(temperature, pressure, humidity):
    if temperature == 0 and pressure == 0 and humidity == 0:
        return "System inactive"
    elif temperature > 25:
        return "Warning: High temperature"
    elif humidity > 50:
        return "Warning: High humidity"
    else:
        return "System normal"


# Input del usuario
temperature = float(input("Ingresa la temperatura: "))
pressure = float(input("Ingresa la presión: "))
humidity = float(input("Ingresa la humedad: "))

result = monitor_system(temperature, pressure, humidity)
print(result)
