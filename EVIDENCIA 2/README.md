
______  _____   ___  ______ ___  ___ _____ 
| ___ \|  ___| / _ \ |  _  \|  \/  ||  ___|
| |_/ /| |__  / /_\ \| | | || .  . || |__  
|    / |  __| |  _  || | | || |\/| ||  __| 
| |\ \ | |___ | | | || |/ / | |  | || |___ 
\_| \_|\____/ \_| |_/|___/  \_|  |_/\____/ 
                                           
                                           
Bievenido a la guía del proyecto, vamos a llevar tratar de que esta lectura sea lo mas práctica posible:

¿Cómo correr la APP?
- Dentro de la carpeta 'AppFinal' se encuentra la versión final del proyecto, con los módulos organizados por carpetas.
- Ejecutar el único archivo que no se encuentra en ninguna carpeta: 'main.py'

¿Necesito realizar algo antes de poder ejecutar el programa?
- Si, instalar la DB.
- También es necesario modificar las credenciales de acceso dentro del programa para que la APP pueda ingresar.

¿Cómo creo la DB en mi PC?
- Dentro de la carpeta 'SCRIPTS' se encuentra la consulta necesaria para crear la DB (y poblar las tablas, para facilitar el testing de la APP).

¿Cómo modifico las credenciales de acceso?
- Dentro de las carpetas del proyecto, hay una que se llama 'Conexion' con su respectivo 'conexion.py' dentro.
- el parametro que debe ser modificado está señalado con un comentario dentro del código.

¿Acceso para ADMIN?
- Si, en el scrypt de poblado de tablas hay un usuario con USER '1' y PASSWORD '1', para facilitar los continuos accesos.
- Las contraseñas largas no son tan divertidas si tenes que ingresar 100 veces.

 _____  _____ ___  ___ _____  _   _  _____   ___  ______  _____  _____  _____ 
/  __ \|  _  ||  \/  ||  ___|| \ | ||_   _| / _ \ | ___ \|_   _||  _  |/  ___|
| /  \/| | | || .  . || |__  |  \| |  | |  / /_\ \| |_/ /  | |  | | | |\ `--. 
| |    | | | || |\/| ||  __| | . ` |  | |  |  _  ||    /   | |  | | | | `--. \
| \__/\\ \_/ /| |  | || |___ | |\  |  | |  | | | || |\ \  _| |_ \ \_/ //\__/ /
 \____/ \___/ \_|  |_/\____/ \_| \_/  \_/  \_| |_/\_| \_| \___/  \___/ \____/ 
                                                                              
                                                                              
Lo siguiente son comentarios que nos hicimos a lo largo del desarrollo de esta Evidencia

¿Dificultades?
- Si, principalmente nos costó entender como implementar las 'CLASES' (entendemos el concepto y como funcionan, solo que no supimos interpretar qué se esperaba realmente de su uso en el proyecto)
- Mas allá de eso, supimos llevar adelante la totalidad del CRUD con lo que aprendimos hasta ahora (incluso la interacción con la DB)

¿Algo más?
- Intentamos implementar una interfaz gráfica, pero supo ser algo mas complicado de lo esperado y el tiempo no fue suficiente. Quizá para el proximo :D
