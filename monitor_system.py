
# Basic Monitoring System

def monitor_system(temperature, pressure, humidity):
    if temperature == 0 and pressure == 0 and humidity == 0:
        return "System inactive"
    elif temperature > 25:
        return "Warning: High temperature"
    elif humidity > 50:
        return "Warning: High humidity"
    else:
        return "System normal"


# Example test
result = monitor_system(30, 0, 60)
print(result)
