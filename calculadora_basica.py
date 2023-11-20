def calculadora_basica():
    print("\n1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Salir\n")
    eleccion = int(input("Elige una opción: "))
    
    if eleccion == 7:
        return None
    elif eleccion < 1 or eleccion > 7:
        print("\nOpción no válida. Por favor, elige una opción entre 1 y 7.")
        calculadora_basica()
    
    num1 = float(input("Ingresa el primer número: "))
    
    if eleccion != 6:
        num2 = float(input("Ingresa el segundo número: "))
    
    if eleccion == 1:
        print("\nResultado: ", num1 + num2)
    elif eleccion == 2:
        print("\nResultado: ", num1 - num2)
    elif eleccion == 3:
        print("\nResultado: ", num1 * num2)
    elif eleccion == 4:
        if num2 != 0:
            print("\nResultado: ", num1 / num2)
        else:
            print("\nError: División por cero no está permitida.")
    elif eleccion == 5:
        print("\nResultado: ", num1 ** num2)
    elif eleccion == 6:
        if num1 >= 0:
            print("\nResultado: ", num1 ** 0.5)
        else:
            print("\nError: Raíz cuadrada de un número negativo no está permitida.")
    calculadora_basica()