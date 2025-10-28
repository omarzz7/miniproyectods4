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

if __name__ == '__main__':
    app.run(debug=True)
