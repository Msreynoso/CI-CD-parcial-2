import pytest
from operaciones import suma, resta, multiplicacion, division


# ─── validar_entero (indirectamente via operaciones) ──────────────────────────

class TestValidarEntero:
    @pytest.mark.parametrize("fn", [suma, resta, multiplicacion, division])
    def test_lanza_type_error_si_primer_argumento_es_float(self, fn):
        with pytest.raises(TypeError, match="Solo se permiten números enteros"):
            fn(1.5, 2)

    @pytest.mark.parametrize("fn", [suma, resta, multiplicacion, division])
    def test_lanza_type_error_si_segundo_argumento_es_float(self, fn):
        with pytest.raises(TypeError, match="Solo se permiten números enteros"):
            fn(2, 1.5)

    @pytest.mark.parametrize("fn", [suma, resta, multiplicacion, division])
    def test_lanza_type_error_si_argumento_es_string(self, fn):
        with pytest.raises(TypeError, match="Solo se permiten números enteros"):
            fn("3", 2)

    @pytest.mark.parametrize("fn", [suma, resta, multiplicacion, division])
    def test_lanza_type_error_si_argumento_es_none(self, fn):
        with pytest.raises(TypeError, match="Solo se permiten números enteros"):
            fn(None, 2)


# ─── suma ──────────────────────────────────────────────────────────────────────

class TestSuma:
    def test_suma_positivos(self):
        assert suma(3, 4) == 7

    def test_suma_negativos(self):
        assert suma(-3, -4) == -7

    def test_suma_positivo_y_negativo(self):
        assert suma(10, -3) == 7

    def test_suma_con_cero(self):
        assert suma(5, 0) == 5

    def test_suma_ambos_cero(self):
        assert suma(0, 0) == 0


# ─── resta ─────────────────────────────────────────────────────────────────────

class TestResta:
    def test_resta_positivos(self):
        assert resta(10, 4) == 6

    def test_resta_resultado_negativo(self):
        assert resta(3, 10) == -7

    def test_resta_negativos(self):
        assert resta(-3, -4) == 1

    def test_resta_con_cero(self):
        assert resta(5, 0) == 5

    def test_resta_ambos_cero(self):
        assert resta(0, 0) == 0


# ─── multiplicacion ────────────────────────────────────────────────────────────

class TestMultiplicacion:
    def test_multiplicacion_positivos(self):
        assert multiplicacion(3, 4) == 12

    def test_multiplicacion_por_cero(self):
        assert multiplicacion(5, 0) == 0

    def test_multiplicacion_negativos(self):
        assert multiplicacion(-3, -4) == 12

    def test_multiplicacion_positivo_y_negativo(self):
        assert multiplicacion(3, -4) == -12

    def test_multiplicacion_por_uno(self):
        assert multiplicacion(7, 1) == 7


# ─── division ──────────────────────────────────────────────────────────────────

class TestDivision:
    def test_division_exacta(self):
        assert division(10, 2) == 5

    def test_division_resultado_uno(self):
        assert division(7, 7) == 1

    def test_division_negativos_resultado_positivo(self):
        assert division(-10, -2) == 5

    def test_division_positivo_entre_negativo(self):
        assert division(10, -2) == -5

    def test_lanza_zero_division_error(self):
        with pytest.raises(ZeroDivisionError, match="No se puede dividir por cero"):
            division(10, 0)

    def test_lanza_value_error_si_resultado_no_es_entero(self):
        with pytest.raises(ValueError, match="La división debe dar un entero"):
            division(10, 3)

    def test_lanza_value_error_con_negativos_no_exactos(self):
        with pytest.raises(ValueError, match="La división debe dar un entero"):
            division(-10, 3)
