import pytest
import re
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


# ── Etiquetas bien formadas ──────────────────────────────────────────────────

def test_etiquetas_con_apertura_correcta(contenido):
    """
    Detecta etiquetas con '<' pero sin '>' de cierre antes del contenido.
    Ejemplo inválido: <h1otro titulo</h1>
    Ejemplo válido:   <h1>otro titulo</h1>
    """
    mal_formadas = re.findall(r'<[^>]*(?:<|$)', contenido)
    mal_formadas = [
        tag for tag in mal_formadas
        if not tag.strip().startswith("<!--")
        and not tag.strip().lower().startswith("<!doctype")
    ]
    assert not mal_formadas, \
        f"Etiquetas con apertura mal formada (falta el '>'): {mal_formadas}"


def test_etiquetas_tienen_apertura_y_cierre(contenido):
    """
    Para cada etiqueta de cierre encontrada (</tag>),
    verifica que exista su correspondiente etiqueta de apertura (<tag> o <tag ...>).
    Ejemplo inválido: <h1otro titulo</h1>  → existe </h1> pero no <h1>
    """
    etiquetas_cierre = re.findall(r'</(\w+)>', contenido)
    for tag in etiquetas_cierre:
        apertura = re.search(rf'<{tag}[\s>]', contenido)
        assert apertura, \
            f"Se encontró '</{tag}>' pero falta su etiqueta de apertura '<{tag}>'"
