from flask import Flask, render_template, request, redirect, url_for

# Inicializar la aplicacion
app = Flask(__name__, template_folder='templates')

usuarios_Registro = []
pagoVuelos=[]

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

# Ruta para vuelos
@app.route('/Vuelos')
def Vuelos():
    return render_template('Vuelos.html')

# Ruta para preguntas
@app.route('/PreguntasFrecuentes')
def Preguntitas():
    return render_template('PreguntasF.html')

# Ruta para contactanos
MensajeContactanos = []
@app.route('/Contactanos', methods=['GET','POST'])
def Contactanos():
    if(request.method == "POST"):
        nombre = request.form['nombre']           
        correo = request.form['email']         
        telfono = request.form['phone']
        mensaje = request.form['message']
        if(nombre == "" or correo  == "" or telfono == "" or mensaje == ""):             #Si no hay datos no redirecciona
            return redirect(url_for('Contactanos'))
        else:
            MensajeContactanos.append(nombre)
            MensajeContactanos.append(correo)
            MensajeContactanos.append(telfono)
            MensajeContactanos.append(mensaje)
            print(MensajeContactanos)
            return redirect(url_for('Contactanos'))

    return render_template('Contactanos.html')

# Ruta para Argentina
VuelosARGENTINA=[]
@app.route('/Argentina', methods=['GET','POST'])
def Argentina():
    if(request.method == "POST"):
        nombre = request.form['nombre']           
        correo = request.form['email']         
        telfono = request.form['phone']
        fecha = request.form['fecha']
        hora = request.form['hora']
        if(nombre == "" or correo  == "" or telfono == "" or fecha == ""  or hora == ""):             #Si no hay datos no redirecciona
            return redirect(url_for('Argentina'))
        else:
            VuelosARGENTINA.append(nombre)
            VuelosARGENTINA.append(correo)
            VuelosARGENTINA.append(telfono)
            VuelosARGENTINA.append(fecha)
            VuelosARGENTINA.append(hora)
            print(VuelosARGENTINA)
            return redirect(url_for('Pago'))
    return render_template('Argentina.html')


# Ruta para España
VuelosESPAÑA=[]
@app.route('/España', methods=['GET','POST'])
def España():
    if(request.method == "POST"):
        nombre = request.form['nombre']           
        correo = request.form['email']         
        telfono = request.form['phone']
        fecha = request.form['fecha']
        hora = request.form['hora']
        if(nombre == "" or correo  == "" or telfono == "" or fecha == ""  or hora == ""):             #Si no hay datos no redirecciona
            return redirect(url_for('España'))
        else:
            VuelosESPAÑA.append(nombre)
            VuelosESPAÑA.append(correo)
            VuelosESPAÑA.append(telfono)
            VuelosESPAÑA.append(fecha)
            VuelosESPAÑA.append(hora)
            print(VuelosESPAÑA)
            return redirect(url_for('Pago'))
    return render_template('España.html')


# Ruta para Egipto
VuelosEGIPTO=[]
@app.route('/Egipto', methods=['GET','POST'])
def Egipto():
    if(request.method == "POST"):
        nombre = request.form['nombre']           
        correo = request.form['email']         
        telfono = request.form['phone']
        fecha = request.form['fecha']
        hora = request.form['hora']
        if(nombre == "" or correo  == "" or telfono == "" or fecha == ""  or hora == ""):             #Si no hay datos no redirecciona
            return redirect(url_for('Egipto'))
        else:
            VuelosEGIPTO.append(nombre)
            VuelosEGIPTO.append(correo)
            VuelosEGIPTO.append(telfono)
            VuelosEGIPTO.append(fecha)
            VuelosEGIPTO.append(hora)
            print(VuelosEGIPTO)
            return redirect(url_for('Pago'))
    return render_template('Egipto.html')

# Ruta para Pago
@app.route('/Pago')
def Pago():
    return render_template('pago.html')


# Ejecutar la aplicacion
if __name__ == '__main__':
    app.run(debug=True)