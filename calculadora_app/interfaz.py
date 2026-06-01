from operaciones import suma, resta, multiplicacion, division


OPERACIONES = {
    "1": ("Suma",           "+", suma),
    "2": ("Resta",          "-", resta),
    "3": ("Multiplicación", "×", multiplicacion),
    "4": ("División",       "÷", division),
}


def pausar(mensaje="Presioná Enter para continuar..."):
    input(f"\n{mensaje}")


def seleccionar_operacion():
    print("┌─────────────────────────────┐")
    print("│  ¿Qué operación querés hacer? │")
    print("├─────────────────────────────┤")
    for clave, (nombre, simbolo, _) in OPERACIONES.items():
        print(f"│  {clave}. {nombre:15} ({simbolo})    │")
    print("└─────────────────────────────┘")

    while True:
        opcion = input("\nIngresá el número de operación: ").strip()
        if opcion in OPERACIONES:
            return opcion
        print("  ⚠  Opción inválida. Ingresá 1, 2, 3 o 4.")


def pedir_numeros():
    print("\nIngresá exactamente dos números enteros separados por coma.")
    print("  Ejemplo: 8, 3   (presioná Enter para confirmar)")

    while True:
        entrada = input("\n  Números: ").strip()
        partes = [p.strip() for p in entrada.split(",")]

        if len(partes) != 2:
            print(f"  ⚠  Se esperaban 2 números, recibí {len(partes)}. Intentá de nuevo.")
            continue

        try:
            a, b = int(partes[0]), int(partes[1])
            return a, b
        except ValueError:
            print("  ⚠  Ambos valores deben ser números enteros (sin decimales). Intentá de nuevo.")


def pedir_segundo_numero():
    print("\nIngresá el segundo número entero.")
    print("  Ejemplo: 4   (presioná Enter para confirmar)")

    while True:
        entrada = input("\n  Segundo número: ").strip()
        try:
            return int(entrada)
        except ValueError:
            print("  ⚠  Debe ser un número entero. Intentá de nuevo.")


def ejecutar_operacion(opcion, a, b):
    nombre, simbolo, fn = OPERACIONES[opcion]
    try:
        resultado = fn(a, b)
        print(f"\n  ✔  {a} {simbolo} {b} = {resultado}")
        return resultado
    except ZeroDivisionError as e:
        print(f"\n  ✖  Error: {e}")
    except ValueError as e:
        print(f"\n  ✖  Error: {e}")
    except TypeError as e:
        print(f"\n  ✖  Error: {e}")
    return None


def preguntar_siguiente(resultado_anterior):
    print("\n¿Qué querés hacer ahora?")
    print("  1. Operar con números nuevos")
    if resultado_anterior is not None:
        print("  2. Usar el resultado anterior como primer número")
    print("  3. Salir de la calculadora")

    opciones_validas = {"1", "3"} | ({"2"} if resultado_anterior is not None else set())

    while True:
        opcion = input("\nIngresá una opción: ").strip()
        if opcion in opciones_validas:
            return opcion
        print("  ⚠  Opción inválida. Intentá de nuevo.")
