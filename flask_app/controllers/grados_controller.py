from flask import render_template, redirect, request, session, flash
from flask_app import app

from flask_app.models.usuarios import User
from flask_app.models.grados import Grado

@app.route('/new/grade')
def new_grade():
    if 'usuario_id' not in session:
        return redirect('/')

    formulario = { "id": session['usuario_id']}

    usuario = User.get_by_id(formulario)

    return render_template('new_grade.html', usuario = usuario)

@app.route('/create/grade', methods=['POST'])
def create_grade():
    if 'usuario_id' not in session:
        return redirect('/')

    if not Grado.valida(request.form):
        return redirect('/new/grade')

    Grado.save(request.form)

    return redirect('/home')

@app.route('/edit/grade/<int:id>')
def edit_grade(id):
    if 'usuario_id' not in session:
        return redirect('/')

    formulario = { "id": session['usuario_id']}

    usuario = User.get_by_id(formulario)

    formulario_calificacion = {"id": id}
    grado = Grado.get_id(formulario_calificacion)

    return render_template('edit_grade.html',usuario=usuario, grado=grado)

@app.route('/update/grade', methods=['POST'])
def update_grade():
    if 'usuario_id' not in session:
        return redirect('/')
    
    #Validación de Calificación
    if not Grado.valida(request.form):
        return redirect('/edit/grade/'+request.form['id']) #/edit/grade/1
    
    Grado.update(request.form)

    return redirect('/home')

@app.route('/delete/grade/<int:id>')
def delete_grade(id):
    if 'usuario_id' not in session:
        return redirect('/')

    formulario = {"id": id}
    Grado.delete(formulario)

    return redirect('/home')