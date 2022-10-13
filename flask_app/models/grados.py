from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
import re
from datetime import datetime

class Grado:
    def __init__(self, data):
        self.id = data['id']
        self.alumno = data['alumno']
        self.stack = data['stack']
        self.fecha = data['fecha']
        self.calificacion = data['calificacion']
        self.cinturon = data['cinturon']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuario_id = data['usuario_id']

    @staticmethod
    def valida(formulario):
        es_valido = True

        if formulario['alumno'] == '':
            flash('Alumno no puede estar vacío', 'grades')
            es_valido = False

        if formulario['calificacion']== '':
            flash('Ingresa calificación','grades')
            es_valido = False
        else:
            if int(formulario['calificacion']) < 1 or int(formulario['calificacion']) > 10:
                flash('Calificación debe ser entre 1 y 10', 'grades')
                es_valido = False
            
        if formulario['fecha'] == '':
            flash('Ingrese una fecha', 'grades')
            es_valido = False
        else:
            fecha_obj = datetime.strptime(formulario['fecha'], '%Y-%m-%d') #Estamos transformando un texto a formato de fecha
            hoy = datetime.now() #Me da la fecha de hoy
            if hoy < fecha_obj:
                flash('La fecha debe ser en pasado', 'grades')
                es_valido = False


        return es_valido

    @classmethod
    def save(cls,formulario):
        query = "INSERT INTO grados (alumno, stack, fecha, calificacion, cinturon, usuario_id) VALUES (%(alumno)s,%(stack)s,%(fecha)s,%(calificacion)s,%(cinturon)s,%(usuario_id)s)"
        result = connectToMySQL('belt').query_db(query,formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM grados"
        results = connectToMySQL('belt').query_db(query)
        grados = []

        for grado in results:
            grados.append(cls(grado))
        
        return grados

    @classmethod
    def get_id(cls,formulario):
        query = "SELECT * FROM grados WHERE id = %(id)s"
        result = connectToMySQL('belt').query_db(query, formulario)

        grado = cls(result[0])
        return grado

    @classmethod
    def update(cls, formulario):
        query = "UPDATE grados SET alumno=%(alumno)s, stack=%(stack)s, fecha=%(fecha)s, calificacion=%(calificacion)s, cinturon=%(cinturon)s, usuario_id=%(usuario_id)s WHERE id=%(id)s"
        result = connectToMySQL('belt').query_db(query, formulario)
        return result
    

    @classmethod
    def delete(cls, formulario):
        query = "DELETE FROM grados WHERE id = %(id)s"
        result = connectToMySQL('belt').query_db(query, formulario)
        return result
