from flask import Flask, render_template, request, redirect, url_for                    #LIBRERIAS

# Inicializar la aplicacion
app = Flask(__name__, template_folder='templates')

usuarios_Registro = []                          #Array para los usuarios que se registren
pagoVuelos=[]                           #Array para los vuelos que hace el usuario


@app.route('/')         # Ruta principal 
def home():
    return render_template('home.html')



@app.route('/Login', methods=['GET','POST'])            # Ruta para el login
def Login():
    #Obtiene los datos del pagina Login por medio del metodo POST
    if(request.method == "POST"):
        correo = request.form['email']          #obtencion de correo
        contrase = request.form['password']         #obtencion de contraseña


        #try para evaluar si un correo no se encuentra en la lista
        try:
            if (usuarios_Registro.index(correo) > 0):               #obtener el indice del correo
                posicionCorreo = usuarios_Registro.index(correo)
                print(usuarios_Registro)
                print(posicionCorreo)
                if(usuarios_Registro[posicionCorreo] == correo and usuarios_Registro[posicionCorreo+1] == contrase):        #compara los datos ingresados con el registro
                    return redirect(url_for('Vuelos'))              #envia a la pagina Vuelos
                else:
                    return redirect(url_for('Login'))
        except:
            return redirect(url_for('Login'))

    return render_template('Login.html')


@app.route('/Registro' , methods=['GET','POST'])                    # Ruta para el registro    
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


@app.route('/Vuelos')           # Ruta para vuelos
def Vuelos():
    return render_template('Vuelos.html')


@app.route('/PreguntasFrecuentes')              # Ruta para preguntas
def Preguntitas():
    return render_template('PreguntasF.html')


MensajeContactanos = []                                             
@app.route('/Contactanos', methods=['GET','POST'])          # Ruta para contactanos
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


VuelosARGENTINA=[]                                          #Guarda los vuelos realizados a argentina
@app.route('/Argentina', methods=['GET','POST'])                # Ruta para Argentina
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

@app.route('/borrarArgentina', methods=['POST']) 
def borrarArgentina():
    if request.method == 'POST':
      VuelosARGENTINA.clear()
      return redirect(url_for('VuelosRealizados'))   



VuelosESPAÑA=[]                                          #Guarda los vuelos realizados a españa
@app.route('/España', methods=['GET','POST'])               # Ruta para España
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

@app.route('/borrarEspaña', methods=['POST']) 
def borrarEspaña():
    if request.method == 'POST':
      VuelosESPAÑA.clear()
      return redirect(url_for('VuelosRealizados'))   


  
VuelosEGIPTO=[]                                          #Guarda los vuelos realizados a egipto
@app.route('/Egipto', methods=['GET','POST'])             # Ruta para Egipto
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

@app.route('/borrarEgipto', methods=['POST']) 
def borrarEgipto():
    if request.method == 'POST':
      VuelosEGIPTO.clear()
      return redirect(url_for('VuelosRealizados'))   



VuelosTurquia=[]                                          #Guarda los vuelos realizados a turqia
@app.route('/Turquia' , methods=['GET','POST'])             # Ruta para Turquia
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

@app.route('/borrarTurquia', methods=['POST']) 
def borrarTurquia():
    if request.method == 'POST':
      VuelosTurquia.clear()
      return redirect(url_for('VuelosRealizados'))   


VuelosFrancia=[]                                          #Guarda los vuelos realizados a francia
@app.route('/Francia', methods=['GET','POST'])                      # Ruta para Francia
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

@app.route('/borrarFrancia', methods=['POST']) 
def borrarFrancia():
    if request.method == 'POST':
      VuelosFrancia.clear()
      return redirect(url_for('VuelosRealizados'))   


VuelosMexico=[]                                          #Guarda los vuelos realizados a mexico
@app.route('/Mexico', methods=['GET','POST'])       # Ruta para Mexico
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

@app.route('/borrarMexico', methods=['POST']) 
def borrarMexico():
    if request.method == 'POST':
      VuelosMexico.clear()
      return redirect(url_for('VuelosRealizados'))   



pago=[]                         #guarda los datos de la tarjeta del pago
@app.route('/Pago', methods=['GET','POST'])         # Ruta para Pago
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


@app.route('/VuelosRealizados' )        # Ruta para Vuelos Realizados
def VuelosRealizados():     
    #Envia cada uno de los arreglos donde se encuentran los vuelos realizados
    return render_template('VuelosRealizados.html', VuelosRealizadosM = VuelosMexico, VuelosRealizadosF = VuelosFrancia
        , VuelosRealizadosT = VuelosTurquia, VuelosRealizadosEs = VuelosESPAÑA, VuelosRealizadosEg = VuelosEGIPTO
        , VuelosRealizadosA = VuelosARGENTINA)              #Se les asigna otra variable para pasar los arrays




if __name__ == '__main__':
    app.run(debug=True) # Ejecuta la aplicacion