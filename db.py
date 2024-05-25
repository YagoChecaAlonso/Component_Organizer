# Description: Este archivo contiene las funciones necesarias para la creación de la base de datos y las tablas necesarias para el funcionamiento del sistema.
import sqlite3 as sql

# Crear la base de datos
conexion = sql.connect('db.sqlite3')
cursorBD = conexion.cursor()

def tablaExiste(mainTable):
    cursorBD.execute('''SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{}' '''.format(mainTable))
    if cursorBD.fetchone()[0]==1:#existe la tabla
        print("La tabla ya existe")
    else:
        cursorBD.execute('''CREATE TABLE Componentes (id INTEGER PRIMARY KEY, nombre TEXT, cantidad INTEGER, precio REAL, localizacion TEXT)''')
        print("Tabla creada")
    
    
    
tablaExiste('Componentes')    




#C Create

def insertarComponente(nombre, cantidad, precio, localizacion):
    cursorBD.execute('''INSERT INTO Componentes (nombre, cantidad, precio, localizacion) VALUES ('{}', {}, {}, '{}')'''.format(nombre, cantidad, precio, localizacion))
    conexion.commit()


#insertarComponente('Resistor', 100, 0.5, 'cajon de abajo')


#R Read

def SelectAll():
    cursorBD.execute('''SELECT * FROM Componentes''')
    lista = []
    for filaEncontrada in cursorBD.fetchall():
        lista.append(filaEncontrada)
    return lista

print(SelectAll())
def SelectSome():
    cursorBD.execute('''SELECT nombre, cantidad FROM Componentes''')
    print(cursorBD.fetchall())
SelectSome()    

#U Update
def actualizarComponente(id, diccionario):
    valoresvalidos=['Cantidad', 'Localizacion']
    for key in diccionario.keys():
        if key not in valoresvalidos:
            raise Exception('Esa columna no existe')
        else:
            query = '''UPDATE COMPONENTES SET {} = '{}' WHERE ID = {}'''.format(key, diccionario[key], id)
            cursorBD.execute(query)
    conexion.commit()
    
    
    
print("Antes de actualizar")
actualizarComponente(1, {'Cantidad': 300})
actualizarComponente(1, {'Localizacion': 'Cajon de abajo'})
actualizarComponente(1, {'Cantidad': 100, 'Localizacion': 'Cajon de arriba'})
print(SelectAll())


#D Delete
insertarComponente('Resistor', 100, 0.5, 'cajon de abajo')
#########################################
###CUIDADO CON ESTA FUNCION
#########################################

print(SelectAll())
def borrarComponente(id):
    cursorBD.execute('''DELETE FROM Componentes WHERE id = {}'''.format(id))
    conexion.commit()

borrarComponente(2)
print(SelectAll())



