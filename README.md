# magneto-api

Con magneto-api sabrás cuando un humano es mutante, si encuentras más de una secuencia de cuatro letras iguales , de forma oblicua, horizontal o vertical. 

![enter image description here](https://raw.githubusercontent.com/aescobar-icc/magneto-api/master/img/matris.png)

Esta solución implementa un micro servicio para un Docker Container.

# Instalacion Local
### 1.- Instalar `Docker` .

**Instalación OSX**

        brew cask install docker
Luego corre **Docker.app** . Click next. Te pedirá permisos de acceso que debes confirmar. Te aparecerá el icono de una ballena en la barra de tareas has click en él y espera a que aparezca **"Docker is running"**.   

**Instalación Ubuntu**

        sudo apt install docker.io
        sudo systemctl start docker


### 2.- Obtén  el proyecto

        https://github.com/aescobar-icc/magneto-api.git

### 3.- Creacion de la base de datos
La api se conecta a una base de datos MySql para guardar los stats de verificaciones de adn.

**Script de creación de Base de Datos**
		
		CREATE DATABASE IF NOT EXISTS magneto;
		use magneto;
		CREATE TABLE IF NOT EXISTS stats (
		    stat_id INT AUTO_INCREMENT,
		    is_mutant boolean NOT NULL,
		    register timestamp,
		    dna TEXT NOT NULL,
		    dna_hash VARCHAR(128) NOT NULL,
		    PRIMARY KEY (stat_id),
		    UNIQUE KEY(dna_hash)
		)  ENGINE=INNODB;
**Nota Importante:** La api puede funcionar sin la base de datos, esto se verá en más detalle en la sección probar api.

### 4.- Configurar conexión a Base
Por simplicidad la uri de conexión a la base se debe especificar en el archivo `Dockerfile`

		ENV SQLALCHEMY_URI=mysql+pymysql://admin:admin@123.123.123.123:3306/magneto
Para este ejemplo de conexión, estoy asumiendo que el servidor MySql es local y para poder accederlo desde el contenedor se debe anexar un alias de IP a la interfaz de red, para ello en la máquina host debes correr el siguiente comando:

		sudo ifconfig lo0 alias 123.123.123.123/24
En caso de que estés accediendo a un servidor con IP pública el paso anterior no es necesario.

### 5.- Crea una imagen docker a partir del proyecto

        $ cd magneto-api
        $ sudo docker build -t magneto-api:v1 .
        
 Verificar si la imagen se creó correctamente.

	$ sudo docker images
	REPOSITORY  TAG IMAGE ID     CREATED   SIZE 
	magneto-api v1  349e5abc9fec 5sec ago  343MB
### 6.- Correr la Api 
Ahora que ya tienes la imagen creada puedes correr el micro servicio.

        $ sudo docker run -it -p 5050:5000 magneto-api:v1

Aquí se está especificando que en el `host` la API será visible en el puerto 5050 y que en el `contenedor` corre en el puerto 5000.

### 7.- Probar api usando postman

Nuestra imagen se ha publicado en http://localhost:5050/mutant podemos testear fácilmente nuestra API usando `postman` enviando la información de adn en el siguiente formato:

		{ “dna”:
			["ATGCGA",
			"CAGTGC",
			"TTATGT",
			"AGAAGG",
			"CCCCTA",
			"TCACTG"]
		}
**Nota Importante:** Si no has instalado la base de datos puedes agregar el valor `"nobase":null` para decirle a la API que no use la base de datos, obviamente esto hará que no se guarden los stats.

		{ “dna”:
			["ATGCGA",
			"CAGTGC",
			"TTATGT",
			"AGAAGG",
			"CCCCTA",
			"TCACTG"],
			"nobase":null
		}

![enter image description here](https://raw.githubusercontent.com/aescobar-icc/magneto-api/master/img/postman.png)


### 8.- Instalacion GCloud

Para una completa guía de como instalar esta API en la nube de google sigue este tutorial:

[https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app](https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app)
