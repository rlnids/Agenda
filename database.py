''' Manejo de la base de datos
En esta parte del proyecto trabajaremos dos funciones simples:
-conectar la base de datos 
-crear base de datos
Ademas crearemos la tabla
Es importante recordar que este archivo se encarga de gestionar la conexión con SQLite y crear las tablas.
No contiene lógica del programa ni interacción con el usuario.
'''
#primero importamos Sqlite3
import sqlite3
#funcion para conectar la base de datos, ademas con esta la invocaremos 
def conectar_base_de_datos():
    # Si no existe la base de datos, SQLite la crea automáticamente 
    conexion = sqlite3.connect("agenda.db")
    print('Conexión establecida exitosasmente') #hago un print para que en el terminal me asegure de que todo esta yendo como debe
    return conexion #Devuelve la conexión a la base de datos para que pueda usarse fuera de la función

#hago un print, para poder ver la versión de Sqlite que trabajamos
print(f'Version de SQLITE : {sqlite3.sqlite_version}')

print(f'\n*******************************************')
print(f'CONEXION Y CREACION DE LA BASE DE DATOS')
print('*******************************************')

#🧱Función para crear la tabla de contactos y poder invocarla
def crear_tabla():
    conexion = sqlite3.connect('agenda.db')
    print('¡Conexión establecida exitosasmente!') #hago un print para que en el terminal me asegure de que todo esta yendo como debe
    cursor = conexion.cursor() #se crea la variable cursor para el alojamiento del modulo cursor, nos sirve para señalar ejecutar y manipular datos, en este caso de la base de datos
    print("Cursor creado correctamente")#hago un print para que en el terminal me asegure de que todo esta yendo como debe

    #🧱Creamos la tabla si no existe y aplicamos los tipos de datos, tanto a la tabla como a las columnas🧱
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT
        )
    ''')#Le decimos que ejecute nuestra orden 'crear tabla'.
    varios_contactos = [ #variable para hacer una lista de contactos para añadir, que se convierte en una tupla separada por las comas la lista es vertical y la tupla horizontal
    ("Juan Pérez", "600123456", "juan@gmail.com"),
    ("Ana López", "611987654", "ana@gmail.com"),
    ("Carlos Ruiz", "622555444", "carlos@gmail.com")
    ]       
    cursor.executemany('INSERT INTO contactos (nombre, telefono, email) Values (?,?,?)', varios_contactos)#añadimos los contactos con valores seguros para evitar filtraciones
    print("\n*****************")
    print("CONTACTOS DE LA BIBLIOTECA")
    print('tabla "contactos" Creada') #hago un print para asegurarme de que la tabla esta creada
    print('CONTACTOS AGREGADOS!')
    conexion.commit()  # Guardar cambios
    print('CAMBIOS GUARDADOS') #hago un print para comprobar que los datos esten guardados
    conexion.close()   # Cerrar conexión. ES IMPORTANTE RECORDAR QUE SIEMPRE ASEGURARNOS QUE CERRAMOS LA CONEXION 
    print('CONEXION CERRADA') #hago un print para comprobar que la conexión este cerrada
