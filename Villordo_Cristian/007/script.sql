create database cinematografia;

use cinematografia;


create table if not exists Actores(
	id_actor int auto_increment primary key,
	nombre varchar(30) not null,
	apellido varchar(30) not null,
	fecha_de_nacimiento date null );

create table if not exists Peliculas(
	id_peliculas int auto_increment primary key,
	nombre varchar(30) not null,
	estreno date null,
	costo int null);

create table if not exists Directores(
	id_directores int auto_increment primary key,
	nombre varchar(30) not null,
	apellido varchar(30) not null,
	fecha_de_nacimiento date null );

create table if not exists Actores_Peliculas(
	id_peliculas int not null,
	id_actor int not null,
	foreign key ( id_peliculas ) references Peliculas( id_peliculas ),
	foreign key (id_actor) references Actores(id_actor),
	primary key (id_peliculas,id_actor));

create table if not exists Directores_Peliculas(
	id_peliculas int not null,
	id_directores int not null,
	foreign key ( id_peliculas ) references Peliculas( id_peliculas ),
	foreign key (id_directores) references Directores(id_directores),
	primary key (id_peliculas, id_directores));