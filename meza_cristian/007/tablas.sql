# Se crea tabla Director
CREATE TABLE  Director (
	id_director int auto_increment,
	nombre  varchar (50) NOT NULL,
	apellido  varchar (50) NOT NULL,
	fecha_nacimiento  date NOT NULL,
	PRIMARY KEY (id_director)
	);
# Se crea tabla Actor
CREATE TABLE  Actor (
	id_actor int auto_increment,
	nombre   varchar (50) NOT NULL,
	apellido  varchar (50) NOT NULL,
	fecha_nacimiento  date NOT NULL,
	PRIMARY KEY (id_actor)
	);
# Se crea tabla Pelicula
CREATE TABLE  Pelicula (
	id_pelicula int auto_increment,
	nombre varchar (50) NOT NULL ,
	fecha_estreno date NOT NULL ,
	costo_total decimal NOT NULL,
	PRIMARY KEY (id_pelicula)
	);
# Se crea tabla Actores_Peliculas
CREATE TABLE Actores_Peliculas(
	id_actor int  NOT NULL,
	id_pelicula int NOT NULL,
	PRIMARY KEY (id_actor, id_pelicula),
	FOREIGN KEY (id_actor) references Actor(id_actor),
	FOREIGN KEY (id_pelicula) references Pelicula (id_pelicula)
	);
#Se crea tabla Directores_Peliculas
CREATE TABLE Directores_Peliculas(
	id_director int NOT NULL,
	id_pelicula int NOT NULL,
	PRIMARY KEY (id_director, id_pelicula),
	FOREIGN KEY (id_director) REFERENCES Director(id_director),
	FOREIGN KEY (id_pelicula) REFERENCES Pelicula(id_pelicula)
	);