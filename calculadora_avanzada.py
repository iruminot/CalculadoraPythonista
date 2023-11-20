import math

def calculadora_avanzada():
    print("\n1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    print("4. Logaritmo natural")
    print("5. Logaritmo base 10")
    print("6. Salir\n")
    eleccion = int(input("Elige una opción: "))
    
    if eleccion == 6:
        return
    elif eleccion < 1 or eleccion > 6:
        print("\nOpción no válida. Por favor, elige una opción entre 1 y 6.")
        calculadora()
    
    num = float(input("Ingresa un número: "))
    
    if eleccion == 1:
        print("\nResultado: ", math.sin(num))
    elif eleccion == 2:
        print("\nResultado: ", math.cos(num))
    elif eleccion == 3:
        print("\nResultado: ", math.tan(num))
    elif eleccion == 4:
        if num > 0:
            print("\nResultado: ", math.log(num))
        else:
            print("\nError: Logaritmo de un número no positivo no está permitido.")
    elif eleccion == 5:
        if num > 0:
            print("\nResultado: ", math.log10(num))
        else:
            print("\nError: Logaritmo de un número no positivo no está permitido.")
    
    calculadora()