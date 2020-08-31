DROP database if EXISTS pelis;
CREATE DATABASE if NOT EXISTS pelis;
USE pelis;

CREATE TABLE if not exists personas(
	id INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(50),
	apellido VARCHAR(50),
	fecha_nacimiento DATE null
);

CREATE TABLE if not exists actores(
	persona_id INT NOT null,
	FOREIGN KEY(persona_id) REFERENCES personas(id),
	PRIMARY KEY (persona_id)
);

CREATE TABLE if NOT EXISTS directores(
	persona_id INT NOT null,
	FOREIGN KEY (persona_id) REFERENCES personas(id),
	PRIMARY KEY (persona_id)
);

CREATE TABLE if NOT EXISTS peliculas(
	id INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(50),
	fecha_estreno DATE null,
	coste_total INT NULL
);

CREATE TABLE if NOT EXISTS actores_peliculas(
	pelicula_id INT NOT NULL,
	actor_id INT NOT NULL,
	FOREIGN KEY (pelicula_id) REFERENCES peliculas(id),
	FOREIGN KEY (actor_id) REFERENCES actores(persona_id),
	PRIMARY KEY (pelicula_id, actor_id)
);

CREATE TABLE if NOT EXISTS directores_peliculas(
	pelicula_id INT NOT NULL,
	director_id INT NOT NULL,
	FOREIGN KEY (pelicula_id) REFERENCES peliculas(id),
	FOREIGN KEY (director_id) REFERENCES directores(persona_id),
	PRIMARY KEY (pelicula_id, director_id)
);
