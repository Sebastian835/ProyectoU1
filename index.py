from flask import Flask, render_template, request, redirect, url_for

# Inicializar la aplicacion
app = Flask(__name__, template_folder='templates')

usuarios_Registro = []                          #Array para los usuarios que se registren
pagoVuelos=[]                           #Array para los vuelos que hace el usuario

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
    if(request.method == "POST"):                               #valida que haya enviado datos por el metodo POST
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
MensajeContactanos = []                                             #Mensaje del usuario a la pagina
@app.route('/Contactanos', methods=['GET','POST'])
def Contactanos():
    if(request.method == "POST"):                   #valida que haya enviado datos por el metodo POST
        nombre = request.form['nombre']           
        correo = request.form['email']         
        telfono = request.form['phone']
        mensaje = request.form['message']
        if(nombre == "" or correo  == "" or telfono == "" or mensaje == ""):             #Si no hay datos no redirecciona
            return redirect(url_for('Contactanos'))
        else:
            MensajeContactanos.append(nombre)
            MensajeContactanos.append(correo)                   ##si hay datos los agrega al array MensajeContactos
            MensajeContactanos.append(telfono)
            MensajeContactanos.append(mensaje)
            print(MensajeContactanos)
            return redirect(url_for('Contactanos'))

    return render_template('Contactanos.html')

# Ruta para Argentina
VuelosARGENTINA=[]                                          #Guarda los vuelos realizados a argentina
@app.route('/Argentina', methods=['GET','POST'])
def Argentina():
    if(request.method == "POST"):                           #valida que haya enviado datos por el metodo POST
        nombre = request.form['nombre']           
        correo = request.form['email']         
        telfono = request.form['phone']
        fecha = request.form['fecha']
        hora = request.form['hora']
        if(nombre == "" or correo  == "" or telfono == "" or fecha == ""  or hora == ""):             #Si no hay datos no redirecciona
            return redirect(url_for('Argentina'))
        else:
            VuelosARGENTINA.append({'nombre': nombre, 'telefono': telfono, 'fecha': fecha, 'hora': hora} )       #guardado en el array de vuelosArgentina
            print(VuelosARGENTINA)
            return redirect(url_for('Pago'))
    return render_template('Argentina.html')


# Ruta para España
VuelosESPAÑA=[]                                          #Guarda los vuelos realizados a españa
@app.route('/España', methods=['GET','POST'])
def España():
    if(request.method == "POST"):                       #valida que haya enviado datos por el metodo POST
        nombre = request.form['nombre']           
        correo = request.form['email']         
        telfono = request.form['phone']
        fecha = request.form['fecha']
        hora = request.form['hora']
        if(nombre == "" or correo  == "" or telfono == "" or fecha == ""  or hora == ""):             #Si no hay datos no redirecciona
            return redirect(url_for('España'))
        else:
            VuelosESPAÑA.append({'nombre': nombre, 'telefono': telfono, 'fecha': fecha, 'hora': hora} )      #guardado en el array de vuelosEspaña
            print(VuelosESPAÑA)
            return redirect(url_for('Pago'))
    return render_template('España.html')


# Ruta para Egipto
VuelosEGIPTO=[]                                          #Guarda los vuelos realizados a egipto
@app.route('/Egipto', methods=['GET','POST'])
def Egipto():
    if(request.method == "POST"):                       #valida que haya enviado datos por el metodo POST
        nombre = request.form['nombre']           
        correo = request.form['email']         
        telfono = request.form['phone']
        fecha = request.form['fecha']
        hora = request.form['hora']
        if(nombre == "" or correo  == "" or telfono == "" or fecha == ""  or hora == ""):             #Si no hay datos no redirecciona
            return redirect(url_for('Egipto'))
        else:
            VuelosEGIPTO.append({'nombre': nombre, 'telefono': telfono, 'fecha': fecha, 'hora': hora} )          #guardado en el array de vuelosEgipto
            print(VuelosEGIPTO)
            return redirect(url_for('Pago'))
    return render_template('Egipto.html')


