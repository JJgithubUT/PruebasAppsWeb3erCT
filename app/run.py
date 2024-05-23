#Activar Entorno Virtual  <---->  .venv\Scripts\activate
#Correr Aplicación  ----------------------------------  python app\run.py run
#Correr App alternativa  -----------------------------  flask -app app\run.py run
#Inspeccionar con: ----------------  pip list

from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about-us")
def about_us():
    return render_template('about_us.html')

@app.route("/layout")
def layout():
    return render_template('layout.html')

@app.route('/dashboard')
def dashboard():
    return render_template('/dashboard.html')

def pagina_no_encontrada(error):
    #return redirect(url_for('index'))
    return render_template('404.html')


if __name__ == '__main__':
    # Primero ENCONTRAR ERRORES y luego correr la página
    app.register_error_handler(404, pagina_no_encontrada)

    # Primero encontrar errores y luego CORRER LA PÁGINA
    app.run(debug=True, port=1946)