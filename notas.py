import sqlite3
import os

class Nota:
    def __init__(self, id=None, titulo="", contenido=""):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido


class ManejadorDeNotas:
    def __init__(self, db_name="notasBD.db"):
        self.db_name = db_name
        self._crear_tabla()

    def _conectar(self):
        return sqlite3.connect(self.db_name)

    def _crear_tabla(self):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    contenido TEXT NOT NULL
                )
            """)
            conn.commit()

    # En este espacio se crea la nota
    def crear_nota(self, nota: Nota):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO notas (titulo, contenido) VALUES (?, ?)",
                           (nota.titulo, nota.contenido))
            conn.commit()
            return cursor.lastrowid

    # Aqui lee todas las notas
    def leer_notas(self):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, titulo, contenido FROM notas")
            filas = cursor.fetchall()
            return [Nota(id=f[0], titulo=f[1], contenido=f[2]) for f in filas]

    # Y en este solo las de un ID
    def leer_nota(self, id):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, titulo, contenido FROM notas WHERE id = ?", (id,))
            fila = cursor.fetchone()
            if fila:
                return Nota(id=fila[0], titulo=fila[1], contenido=fila[2])
            return None

    # Aqui se actualiza
    def actualizar_nota(self, nota: Nota):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE notas SET titulo = ?, contenido = ? WHERE id = ?",
                           (nota.titulo, nota.contenido, nota.id))
            conn.commit()
            return cursor.rowcount

    # Y aqui se eliminan
    def eliminar_nota(self, id):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM notas WHERE id = ?", (id,))
            conn.commit()
            return cursor.rowcount
