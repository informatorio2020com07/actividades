CREATE DATABASE Estudio;
USE Estudio;

CREATE TABLE Pelicula(
    id int auto_increment primary key,
    titulo varchar(50) not null,
    fecha_estreno date not null,
    costo_total float not null
);

CREATE TABLE Actor_director(
    id int auto_increment primary key,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    fecha_nacimiento date not null
);
CREATE TABLE Pelicula_actor(
    id_pelicula int,
    id_actor int,
    funcion varchar(20) not null,
    foreign key(id_pelicula) references Pelicula(id),
    foreign key(id_actor) references Actor_director(id)
);
CREATE TABLE Pelicula_director(
    id_pelicula int,
    id_director int,
    funcion varchar(20) not null,
    foreign key(id_pelicula) references Pelicula(id),
    foreign key(id_director) references Actor_director(id)
);

