import pytest
from pathlib import Path

HTML = Path(__file__).parent.parent / "index.html"


@pytest.fixture
def contenido():
    return HTML.read_text(encoding="utf-8")


# ── Estructura básica ────────────────────────────────────────────────────────

def test_archivo_html_existe():
    assert HTML.exists(), "index.html no encontrado"

def test_tiene_doctype(contenido):
    assert contenido.strip().lower().startswith("<!doctype html>"), \
        "Falta el DOCTYPE"

def test_tiene_etiqueta_html(contenido):
    assert "<html" in contenido and "</html>" in contenido, \
        "Falta la etiqueta <html>"

def test_tiene_etiqueta_head(contenido):
    assert "<head>" in contenido and "</head>" in contenido, \
        "Falta la etiqueta <head>"

def test_tiene_etiqueta_body(contenido):
    assert "<body>" in contenido and "</body>" in contenido, \
        "Falta la etiqueta <body>"

def test_tiene_charset_utf8(contenido):
    assert 'charset="UTF-8"' in contenido or "charset='UTF-8'" in contenido, \
        "Falta meta charset UTF-8"

def test_tiene_titulo(contenido):
    assert "<title>" in contenido and "</title>" in contenido, \
        "Falta la etiqueta <title>"

def test_tiene_h1(contenido):
    assert "<h1>" in contenido and "</h1>" in contenido, \
        "Falta la etiqueta <h1>"

def test_h1_contiene_hola_mundo(contenido):
    inicio = contenido.index("<h1>") + len("<h1>")
    fin = contenido.index("</h1>")
    texto_h1 = contenido[inicio:fin]
    assert "Hola Mundo" in texto_h1 or "Hola mundo" in texto_h1, \
        "El <h1> no contiene 'Hola Mundo'"

