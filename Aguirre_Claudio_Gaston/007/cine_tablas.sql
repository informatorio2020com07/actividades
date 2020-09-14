CREATE DATABASE cine;

USE cine;

CREATE TABLE actores(
	id_actor int auto_increment primary key,
	nombre varchar(50) not null,
	apellido varchar(50) not null,
	fecha_nacimiento date
	);
	
CREATE TABLE directores(
	id_director int auto_increment primary key,
	nombre varchar(50) not null,
	apellido varchar(50) not null,
	fecha_nacimiento date
	);
	
CREATE TABLE pelis(
	id_peli int auto_increment primary key,
	nombre varchar(50) not null,
	fecha_estreno date
	);
	
CREATE TABLE direccion(
	id_director int not null,
	id_peli int not null,
	foreign key(id_director) references directores(id_director),
	foreign key(id_peli) references pelis(id_peli)
	);

CREATE TABLE actuacion(
	id_actor int not null,
	id_peli int not null,
	foreign key(id_actor) references actores(id_actor),
	foreign key(id_peli) references pelis(id_peli)
	);
