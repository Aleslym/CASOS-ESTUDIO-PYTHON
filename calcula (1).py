while True:
    print("Calculadora")
    print("1. Operaciones básicas (suma, resta, multiplicación, división)")
    print("2. Operaciones numéricas (decimal a binario, binario a decimal)")
    print("3. Conversión de temperatura (Celsius a Fahrenheit)")
    print("4. IMC")
    print("5. Conversión de unidades de medida (cm a mt, mt a cm, mt a km, km a mt)")
    print("6. Conversión de unidades de tiempo (segundos a minutos, minutos a horas, horas a minutos y segundos)")
    print("0. Finalizar")
    opcion = int(input("Ingrese la opción a realizar: "))

    if opcion == 0:
        print("Muchas gracias")
        break

    if opcion == 1:
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        opcion_operacion = int(input("Ingrese la opción a realizar: "))

        numero1 = int(input("Ingrese un número: "))
        numero2 = int(input("Ingrese un segundo número: "))

        if opcion_operacion == 1:
            print("La suma de los dos números es:", numero1 + numero2)
        elif opcion_operacion == 2:
            print("La resta de los dos números es:", numero1 - numero2)
        elif opcion_operacion == 3:
            print("La multiplicación de los dos números es:", numero1 * numero2)
        elif opcion_operacion == 4:
            if numero2 != 0:
                print("La división de los dos números es:", numero1 / numero2)
            else:
                print("No se puede dividir por cero")

    elif opcion == 2:
        print("1. Decimal a binario")
        print("2. Binario a decimal")
        opcion_operacion = int(input("Ingrese la opción a realizar: "))

        numero = int(input("Ingrese un número: "))
        
    if opcion_operacion == 1:
        (numero_decimal)  = int(input("Ingrese un número decimal: "))
        binario = bin(numero_decimal)[2:]
        print("El número en binario es:", binario)
    elif opcion_operacion == 2:
        numero_binario = input("Ingrese un número binario: ")
        decimal = int(numero_binario, 2)
        print("El número en decimal es:", decimal)



    elif opcion == 3:
        print("Celsius a Fahrenheit")
        celsius = float(input("Ingrese la temperatura en Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print("La conversión de Celsius a Fahrenheit es:", fahrenheit)

    elif opcion == 4:
        altura = float(input("Ingrese su altura en metros: "))
        peso = float(input("Ingrese su peso en kilogramos: "))
        if altura > 0:
            imc = peso / (altura ** 2)
            print("El resultado de su IMC es:", imc)
        else:
            print("La altura debe ser mayor a cero")

    elif opcion == 5:
        print("1. cm a mt")
        print("2. mt a cm")
        print("3. mt a km")
        print("4. km a mt")
        opcion_operacion = int(input("Ingrese la opción a realizar: "))
        
        medida = float(input("Ingrese la medida: "))
        
        if opcion_operacion == 1:
            print("El resultado de la conversión de cm a mt es:", medida / 100)
        elif opcion_operacion == 2:
            print("El resultado de la conversión de mt a cm es:", medida * 100)
        elif opcion_operacion == 3:
            print("El resultado de la conversión de mt a km es:", medida / 1000)
        elif opcion_operacion == 4:
            print("El resultado de la conversión de km a mt es:", medida * 1000)

    elif opcion == 6:
        print("1. Segundos a minutos")
        print("2. Minutos a horas")
        print("3. Horas a minutos")
        print("4. Horas a segundos")
        opcion_operacion = int(input("Ingrese la opción a realizar: "))

        tiempo = float(input("Ingrese el tiempo: "))

        if opcion_operacion == 1:
            print("El resultado de la conversión de segundos a minutos es:", tiempo / 60)
        elif opcion_operacion == 2:
            print("El resultado de la conversión de minutos a horas es:", tiempo / 60)
        elif opcion_operacion == 3:
            print("El resultado de la conversión de horas a minutos es:", tiempo * 60)
        elif opcion_operacion == 4:
            print("El resultado de la conversión de horas a segundos es:", tiempo * 3600)

if opcion ==0:
 continuar = input("¿Desea continuar? (Sí/No): ")
if continuar.lower() != "sí":
            print("Muchas gracias")
