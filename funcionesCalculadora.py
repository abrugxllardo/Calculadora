#Abril Gallardo


def menu(numeroUno, numeroDos)-> str:
    """Menu de opciones a elegir

    Returns:
        str: ingreso de la opcion
    """
    limpiarPantalla()
    print(f"{'CALCULADORA':^50s}")
    print("a- Ingresar primer numero")
    print("b- Ingresar segundo numero")
    print("c- Elegir operacion")
    print("d- Mostrar resultado")
    print("e- Salir")
    print(f"A = {numeroUno}")
    print(f"B = {numeroDos}")
    return input("Ingrese opcion: ").lower()

def menuOperaciones():
    """menu de operaciones a elegir
    """
    print("1- Suma")
    print("2- Resta")
    print("3- Multiplicacion")
    print("4- Division")
    print("5- Factorial")

def limpiarPantalla():
    """Limpiar pantalla por cada iteracion
    """
    import os
    os.system("cls")

def pausar():
    """Pausar el programa en cada iteracion
    """
    import os
    os.system("pause")

def ingresarOperando() -> int:
    """Pide al usuario ingresar el operando

    Returns:
        int: el numero ingresado
    """
    while True:
        operando = input("Ingrese un número: ")
        if operando.lstrip('-').isdigit():
            return int(operando)
        else:
            operando = input("Error, ingrese el numero: ")


def suma(numeroUno:int, numeroDos:int)->int:
    """Suma de dos numeros

    Args:
        numeroUno (int): primer operando ingresado
        numeroDos (int): segundo operando ingresado

    Returns:
        int: retorna el resultado de la suma
    """
    resultado = numeroUno + numeroDos
    return resultado

def resta(numeroUno:int, numeroDos:int)->int:
    """Resta de dos numeros

    Args:
        numeroUno (int): primer operando ingresado
        numeroDos (int): segundo operando ingresado

    Returns:
        int: retorna el resultado de la resta
    """
    resultado = numeroUno - numeroDos
    return resultado

def multiplicacion(numeroUno:int, numeroDos:int)->int:
    """Multiplicacion de dos numeros

    Args:
        numeroUno (int): primer operando ingresado
        numeroDos (int): segundo operando ingresado

    Returns:
        int: retorna el resultado de la multiplicacion
    """
    resultado = numeroUno * numeroDos
    return resultado

def division(numeroUno:int, numeroDos:int)->float:
    """Dividion de dos numeros

    Args:
        numeroUno (int): dividendo ingresado
        numeroDos (int): divisor ingresado

    Returns:
        int: retorna el resultado de la division
    """
    if numeroDos == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    else:
        return numeroUno / numeroDos
    

def factorial(numero:int)->int:
    """Calcula el facotiral de un numero

    Args:
        numero (int):Numero a calcular

    Raises:
        ValueError: Valida numero entero natural
        TypeError: Valida tipo entero

    Returns:
        int:Factorial del numero ingresado
    """
    resultado = 1
    if isinstance(numero, bool):
        raise TypeError("No aceptamos booleanos")
    elif isinstance(numero, int):
        if numero < 0:
            raise ValueError("No esta definido el factorial de un negativo")
        for i in range(2, numero + 1):
            resultado *= i
    else:
        raise TypeError("Eso no es un numero")
    return resultado

def mostrarResultado(mensaje:str, resultado:any)-> any:
    """Muestra el resultado de la operacion elegida anteriormente

    Args:
        resultado (int): resultado de la operacion

    Returns:
        str: retorna el mensaje del resultado
    """
    result = print(mensaje,resultado)
    return result

def pedirConfirmacion(mensaje:str)->str:
    """Confirma la salida del programa

    Args:
        mensaje (str): mensaje hacia el usuario

    Returns:
        str: retorna la respuesta del usuario
    """
    rta = input(mensaje).lower()
    return rta == "si"

