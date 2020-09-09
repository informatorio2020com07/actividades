CREATE DATABASE act007;

USE act007;

CREATE TABLE persona (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    fecha_nacimiento DATE
);

CREATE TABLE pelicula (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    fecha_estreno DATE,
    costo_total INT
);

CREATE TABLE persona_pelicula (
    id_persona INT,
    id_pelicula INT,
    rol VARCHAR(20),
    FOREIGN KEY (id_persona) REFERENCES persona (id),
    FOREIGN KEY (id_pelicula) REFERENCES pelicula (id),
    PRIMARY KEY (id_persona, id_pelicula, rol)
);
