📒 Gestión de Contactos
https://img.shields.io/badge/Python-3.8+-blue.svg
https://img.shields.io/badge/SQLite-3.50.4-green.svg
https://img.shields.io/badge/License-MIT-yellow.svg

Un gestor de contactos eficiente y seguro desarrollado en Python con base de datos SQLite, diseñado para administrar tu libreta de contactos de manera intuitiva.

📋 Características Principales
✅ CRUD Completo: Crear, Leer, Actualizar y Eliminar contactos

🛡️ Seguridad Robust: Consultas parametrizadas para prevenir inyección SQL

📤 Exportación Flexible: Exporta contactos a formato CSV

🔄 Operaciones Seguras: Confirmación para operaciones críticas (eliminación)

🎯 Interfaz Intuitiva: Menú interactivo en consola con validación de entradas

🏗️ Arquitectura Modular: Código organizado y mantenible

🛠️ Tecnologías Utilizadas
Python 3.8+ - Lenguaje principal

SQLite 3.50.4 - Base de datos embebida

CSV Module - Exportación de datos

SQL Parametrizado - Seguridad en consultas

📁 Estructura del Proyecto
text
contact-manager/
├── main.py              # Punto de entrada principal
├── database.py          # Gestión de conexión y configuración BD
├── contact_operations.py # Operaciones CRUD de contactos
├── export_manager.py    # Exportación a CSV
├── utils.py            # Utilidades y validaciones
├── contactos.db        # Base de datos (generada automáticamente)
├── requirements.txt    # Dependencias del proyecto
└── README.md          # Documentación
🗄️ Estructura de la Base de Datos
Tabla: contactos

Columna	Tipo	Descripción
id	INTEGER	Clave primaria (autoinc)
nombre	TEXT	Nombre completo
telefono	TEXT	Número de teléfono
email	TEXT	Correo electrónico
🚀 Instalación y Configuración
Prerrequisitos
Python 3.8 o superior

10 MB de espacio libre

Pasos de Instalación
Clonar el repositorio

bash
git clone https://github.com/tuusuario/gestion-contactos.git
cd gestion-contactos
Crear entorno virtual (recomendado)

bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
Instalar dependencias

bash
pip install -r requirements.txt
💻 Uso del Programa
Ejecutar la aplicación
bash
python main.py
Funcionalidades Disponibles
Menú Principal
text
GESTIÓN DE CONTACTOS - MENÚ PRINCIPAL
1. Ver todos los contactos
2. Agregar nuevo contacto
3. Buscar contacto
4. Actualizar contacto
5. Eliminar contacto
6. Exportar contactos a CSV
7. Ver estadísticas
8. Salir
Ejemplos de Uso
Agregar un contacto:

text
Opción: 2
Nombre: Juan Pérez
Teléfono: 123456789
Email: juan@email.com
✅ Contacto agregado exitosamente
Exportar a CSV:

python
# Genera archivo: contactos_export_YYYYMMDD_HHMMSS.csv
# Contenido:
# id,nombre,telefono,email
# 1,Juan Pérez,123456789,juan@email.com
🔒 Características de Seguridad
✅ Implementadas
Consultas Parametrizadas: Uso de ? como placeholders

Validación de Entradas: Filtrado de datos del usuario

Transacciones SQLite: Operaciones atómicas

Confirmación de Eliminación: Doble verificación para borrados

⚠️ Consideraciones
No almacenar información sensible sin cifrado adicional

Realizar copias de seguridad periódicas del archivo .db

Utilizar en entornos controlados para producción

📊 Funciones Específicas
Operaciones CRUD
python
# Crear contacto
agregar_contacto(nombre, telefono, email)

# Leer contactos
obtener_contactos()
buscar_contacto(termino)

# Actualizar contacto
actualizar_contacto(id, nombre, telefono, email)

# Eliminar contacto
eliminar_contacto(id)
Exportación CSV
python
exportar_a_csv()  # Crea archivo con timestamp
🧪 Datos de Ejemplo
El programa incluye 3 contactos de demostración:

Melvin Navas - 829-111-2222 - melvin@email.com

María García - 809-333-4444 - maria@email.com

Carlos López - 829-555-6666 - carlos@email.com

📈 Estadísticas Disponibles
Total de contactos registrados

Contactos agregados por fecha

Distribución de dominios de email

🐛 Solución de Problemas
Problemas Comunes
"No se puede crear la base de datos"

Verificar permisos de escritura en el directorio

Comprobar espacio en disco

"Error al exportar CSV"

Verificar permisos de escritura

Cerrar archivo CSV si está abierto en otro programa

"Módulo sqlite3 no encontrado"

Reinstalar Python con soporte SQLite

Ejecutar en entorno virtual configurado

🤝 Contribuir
Haz fork del proyecto

Crea una rama (git checkout -b feature/mejora)

Commit tus cambios (git commit -m 'Añadir mejora')

Push a la rama (git push origin feature/mejora)

Abre un Pull Request

📄 Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

👨‍💻 Autor
Melvin Omar Navas Santos

Estudiante de Programación Python

Institución: CEIP COLON

GitHub: @melvinnavas

📞 Contacto
¿Preguntas o sugerencias?

📧 Email: melvin@email.com

🐛 Reportar issues: GitHub Issues

🎓 Contexto Educativo
Este proyecto fue desarrollado como parte del curso de Programación Python en CEIP COLON, demostrando:

Manejo de bases de datos SQLite

Programación estructurada en Python

Buenas prácticas de seguridad

Desarrollo de aplicaciones CRUD completas

✨ ¡Gestiona tus contactos de manera profesional y segura! ✨

"La organización es la clave de la productividad"