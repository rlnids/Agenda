'''LOGICA DEL PROGRAMA
Aquí están las funciones que trabajan con los datos:

agregar_contacto ➕

listar_contactos 📋

actualizar_contacto ✏️

eliminar_contacto 🗑️

exportar_csv 📤

👉 En esta parte no hablaremos con el usuario.
👉 Solo ejecutaremos operaciones.'''
#Nota importante: cada archivo se encarga de hacer un proceso. 
from database import conectar_base_de_datos #hacemos conexion con la base de datos para poder hacer las operaciones que pida el interfaz 

# ➕ Agregar contacto 
def agregar_contacto(nombre, telefono, email):#funcion para agregar contacto
    conexion = conectar_base_de_datos()#conexion con base de datos
    cursor = conexion.cursor()

    # 🧱 Insertamos datos usando parámetros seguros (?)
    cursor.execute(
        "INSERT INTO contactos (nombre, telefono, email) VALUES (?, ?, ?)",
        (nombre, telefono, email)  # 📦 Datos que sustituyen a los ?
    )#pedimos al cursor que inserte los datos en nuestra tabla contactos

    conexion.commit() # Guardar cambios
    cursor.close() 
    print('cursor cerrado')
    conexion.close() #Cerrar conexión
    print(f"✅ Contacto '{nombre}'correctamente 😎")


# 📋 Listar contactos 
def listar_contactos():#funcion para listar todos los contactos
    conexion = conectar_base_de_datos()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM contactos")  # 📋 Consulta SQL para ver todos los contactos
    contactos = cursor.fetchall()  # 📥 Obtenemos todos los registros con la nomenclatura el punto y la funcion fetchall (all=todos)

    cursor.close()
    conexion.close()
    return contactos #hacemos un return para que no se pierdan los datos


# ✏️ Actualizar contacto 
def actualizar_contacto(id_contacto, nombre, telefono, email): #funcion para actualizar contactos
    conexion = conectar_base_de_datos()
    cursor = conexion.cursor()

    # ✏️ Actualizamos datos usando parámetros seguros (?)
    cursor.execute(
        "UPDATE contactos SET nombre = ?, telefono = ?, email = ? WHERE id = ?",
        (nombre, telefono, email, id_contacto)#ejecutamos el comando update para actualizar 
    )

    conexion.commit()
    cursor.close()
    conexion.close()
    print("✏️ Contacto actualizado correctamente 😄")#hacemos un print para asegurarnos que el contacto se ha actualizado


# 🗑️ Eliminar contacto con parametros seguros (?)
def eliminar_contacto(id_contacto):#funcion para elimitar contacto
    conexion = conectar_base_de_datos()
    cursor = conexion.cursor()

    # 🗑️ Eliminamos usando parámetros seguros (?)
    cursor.execute(
        "DELETE FROM contactos WHERE id = ?",#
        (id_contacto,)  # ⚠️ coma obligatoria porque es una tupla
    )
    print(f"🗑️Contactos eliminados : {cursor.rowcount}")# hacemos un print y un cursor.rowcount  para saber el total de contactos que fueron eliminados de la base de datos
    conexion.commit()
    cursor.close()
    conexion.close()
    print("🗑️ Contacto eliminado correctamente 😈")#Un print para saber si hemos eliminado un contacto


# 📤 Exportar contactos a CSV (ejercicio extra)
def exportar_csv():  # función para exportar los datos a formato CSV
    import csv  # importamos el módulo csv, que proporciona funcionalidades para leer y escribir archivos CSV

    # Invocamos a la función listar_contactos() que retorna una lista de tuplas con los datos de los contactos
    contactos = listar_contactos()

    # Abrimos (o creamos si no existe) el archivo "contactos.csv" en modo escritura ("w")
    # - "newline=''" es importante para evitar líneas en blanco adicionales en algunos sistemas operativos
    # - "encoding='utf-8'" asegura que se manejen correctamente caracteres especiales (tildes, eñes, etc.)
    with open("contactos.csv", mode="w", newline="", encoding="utf-8") as archivo:
        # Creamos un objeto escritor CSV que nos permitirá escribir en el archivo
        writer = csv.writer(archivo)

        # 🏷️ Escribimos la cabecera del CSV, que son los nombres de las columnas
        writer.writerow(["ID", "Nombre", "Teléfono", "Email"])

        # 📋 Iteramos sobre cada contacto en la lista de contactos
        for contacto in contactos:
            # Escribimos una fila en el archivo CSV por cada contacto
            # Cada contacto 'c' es una tupla con los datos en el orden: (ID, Nombre, Teléfono, Email)
            writer.writerow(contacto)

    # Finalmente, mostramos un mensaje confirmando la exportación
    print("📁 Contactos exportados a contactos.csv 🚀")
#🔍 Buscar contacto por nombre
def buscar_contacto_por_nombre(nombre): #funcion para buscar por nombre
    conexion = conectar_base_de_datos()
    cursor = conexion.cursor()

    cursor.execute(
        '''SELECT * FROM contactos 
           WHERE nombre LIKE ? 
           ORDER BY nombre''',
        (f'%{nombre}%',) #ejecutamos el codigo para filtrar un contacto por %nombre% y lo ordenamos de manera ascendente.
    #lo que va entre el simbolo de porcentaje es lo que va buscar la funcion 
    )

    resultados = cursor.fetchall()# fetchall() recupera TODAS las filas que coinciden con la búsqueda
    conexion.close()

    # Mostrar resultados
    if resultados:
        print(f"\n✅ Contactos encontrados ({len(resultados)}):")
        for contacto in resultados:
            print(f"  👤 {contacto[1]} - 📞 {contacto[2]} - 📧 {contacto[3]}")
    else:
        print(f"🔍 No se encontraron contactos con '{nombre}'")

    return resultados #retorna la lista de contactos encontrados