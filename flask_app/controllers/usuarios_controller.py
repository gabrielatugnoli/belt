from flask import render_template, redirect, request, session, flash
from flask_app import app

from flask_app.models.usuarios import User
from flask_app.models.grados import Grado

#Importación de BCrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    #validamos la info que recibimos
    if not User.valida_usuario(request.form):
        return redirect('/')

    #guardamos registro
    pwd = bcrypt.generate_password_hash(request.form['password']) #encriptando la password del usuario y la guardamos en pwd

    #creamos un diccionario con todos los datos del request.form
    #creamos un neuvo diccionario porque request.form es un objeto (diccionario) inmutable y no se puede cambiar, daria error si quisieramos reemplazar la contrase;a original por la encriptada
    formulario = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": pwd
    }

    id = User.save(formulario) #recibimos el id del nuevo usuario

    session['usuario_id'] = id #guardamos en sesion el id del usuario

    return redirect('/home')

@app.route('/home')
def home():
    if 'usuario_id' not in session: #aqui restringo la posibilidad de entrar sin haber iniciado sesion
        return redirect('/')

    formulario = { "id": session['usuario_id']}

    usuario = User.get_by_id(formulario)

    grados = Grado.get_all()
    
    return render_template('home.html', usuario=usuario, grados=grados)

@app.route('/login', methods=['POST'])
def login():
    #verificamos que el email exista en la base de datos
    usuario = User.get_by_email(request.form) #recibimos una instancia de usuario o false

    if not usuario: #si user = false
        flash('Email no encontrado', 'login')
        return redirect('/')

    #user es una instancia
    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash('Password incorrecto', 'login')
        return redirect('/')

    session['usuario_id'] = usuario.id
    return redirect ('/home')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')