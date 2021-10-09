# TEST-DJANGO-AUTH
CONFIGURACIONES E INSTALACIONES PARA USAR EL PROYECTO TEST-DJANGO-AUTH

1. RECOMENDACIÓN: PREPARE SU MAQUINA CON UN ENTORNO VIRTUAL EN LA RAIZ DEL PROYECTO QUE CLONÓ EN SU MAQUINA Y EJECUTE LOS SIGUIENTES COMANDOS 
DESDE SU TERMINAL 
-El comando que yo uso es el siguiente (SI NO LO TIENE INSTALE CON EL SIGUIENTE COMANDO):

->   pip install pipenv

-para ejecutar la maquina virtual ingrese el siguiente comando en su terminal:

->   pipenv shell

2. PROCEDEMOS A INSTALAR LAS DEPENDENCIAS PARA NUESTRO PROYECTO CON EL SIGUIENTE COMANDO (ASEGURESE DE ESTAR UBICADO EN LA CARPETA QUE CONTIENE 
EL ARCHIVO -> requirements.txt ):

->   pip install -r requirements.txt

3. PROCEDA A CREAR UNA BASE DE DATOS EN POSTGRESQL O EN EL GESTOR DE BBDD DE SU PREFERENCIA
(AQUÍ LE DEJO LOS COMANDOS PARA HACERLO DESDE LA TERMINAL CON POSTGRESQL) (TOTALMENTE BÁSICO)

->   psql postgres
->   CREATE DATABASE test_auth;

-comprobamos que podemos conectarnos a la base de datos
->   \connect test_auth;

*NOTA: recuerde configurar el settings.py linea 79 aproximadamente -> cambie su contraseña y usuario que usará en su BBDD

4. UNA VEZ ESTÉ TODO CONFIGURADO PROCEDA HA REALIZAR LAS MIGRACIONES DE LOS MODELOS A LA BBDD, AQUÍ DEJO LOS COMANDOS:

->   python3 manage.py makemigrations
->   python3 manage.py migrate

5. PROCEDA A CREAR UN SUPER USUARIO PARA ACCEDER A EL ADMIN 
->   python3 manage.py createsuperuser

6. PROCEDA A EJECUTAR EL SERVIDOR CON EL SIGUIENTE COMANDO
->   python3 manage.py runserver

*NOTA: puede usar el entorno virtual con el comando de su preferencia, coloque (pipenv) porque es el que usé...
usé ubunto para la creación de este proyecto.

