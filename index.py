from flask import Flask, render_template, request, redirect, url_for


# Inicializar la aplicacion
app = Flask(__name__, template_folder='templates')

usuarios_Registro = []

# Ruta principal 
@app.route('/')
def home():
    return render_template('home.html')

# Ruta para el login
@app.route('/Login', methods=['GET','POST'])
def Login():
    return render_template('Login.html')

# Ruta para el registro
@app.route('/Registro' , methods=['GET','POST'])
def Registro():
    if(request.method == "POST"):
        nombre = request.form['name']
        correo = request.form['email']
        contrase = request.form['password']

        if(nombre == "" or correo  == "" or contrase == ""):
            return redirect(url_for('Registro'))
        else:
            usuarios_Registro.append({'nombre': nombre, 'email': correo, 'password': contrase})
            print(usuarios_Registro)
            return redirect(url_for('Login'))
    return render_template('Registro.html')


# Ejecutar la aplicacion
if __name__ == '__main__':
    app.run(debug=True)