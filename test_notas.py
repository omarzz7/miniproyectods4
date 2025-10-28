import pytest
from notas import Nota, ManejadorDeNotas

@pytest.fixture
def manejador(tmp_path):
    db_file = tmp_path / "notasTestBD.db"
    m = ManejadorDeNotas(str(db_file))
    yield m

def test_crear_nota(manejador):
    nota = Nota(titulo="Prueba", contenido="Contenido de prueba")
    id_nueva = manejador.crear_nota(nota)
    assert id_nueva > 0

def test_leer_nota(manejador):
    nota = Nota(titulo="Lectura", contenido="Leer nota")
    id_nueva = manejador.crear_nota(nota)
    nota_leida = manejador.leer_nota(id_nueva)
    assert nota_leida.titulo == "Lectura"

def test_actualizar_nota(manejador):
    nota = Nota(titulo="Viejo", contenido="Texto viejo")
    id_nueva = manejador.crear_nota(nota)
    nota.id = id_nueva
    nota.titulo = "Nuevo"
    filas = manejador.actualizar_nota(nota)
    assert filas == 1
    nota_actualizada = manejador.leer_nota(id_nueva)
    assert nota_actualizada.titulo == "Nuevo"

def test_eliminar_nota(manejador):
    nota = Nota(titulo="Eliminar", contenido="Borrar esto")
    id_nueva = manejador.crear_nota(nota)
    filas = manejador.eliminar_nota(id_nueva)
    assert filas == 1
    assert manejador.leer_nota(id_nueva) is None
