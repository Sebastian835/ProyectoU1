from flask import Flask, render_template, request, redirect, url_for


# Inicializar la aplicacion
app = Flask(__name__, template_folder='templates')


# Ruta principal para el login
@app.route('/')
def home():
    return render_template('home.html')


# Ejecutar la aplicacion
if __name__ == '__main__':
    app.run(debug=True)