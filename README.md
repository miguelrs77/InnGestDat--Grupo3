# InstaTURNO

`InstaTURNO` es un sistema de gestión de turnos médicos que permite a los usuarios, en pocos pasos, agendar turnos para estudios médicos y consultas a profesionales de las diversas ramas de la salud.

Las principales funcionalidades que incluye son:
- Gestión de Turnos:
    - Reserva de turnos.
    - Consulta de turnos.
    - Actualización de turnos.
- Gestión de Especialidades:
    - Creación de especialidades médicas.
    - Consulta de especialidades médicas.
    - Actualización de especialidades médicas.
- Gestión de Departamentos:
    - Creación de departamentos de estudios médicos.
    - Consulta de departamentos de estudios médicos.
    - Actualización de departamentos de estudios médicos.
- Gestión de Horarios:
    - Creación de horarios de atención.
    - Consulta de horarios de atención.
    - Actualización de horarios de atención.
- Gestión de Personal:
    - Creación de profesionales de la salud.
    - Consulta de profesionales de la salud.
    - Actualización de profesionales de la salud.
- Gestión de Pacientes:
    - Creación de pacientes.
    - Consulta de pacientes.
    - Actualización de pacientes.
- Gestión de Usuarios:
    - Creación de usuarios.
    - Consulta de usuarios.
    - Actualización de usuarios.
- Gestión de Roles:
    - Creación de roles.
    - Consulta de roles.
    - Actualización de roles.

## Contexto
> La propuesta `InstaTURNO` es desarrollada por el `Grupo 3`: `Córdoba Data Solutions` como `Proyecto Integrador ABP` del `Módulo Innovación en Gestión de Datos` de la carrera `Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial - Cohorte 2024` dictada en el `Instituto Superior Politécnico Córdoba (ISPC)` de la `Provincia de Córdoba`, `Argentina`.

---

# Proyecto Integrador ABP
- **Asignaturas:**
    - Base de Datos II (_Docente/Tutor: Romina_)
    - Programación II (_Docente/Tutor: Julián Conde_)
- **Módulo:**
    - Innovación en Gestión de Datos
- **Carrera - Cohorte:**
    - Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial - Cohorte 2024
- **Institución:**
    - Instituto Superior Politécnico Córdoba

