# Introducción a la ingeniería de Software Proyecto Final

Este repositorio contiene el proyecto final para la materia de **Introducción al Desarrollo de Software**. A continuación, encontrarás detalles sobre los integrantes del equipo, los requisitos necesarios para ejecutar el proyecto sin errores y las credenciales de prueba para explorar las funciones de la aplicación.

## Integrantes del Equipo

- Debbie Nicole Cruz Alvarado
- André Giovanni Iraheta Guevara
- Tiffany Lisbeth Meléndez Ramos
- Dana Liz Ochoa González
- Oscar Marcelo Velásquez Zapata

## Desarrollador

- André Giovanni Iraheta Guevara
  
## Requisitos del Proyecto

Este proyecto necesita algunas librerías de Python. Verifica que tienes las siguientes librerías instaladas en tu entorno:

> ⚠️ **Advertencia:** Si encuentras problemas con la ejecución del proyecto, revisa que estas librerías estén correctamente instaladas.

> ### Windows
> ```bash
> pip install pandas bcrypt openpyxl pillow
> ```

> ### MacOS
> ```bash
> python3 -m pip install pandas bcrypt openpyxl pillow
> ```

Estas librerías son esenciales para el cifrado de contraseñas y la manipulación de archivos Excel.

> 🔴 **Importante:** Si no puedes iniciar sesión como estudiante o encuentras el error:
> ```
> Error loading the student data: [Errno 2] No such file or directory: 'data/students_data.xlsx'
> ```
> Asegúrate de tener todos los archivos en la estructura correcta del proyecto y que el archivo `data/students_data.xlsx` esté en la ubicación especificada.

> 💡 **Tip:** Los ID de los estudiantes están en `data/students_data.xlsx`.
> 
> 💡 **Tip:** Los perfiles de administrador están en `data/json/admin_password.json`.

## Credenciales de Prueba

Para probar la funcionalidad del proyecto, utiliza los siguientes datos de acceso:

### Estudiantes
| **ID** |  **Nombre**  |
| ------ | ------------ |
| 202401 | Estudiante1  |
| 202402 | Estudiante2  |
| 202403 | Estudiante3  |
|   ...  |     ...      |
| 202431 | Estudiante31 |

### Administradores
| **Usuario** | **Contraseña** |
| ----------- | -------------- |
| admin       | 123            |
| dre         | 321            |

**Nota:** Estas credenciales son solo para testeo. Si deseas agregar o modificar usuarios, puedes hacerlo en los archivos `students_data.xlsx` y `admin_password.json` en la carpeta `data`.

---

**¡Cruzamos los dedos para que todo funcione y consigamos el 10!**

**[Link al repositorio en GitHub](https://github.com/DreGi0/IDS-Proyecto-Final)**
