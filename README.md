# IDS - Proyecto Final

Este repositorio contiene el proyecto final para la materia de Introducción al Desarrollo de Sowftware. A continuación, se presentan los detalles del equipo de trabajo, los requisitos para ejecutar el proyecto sin errores y las credenciales de prueba que puedes utilizar para probar las funciones de la aplicación.

## Integrantes del Equipo

- Debbie Nicole Cruz Alvarado
- André Giovanni Iraheta Guevara
- Tiffany Lisbeth Meléndez Ramos
- Dana Liz Ochoa González
- Oscar Marcelo Velásquez Zapata

## Requisitos del Proyecto

Este proyecto requiere algunas librerías de Python para su correcto funcionamiento. Asegúrate de que las siguientes librerías estén instaladas en tu entorno:

> ⚠️ **Advertencia:** Si tienes problemas con el archivo, asegúrate de instalar las librerías necesarias:
> 
> ```bash
> pip install pandas
> ```
> ```bash
> pip install bcrypt
> ```
> ```bash
> pip install openpyxl
> ```

Estas librerías son esenciales para manejar el cifrado de contraseñas y la manipulación de archivos Excel.

> 🔴 **Importante:** En caso de no poder iniciar sesión como estudiante o si ves el error en consola:
> ```
> Error loading the student data: [Errno 2] No such file or directory: 'data/students_data.xlsx'
> ```
> Verifica que tienes todo el proyecto abierto en el IDE (sin archivos sueltos fuera de la carpeta principal), y que los archivos de datos estén en la ubicación especificada (`data/students_data.xlsx`).

> 💡 **Tip:** Los ID de los estudiantes se encuentran en el archivo `data/students_data.xlsx`.

> 💡 **Tip:** Los perfiles de administradores se encuentran en el archivo `data/json/admin_password.json`.

## Usuarios y Contraseñas de Testeo

Para fines de testeo, puedes utilizar los siguientes usuarios y contraseñas para probar la funcionalidad del proyecto:

| **Usuarios** | **Contraseñas** |
| ------------ | --------------- |
| admin        | 123             |
| Dre          | 321             |

**Nota:** Asegúrate de usar estas credenciales únicamente para testear las funciones y no para un uso real. Además, si deseas añadir más usuarios o cambiar contraseñas, puedes hacerlo directamente en los archivos `students_data.xlsx` y `admin_password.json` dentro de la carpeta `data`.

---

¡Buena suerte y que tengas una excelente experiencia de desarrollo y prueba con el proyecto!
