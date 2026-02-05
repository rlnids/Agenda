'''
INTERFAZ DE USUARIO
Importaremos todas las funciones de operaciones para poder interactuar con el usuario.
'''
#importamos todas las funciones de operaciones.py para manejar la interaccion con la base de datos.CRUD (Crear, Leer, Actualizar, Eliminar, Buscar)
from operaciones import (
    agregar_contacto,
    listar_contactos,
    actualizar_contacto,
    eliminar_contacto,
    exportar_csv,
    buscar_contacto_por_nombre
)
import re #re = Módulo de Expresiones Regulares,es una herramienta para buscar patrones en texto ideal para correos electronicos 

# 📧 Validar email, usando expreciones regulares(regex)
def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'# 🔍 Patrón regex para emails
    return re.match(patron, email)#Retorna el resultado de la comparación

# 🧾 Mostrar menú
def mostrar_menu():#menu principal 
    print('\n' + '✨' * 25)
    #opciones del menu
    print('       📒 AGENDA DE CONTACTOS 📒')
    print('✨' * 25)
    print('1️⃣  📝 Agregar contacto')
    print('2️⃣  👁️  Listar contactos')
    print('3️⃣  ✏️  Actualizar contacto')
    print('4️⃣  🗑️  Eliminar contacto')#ejercicio
    print('5️⃣  📤 Exportar a CSV')#ejercicio
    print('6️⃣  🔍 Buscar contacto')
    print('-' * 45)
    print('0️⃣  🚪 Salir')# Opción para salir del programa
    print('✨' * 25)



