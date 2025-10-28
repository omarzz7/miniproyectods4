from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crear_nota', methods=['GET', 'POST'])

def crear_nota():
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']

    return redirect(url_for('index'))
    return render_template('crear_nota.html')

if __name__ == '__main__':
    app.run(debug=True)
