def validar_entero(numero):
    if not isinstance(numero, int):
        raise TypeError("Solo se permiten números enteros")
