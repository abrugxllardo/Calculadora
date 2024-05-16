#Abril Gallardo
from funcionesCalculadora import *

flagPrimerNumero = False
flagSegundoNumero = False
flagResultado = False
seguir = "si"

numeroUno = 0
numeroDos = 0
while seguir == "si":
    match menu(numeroUno, numeroDos):
        case "a":
            numeroUno = ingresarOperando()
            flagPrimerNumero = True
        case "b":
            if flagPrimerNumero:
                numeroDos = ingresarOperando()
                flagSegundoNumero = True
            else: 
                print("Primero debes ingresar el primer numero")
        case "c":
            if flagSegundoNumero:
                menuOperaciones()
                operacion = int(input("Elige la operacion: "))
                while operacion < 0 or operacion > 5:
                    operacion = int(input("Error, elige la operacion nuevamente: "))

                if operacion == 1:
                    resultado = suma(numeroUno, numeroDos)
                    mensaje = f"El resultado de la suma de {numeroUno} y {numeroDos} es: "
                elif operacion == 2:
                    resultado = resta(numeroUno, numeroDos)
                    mensaje = f"El resultado de la resta de {numeroUno} y {numeroDos} es: "
                elif operacion == 3:
                    resultado = multiplicacion(numeroUno, numeroDos)
                    mensaje = f"El resultado de la mulriplicacion de {numeroUno} y {numeroDos} es: "
                elif operacion == 4:
                    try:
                        resultado = division(numeroUno, numeroDos)
                        mensaje = f"El resultado de la division de {numeroUno} y {numeroDos} es: "
                    except ZeroDivisionError as e:
                        mensaje = e
                        resultado = f"Intenta nuevamente!"
                else:
                    try:
                        resultado = factorial(numeroUno)
                        mensaje = f"El factorial de {numeroUno} es: "
                    except ValueError as e:
                        mensaje = e
                        resultado = f"Intenta nuevamente!"
                    except TypeError as e:
                        mensaje = e
                        resultado = f"Intenta nuevamente!"

                flagResultado = True

            else:
                print("Primero debe ingresar dos numeros")
        case "d":
            if flagResultado:
                mostrarResultado(mensaje, resultado)
                flagPrimerNumero = True
                flagSegundoNumero = True
                flagResultado = True
                numeroUno = 0
                numeroDos = 0
            else: 
                print("primero debes hacer una operacion")
        case "e":
            if pedirConfirmacion("Confirmar salida si/no: "):
                seguir = "no"
            continue
    pausar()