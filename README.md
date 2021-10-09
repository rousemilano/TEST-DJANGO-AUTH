# test-django-auth
**configuraciones e instalaciones para usar el proyecto test-django-auth**

**1. recomendación: prepare su maquina con un entorno virtual en la raiz del proyecto que clonó en su maquina y ejecute los siguientes comandos 
desde su terminal**
*-el comando que yo uso es el siguiente (si no lo tiene instale con el siguiente comando):*

`pip install pipenv`

*-para ejecutar la maquina virtual ingrese el siguiente comando en su terminal:*

`pipenv shell`

**2. procedemos a instalar las dependencias para nuestro proyecto con el siguiente comando (asegurese de estar ubicado en la carpeta que contiene 
el archivo -> requirements.txt ):**

`pip install -r requirements.txt`

**3. proceda a crear una base de datos en postgresql o en el gestor de bbdd de su preferencia
(aquí le dejo los comandos para hacerlo desde la terminal con postgresql) (totalmente básico)**

`psql postgres`

`create database test_auth;`

*-comprobamos que podemos conectarnos a la base de datos*

`\connect test_auth;`

*nota: recuerde configurar el settings.py linea 79 aproximadamente -> cambie su contraseña y usuario que usará en su bbdd*

**4. una vez esté todo configurado proceda ha realizar las migraciones de los modelos a la bbdd, aquí dejo los comandos:**

`python3 manage.py makemigrations`

`python3 manage.py migrate`

**5. proceda a crear un super usuario para acceder a el admin** 

`python3 manage.py createsuperuser`

**6. proceda a ejecutar el servidor con el siguiente comando**

`python3 manage.py runserver`

*nota: puede usar el entorno virtual con el comando de su preferencia, coloque (pipenv) porque es el que usé...
usé ubunto para la creación de este proyecto.*