### Grupo 3 - Integrantes:
- **ALCALDE, MARIANA ANDREA**
    - _Usuario GitHub_: [marianaalcalde](https://github.com/marianaalcalde)
    - _Mail_: alcalde.research@gmail.com
    - _DNI_: 25246330
- **ASTORGA DE GIUSTI, MATIAS ALEJANDRO**
    - _Usuario GitHub_: [30matias30](https://github.com/30matias30)
    - _Mail_: 30matias30@gmail.com
    - _DNI_: 39610073
- **GUILLÉN, JONATHAN EDUARDO**
    - _Usuario GitHub_: [JG-UNC](https://github.com/JG-UNC)
    - _Mail_: jonathan.guillen@mi.unc.edu.ar
    - _DNI_: 34440292
- **MAJZUM, MAIA**
    - _Usuario GitHub_: [maiamajzum](https://github.com/maiamajzum)
    - _Mail_: maiamjzum@gmail.com
    - _DNI_: 34889057
- **REYNOSO MARTIN, MATEO**
    - _Usuario GitHub_: [MateoReynosoM](https://github.com/MateoReynosoM)
    - _Mail_: mateoreynoso2009@gmail.com
    - _DNI_: 43881462
- **RODRIGUEZ SAQUILAN, MIGUEL**
    - _Usuario GitHub_: [Miguelrs77](https://github.com/miguelrs77)
    - _Mail_: miguelr.s77@gmail.com
    - _DNI_: 18889456 


## Estructura de Carpetas del Proyecto

```
InstaTURNO--Grupo3--DS-IA/
EVIDENCIA 1
|   ├── APLICACION/
|   ├── Bienvenida y Login/    
|   |     └── login.py
|   ├── Captcha/    
|   |     └── Captcha.py
|   ├── Modulo Aritmetica/    
|   |     └── aritmetica.py
|   ├── Registrar un Usuario/    
|   |     └── RegistrarUsuario.py
|   ├── Aserciones/    
|   |     └── asersiones.py
|   ├── BASE DE DATOS
|   |     ├── CONCLUSION
|   |     ├── DESCRIPCION
|   |     ├── DIAGRAMA ER.png
|   |     ├── Insta-DB2.jpeg
|   |     └── TABLAS
|   └── Evidencia_1_10.01v 
└── README

```

### Descripcion archivos del repositorio:

> #### **APLICACION**: _Este directorio contiene todos los archivos relacionados a los diferentes modulos solicitados._

- **[consultas_generales/consulta_global.py](APLICACION/consultas_generales/consulta_global.py)**
    - Contiene la función consulta_global, que muestra todos los turnos registrados en el sistema. Si hay turnos disponibles, los 
      muestra en una tabla ordenada por código de turno; de lo contrario, imprime un mensaje indicando que no hay turnos cargados en el 
      sistema.
      
- **[consultas_generales/consulta_medicos.py](APLICACION/consultas_generales/consulta_medicos.py)**
    - Ofrece la función consulta_medicos, que muestra una lista de médicos y sus especialidades consultando la base de datos. Si hay 
      médicos disponibles, los muestra en una tabla; de lo contrario, imprime un mensaje indicando que no hay médicos registrados.

- **[mysql/](APLICACION/mysql)**
    - Biblioteca descargada para conectarse correctamente a la base de datos.

- **[tabulate/](APLICACION/tabulate)**
    - Biblioteca descargada para que acomode las tablas al imprimir por consola.
 
- **[actualizar_turno.py](APLICACION/actualizar_turno.py)**
    - Permite al usuario actualizar información de un turno existente, como cambiar el paciente o el área médica. Solicita al usuario 
      que ingrese el código del turno y la información actualizada.

- **[conectar_base_datos.py](APLICACION/Creacion_tablas_python.py)**
    - Función llamada conectar_base_datos, que establece una conexión con una base de datos MySQL utilizando las credenciales 
      proporcionadas (host, usuario, contraseña y nombre de la base de datos). La función devuelve el objeto de conexión para su uso 
      posterior en otras partes del programa.

- **[consultar_turno.py](APLICACION/consultar_turno.py)**
    - Permite al usuario buscar turnos, ya sea por el DNI del paciente o mostrando todos los turnos disponibles. Muestra los resultados 
      en forma tabular si los encuentra.

- **[crear_turno.py](APLICACION/crear_turno.py)**
    - Permite al usuario crear un nuevo turno seleccionando primero una especialidad médica y luego ingresando su información personal. 
      Verifica si el paciente ya existe en la base de datos y lo agrega si es necesario, luego crea el nuevo turno.

- **[eliminar_turno.py](APLICACION/eliminar_turno.py)**
    - Permite al usuario eliminar un turno existente proporcionando su código. Verifica si se encuentra el turno y lo elimina de la base 
      de datos.

- **[Guia_de_usuario.txt](APLICACION/Guía_de_usuario.txt)**
    - Instructivo de uso para técnicos y usuarios finales.

- **[menu.py](APLICACION/menu.py)**
    - Ofrece un menú interactivo que permite al usuario seleccionar entre varias acciones, como crear, consultar, actualizar y eliminar 
      turnos, así como acceder a opciones avanzadas como listar médicos. Utiliza funciones modulares para ejecutar las acciones 
      seleccionadas.

- **[opciones_avanzadas.py](APLICACION/opciones_avanzadas.py)**
    - Ofrece al usuario acceso a opciones avanzadas, en este caso, listar médicos disponibles. Al seleccionar esta opción, muestra la 
      lista de médicos utilizando una función modular.

> #### **BASE DE DATOS**: _Este directorio contiene los archivos solicitados en relacion a la información de la base de datos que utilizaremos en nuestro proyecto._

- **CONCLUSION**
    - Este archivo contiene una conclusion de la viabilidad e importancia del proyecto.

- **DESCRIPCION**
    - Este archivo describe las funcionalidads futuras del proyecto.
      
- **DIAGRAMA ER.png**
    - Diagrama que contiene las tablas iniciales del proyecto y su relacion.
 
- **Insta-DB2.jepg**
    - Diagrama de las tablas futuras del proyecto incorporando más funciones:

- **Documento**
    - Contiene un PDF con los datos solicitados. Esquema:
       - 1. Portada:
       - a. En en segunda página se incluye el DER.
       - b. Nombre del estudiante.
       - c. Nombre de la asignatura
       - d. Fecha de entrega
       - 2. Resumen del proyecto:
       - a. Breve descripcion del tema elegido para el proyecto final.
       - b. Objetivos principales.
       - c. Metodologia a utilizar.
       - d. relevancia del proyecto en el contexto académico o profesional.       
       
- **Evidencia_1_0.01v**
    - 
