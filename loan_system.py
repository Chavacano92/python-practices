while True:
    edad = int(input("Ingresa la edad: "))

    # Condición para terminar
    if edad < 18 or edad > 65:
        print("Edad inválida. Fin del programa.")
        break

    salario = float(input("Ingresa el salario mensual: "))

    # 18 - 25 años
    if 18 <= edad <= 25:
        if salario < 10000:
            print("No es elegible para préstamo")
        elif 10000 <= salario <= 20000:
            print("Préstamo: $50,000 | Interés: 10%")
        else:
            print("Préstamo: $100,000 | Interés: 8%")

    # 26 - 40 años
    elif 26 <= edad <= 40:
        if salario < 15000:
            print("No es elegible para préstamo")
        elif 15000 <= salario <= 30000:
            print("Préstamo: $100,000 | Interés: 7%")
        else:
            print("Préstamo: $200,000 | Interés: 5%")

    # 41 - 65 años
    elif 41 <= edad <= 65:
        if salario < 20000:
            print("No es elegible para préstamo")
        elif 20000 <= salario <= 40000:
            print("Préstamo: $150,000 | Interés: 6%")
        else:
            print("Préstamo: $300,000 | Interés: 4%")

    print("-" * 40)
