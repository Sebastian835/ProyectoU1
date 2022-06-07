from csv import excel_tab
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
    #Obtiene los datos del pagina Login por medio del metodo POST
    if(request.method == "POST"):
        correo = request.form['email']          #obtencion de correo
        contrase = request.form['password']         #obtencion de contraseña


        #try para evaluar si un correo no se encuentra en la lista
        try:
            if (usuarios_Registro.index(correo) > 0):               #obtener el indice del correo
                posicionCorreo = usuarios_Registro.index(correo)
                if(usuarios_Registro[posicionCorreo] == correo and usuarios_Registro[posicionCorreo+1] == contrase):        #compara los datos ingresados con el registro
                    return redirect(url_for('Vuelos'))              #envia a la pagina Vuelos
                else:
                    return redirect(url_for('Login'))
        except:
            return redirect(url_for('Login'))

    return render_template('Login.html')


# Ruta para el registro
@app.route('/Registro' , methods=['GET','POST'])
def Registro():
     #Obtiene los datos del pagina Login por medio del metodo POST
    if(request.method == "POST"):
        nombre = request.form['name']           #Registro datos usuario
        correo = request.form['email']         
        contrase = request.form['password']
        if(nombre == "" or correo  == "" or contrase == ""):             #Si no hay datos no redirecciona
            return redirect(url_for('Registro'))
        else:
            #Ingresa datos en el array del Usuario
            usuarios_Registro.append(nombre)
            usuarios_Registro.append(correo)
            usuarios_Registro.append(contrase)
            return redirect(url_for('Login'))
    return render_template('Registro.html')


@app.route('/Vuelos')
def Vuelos():
    
    return render_template('Vuelos.html')


# Ejecutar la aplicacion
if __name__ == '__main__':
    app.run(debug=True)