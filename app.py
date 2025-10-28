from flask import Flask, render_template, request, redirect, url_for, flash
from notas import Nota, ManejadorDeNotas
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'una_clave_secreta_fuerte')
manejador_notas = ManejadorDeNotas()

INTEGRANTES = [
    "Omar Corral Castro",
    "Miguel Pablo Franco Cruz",
    "Pablo Ivan Durazo Irigoyen",
]

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html', team_members=INTEGRANTES)

@app.route('/crear_nota', methods=['GET', 'POST'])
def crear_nota():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        contenido = request.form.get('contenido')

        if not titulo or not contenido:
            flash('El titulo y el contenido son obligatorios', 'error')
            return redirect(url_for('crear_nota'))

        nueva_nota = Nota(titulo=titulo, contenido=contenido)
        manejador_notas.crear_nota(nueva_nota)

        flash('Nota creada con exito', 'success')
        return redirect(url_for('listar_notas'))

    return render_template('crear_nota.html')

@app.route('/listar_notas')
def listar_notas():
    notas = manejador_notas.leer_notas()

    return render_template('listar_notas.html', notas=notas)

@app.route('/modificar_nota/<int:id>', methods=['GET', 'POST'])
def modificar_nota(id):
    nota_actual = manejador_notas.leer_nota(id)

    if not nota_actual:
        flash(f'La nota con ID {id} no fue encontrada.', 'error')
        return redirect(url_for('listar_notas'))

    if request.method == 'POST':

        nuevo_titulo = request.form.get('titulo')
        nuevo_contenido = request.form.get('contenido')

        if not nuevo_titulo or not nuevo_contenido:
            flash('El título y el contenido son obligatorios.', 'error')

            return redirect(url_for('modificar_nota', id=id))

        nota_actual.titulo = nuevo_titulo
        nota_actual.contenido = nuevo_contenido
        manejador_notas.actualizar_nota(nota_actual)

        flash('Nota modificada exitosamente.', 'success')
        return redirect(url_for('listar_notas'))


    return render_template('modificar_nota.html', nota=nota_actual)

@app.route('/eliminar_nota/<int:id>')
def eliminar_nota(id):

    nota_a_eliminar = manejador_notas.leer_nota(id)
    if not nota_a_eliminar:
        flash(f'La nota con ID {id} no fue encontrada.', 'error')
    else:

        manejador_notas.eliminar_nota(id)
        flash(f'Nota "{nota_a_eliminar.titulo}" eliminada exitosamente.', 'success')

    return redirect(url_for('listar_notas'))

if __name__ == '__main__':
    app.run(debug=True)
#app.py