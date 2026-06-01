import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from interfaz import (
    OPERACIONES,
    pausar,
    seleccionar_operacion,
    pedir_numeros,
    pedir_segundo_numero,
    ejecutar_operacion,
    preguntar_siguiente,
)


def main():
    print("=" * 45)
    print("        CALCULADORA DE ENTEROS")
    print("  Operaciones: suma, resta, multiplicación")
    print("  y división exacta entre números enteros.")
    print("=" * 45)
    pausar("Presioná Enter para empezar...")

    resultado_anterior = None

    while True:
        print()
        opcion_op = seleccionar_operacion()
        nombre_op, simbolo_op, _ = OPERACIONES[opcion_op]

        print(f"\n  Operación seleccionada: {nombre_op} ({simbolo_op})")
        pausar()

        if resultado_anterior is not None:
            print(f"\nEl resultado anterior fue {resultado_anterior}.")
            print("Ya está cargado como primer número.")
            pausar()
            b = pedir_segundo_numero()
            a = resultado_anterior
            resultado_anterior = None
        else:
            a, b = pedir_numeros()

        pausar()

        resultado = ejecutar_operacion(opcion_op, a, b)
        pausar()

        siguiente = preguntar_siguiente(resultado)

        if siguiente == "3":
            print("\n¡Hasta luego! 👋")
            break
        elif siguiente == "2":
            resultado_anterior = resultado
        # si es "1", resultado_anterior queda en None → pide números nuevos


if __name__ == "__main__":
    main()
