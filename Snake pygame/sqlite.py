import sqlite3

def crear_bd_puntajes():
    with sqlite3.connect("tabla_puntajes.db") as conexion:
        try:
            sentencia = ''' CREATE TABLE Puntuacion
            (
            id integer primary key autoincrement,
            nombre text,
            puntaje integer
            )
            '''
            conexion.execute(sentencia)
            print("Se creo la tabla de puntajes")                       
        except sqlite3.OperationalError:
            print("La tabla de puntajes ya existe")

def insertar_puntajes(nombre:str, puntaje:int):
    with sqlite3.connect("tabla_puntajes.db") as conexion:    
        try:
            conexion.execute("INSERT INTO Puntuacion (nombre,puntaje) values (?,?)", (nombre, puntaje)) 
            conexion.commit()
        except:
            print("Error al escribir la tabla")

def lista_puntajes()->list:
    with sqlite3.connect("tabla_puntajes.db") as conexion:
        try:
            cursor = conexion.execute("SELECT * FROM Puntuacion ORDER BY puntaje desc")
            lista = cursor.fetchall()
        except:
            print("Error de registros")
            lista = []

        return lista