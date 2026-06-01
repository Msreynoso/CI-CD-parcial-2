from validaciones import validar_entero


def suma(a, b):
    validar_entero(a)
    validar_entero(b)
    return a + b


def resta(a, b):
    validar_entero(a)
    validar_entero(b)
    return a - b


def multiplicacion(a, b):
    validar_entero(a)
    validar_entero(b)
    return a * b


def division(a, b):
    validar_entero(a)
    validar_entero(b)
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    if a % b != 0:
        raise ValueError("La división debe dar un entero exacto")
    return a // b