# Ruta para Turquia
VuelosTurquia=[]                                          #Guarda los vuelos realizados a turqia
@app.route('/Turquia' , methods=['GET','POST'])
def Turquia():
    if(request.method == "POST"):                   #valida que haya enviado datos por el metodo POST
        nombre = request.form['nombre']           
        correo = request.form['email']         
        telfono = request.form['phone']
        fecha = request.form['fecha']
        hora = request.form['hora']
        if(nombre == "" or correo  == "" or telfono == "" or fecha == ""  or hora == ""):             #Si no hay datos no redirecciona
            return redirect(url_for('Turquia'))
        else:
            VuelosTurquia.append({'nombre': nombre, 'telefono': telfono, 'fecha': fecha, 'hora': hora} )        #guardado en el array de vuelosTurquia
            print(VuelosTurquia)
            return redirect(url_for('Pago'))
    return render_template('Turquia.html')


# Ruta para Francia
VuelosFrancia=[]                                          #Guarda los vuelos realizados a francia
@app.route('/Francia', methods=['GET','POST'])
def Francia():
    if(request.method == "POST"):                               #valida que haya enviado datos por el metodo POST
        nombre = request.form['nombre']           
        correo = request.form['email']         
        telfono = request.form['phone']
        fecha = request.form['fecha']
        hora = request.form['hora']
        if(nombre == "" or correo  == "" or telfono == "" or fecha == ""  or hora == ""):             #Si no hay datos no redirecciona
            return redirect(url_for('Francia'))
        else:
            VuelosFrancia.append({'nombre': nombre, 'telefono': telfono, 'fecha': fecha, 'hora': hora} )  #guardado en el array de vuelosFrancia
            print(VuelosFrancia)
            return redirect(url_for('Pago'))
    return render_template('Francia.html')


# Ruta para Mexico
VuelosMexico=[]                                          #Guarda los vuelos realizados a mexico
@app.route('/Mexico', methods=['GET','POST'])
def Mexico():
    if(request.method == "POST"):                   #valida que haya enviado datos por el metodo POST
        nombre = request.form['nombre']           
        correo = request.form['email']         
        telfono = request.form['phone']
        fecha = request.form['fecha']
        hora = request.form['hora']
        if(nombre == "" or correo  == "" or telfono == "" or fecha == ""  or hora == ""):             #Si no hay datos no redirecciona
            return redirect(url_for('Mexico'))
        else:
            VuelosMexico.append({'nombre': nombre, 'telefono': telfono, 'fecha': fecha, 'hora': hora} )  #guardado en el array de vuelosMexico
            print(VuelosMexico)
            return redirect(url_for('Pago'))
    return render_template('Mexico.html')



# Ruta para Pago
pago=[]                         #guarda los datos de la tarjeta del pago
@app.route('/Pago', methods=['GET','POST'])
def Pago():
    if(request.method == "POST"):               #valida que haya enviado datos por el metodo POST
        numeroTarjeta = request.form['numeroTarjeta']           
        mesVencimiento = request.form['mesVence']         
        yearVencimiento = request.form['añoVence']
        ccv = request.form['ccv']
        dueñoTarjeta = request.form['dueñoTarjeta']
        if(numeroTarjeta == "" or mesVencimiento  == "" or yearVencimiento == "" or ccv == ""  or dueñoTarjeta == ""):             #Si no hay datos no redirecciona
            return redirect(url_for('Vuelos'))
        else:
            pago.append({'NumeroTarjeta': numeroTarjeta, 'ccv': ccv, 'DueñoTarjeta': dueñoTarjeta} )        #guardado en el array de pago
            print(pago)
            return redirect(url_for('VuelosRealizados'))

    return render_template('pago.html')

# Ruta para Pago
@app.route('/VuelosRealizados')
def VuelosRealizados():                                         #Envia cada uno de los arreglos donde se encuentran los vuelos realizados
    return render_template('VuelosRealizados.html', VuelosRealizadosM = VuelosMexico, VuelosRealizadosF = VuelosFrancia
        , VuelosRealizadosT = VuelosTurquia, VuelosRealizadosEs = VuelosESPAÑA, VuelosRealizadosEg = VuelosEGIPTO
        , VuelosRealizadosA = VuelosARGENTINA)              #Se les asigna otra variable para pasar los arrays



if __name__ == '__main__':
    app.run(debug=True) # Ejecutar la aplicacion