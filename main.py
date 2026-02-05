from database import crear_tabla#importamos de manera modular nuestros archivos y invocamos la funcion crear tabla
from interfaz import ejecutar_menu#importamos del archivo interfaz y invocamos ejecutar menu

# 🏁 Punto de entrada del programa
if __name__ == '__main__':#__name__ es una variable que guarda informacion, si el name es == a main ejecuta nuestro programa
    print('\n' + '🎉' * 35)
    print('   BIENVENIDO/A A LA AGENDA DE CONTACTOS')
    print('🎉' * 35)
    crear_tabla()      # 🗄️ Crear tabla si no existe
    ejecutar_menu()    # 🖥️ Mostrar menú