# 🧑‍💻 Interacción con el usuario
def ejecutar_menu():# Esta función despliega todas las opciones disponibles en la agenda
    while True:#utilizaremos un bucle while true, para que gire constantemente hasta que el usuario quiera salir
        mostrar_menu()#mostrar menu en cada interacción
        opcion = input('👉 Elige una opción: ').strip()#el .strip para eliminar los espacios en blanco 
        
        #Opcion agregar contacto
        if opcion == '1':
            print('\n' + '📝' * 30)
            print('   AGREGAR NUEVO CONTACTO')
            print('📝' * 30)
            #cogeremos los datos del usuario
            nombre = input('👤 Nombre: ').strip()#el input para que el programa se detenga y espere a que el usuario escriba algo
            telefono = input('📞 Teléfono: ').strip()
            email = input('📧 Email (opcional): ').strip()#decimos que es opcional asi que el usuario puede dejarlo vacio

            # Validar campos obligatorios
            if not nombre:#si el nombre esta vacio 
                print('❌ El nombre no puede estar vacio')#muestra error
                continue  # Volver al inicio del bucle 
            if not telefono:
                print('❌ El teléfono es obligatorio')
                continue # Volver al inicio del bucle

            # Validar email si se proporciona
            if email:
                if not validar_email(email): #si el email no es valido
                    print('❌ Email inválido')#muestra un error
                    print('💡 Formato correcto: usuario@dominio.com')#sugerencia
                    continue# Volver al inicio del bucle

            agregar_contacto(nombre, telefono, email)#llamamos a la función y le pasamos los datos
            print(f'✅ Contacto \'{nombre}\' agregado correctamente')#mensaje si todo esta correcto
            input('\n↵ Presiona Enter para continuar...')#si no hay variable presionamos enter

        #Opcion lista
        elif opcion == '2':
            print('\n' + '👁️' * 30)
            print('   LISTA DE CONTACTOS')
            print('👁️' * 30)
            #invocamos a la lista de contactos
            contactos = listar_contactos()#obtenemos todos los contactos de la base de datos 
            if contactos:  # 📊 Si hay contactos para mostrar
                print(f'📊 Total de contactos: {len(contactos)}')#nos dice cuantos contactos tiene la lista
                print('-' * 60)
                for contacto in contactos: #le damos un valor a cada contacto de la lista 
                    print(f'ID {contacto[0]} | Nombre {contacto[1]} | Telefono {contacto[2]} | Email {contacto[3]}')
                print('-' * 60)
            else:
                # 📭 Si no hay contactos en la agenda
                print('📭 No hay contactos en la agenda')#mensaje para hacernos saber que no hay contactos
                print('💡 Agrega tu primer contacto usando la opción 1')#opcion de agregar un contacto usando la opcion 1
                print('-' * 60)
            input('\n↵ Presiona Enter para continuar...')#en caso de no querer nada solo continuar

        # Opcion actualizar
        elif opcion == '3':
            print('\n' + '✏️' * 30)
            print('   ACTUALIZAR CONTACTO')
            print('✏️' * 30)
            
            # Capturar ID del contacto a actualizar
            id_contacto = input('🆔 Introduzca el ID del contacto a actualizar: ').strip()
            
            # Validar que el ID sea un número
            if not id_contacto.isdigit():#si el id no es un numero
                print('❌ Error: El ID debe ser un número')#mensaje de error
                continue
            
            # pedir nuevos datos
            nombre = input('👤 Nuevo nombre: ').strip()
            telefono = input('📞 Nuevo teléfono: ').strip()
            email = input('📧 Nuevo email: ').strip()
            
            # Validaciones
            if not nombre:
                print('❌ Error: El nombre no puede estar vacío')
                continue
                
            if not telefono:
                print('❌ Error: El teléfono no puede estar vacío')
                continue
            
            # Validar email solo si se proporcionó
            if email and not validar_email(email):
                print('❌ Error: Email inválido')
                print('💡 Formato correcto: usuario@dominio.com')
                continue
            
            # Llamar a la función de actualización
            actualizar_contacto(id_contacto, nombre, telefono, email)#llamamos a la funcion para actualizar el contacto y le damos todos los datos
            print(f'✅ Contacto ID {id_contacto} actualizado exitosamente!')#mensaje de exito
            input('\n↵ Presiona Enter para continuar...')

        #Opción eliminar contacto
        elif opcion == '4':
            print('\n' + '🗑️' * 30)
            print('   ELIMINAR CONTACTO')
            print('🗑️' * 30)
            #solicitamos el ID del contacto que hay que eliminar
            id_contacto = input('🆔 ID del contacto a eliminar: ').strip()
            #validamos que el id sea un numero
            if not id_contacto.isdigit():
                print('❌ Error: El ID debe ser un número')
                continue
            
            #anadimos una confirmación de eliminacion, por si nos arrepentimos o nos equivocamos
            confirmar = input(f'⚠️ ¿Seguro que quieres eliminar el contacto {id_contacto}? (si/no): ').strip().lower()#muestra el id en la pregunta y le damos una opcion

            # .strip().lower() = estas funciones limpian y convierte a minuscula
            
            if confirmar != 'si':  # si la respuesta es diferente a Si
                print('⏹️ Operación cancelada')#mensaje de cancelación
                input('\n↵ Presiona Enter para continuar...')#opcion de salida
                continue #para devolvernos al bucle
            
            #llamamos a la funcion eliminacion
            eliminar_contacto(id_contacto)
            print(f'✅ Contacto ID {id_contacto} eliminado exitosamente!')#mensaje de exito
            input('\n↵ Presiona Enter para continuar...')#opcion de salida
        
        #Opcion exportar 
        elif opcion == '5':
            print('\n' + '📤' * 30)
            print('   EXPORTAR A CSV')
            print('📤' * 30)
            
            # 💾 Lamamos a la función
            exportar_csv()#esta funcion lo hace todo, obtiene contactos, crea archivos csv etc
            
            
            print('💾 Contactos exportados a \'contactos.csv\'')#mensaje de exito
            print('📁 Puedes abrir el archivo con Excel, Google Sheets, etc.')#mensaje informativo
            input('\n↵ Presiona Enter para continuar...')#opcion de salida

        #Opcion buscar
        elif opcion == '6':
            print('\n' + '🔍' * 30)
            print('   BUSCAR CONTACTO')
            print('🔍' * 30)
            
            # 🔎 Pedimos al usuario el nombre del contacto que esta buscando
            nombre = input('🔎 Introduce nombre que quieres buscar: ').strip()
            
            # validamos que no este vacio
            if not nombre:
                print('❌ Error: Debes ingresar un nombre para buscar')
                continue
            
            # 🔍 llamamos a la funcion de busqueda
            buscar_contacto_por_nombre(nombre)
            # IMPORTANTE: Esta función ya muestra los resultados internamente
            # Por eso NO hacemos print() aquí
            
            input('\n↵ Presiona Enter para continuar...')#opcion de salida
        
        # Opcion salir 
        elif opcion == '0':
            print('\n' + '👋' * 35)
            print('   ¡GRACIAS POR USAR LA AGENDA!')
            print('👋' * 35)
            print('👋 Hasta luego, vuelve pronto!')
            break  # Rompe el bucle infinito
            #fin de programa

        #Opcion invalida
        else:#ejecutamos el para cuando no sea elegida ninguna de las opciones del menu, es nuestro sistema de seguridad, como un salvavidas
            print('\n' + '⚠️' * 35)
            print('   OPCIÓN NO VÁLIDA')#mensaje de error
            print('⚠️' * 35)
            print('⚠️ Opción inválida 😅')
            print('💡 Por favor, elige un número del 0 al 6')#mensaje de opciones
            input('\n↵ Presiona Enter para continuar...')#continuar a la salida



