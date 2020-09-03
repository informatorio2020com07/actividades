SYSTEM CLS
DROP DATABASE IF EXISTS act007;
CREATE DATABASE act007;

USE act007;

CREATE TABLE roles (
  Id int AUTO_INCREMENT PRIMARY KEY,
  Descripcion varchar(50) NOT NULL
);

CREATE TABLE personas (
  Id int AUTO_INCREMENT PRIMARY KEY,
  Nombre varchar(20) NOT NULL,
  Apellido varchar(20) NOT NULL,
  Nacimiento date NOT NULL
   
);

CREATE TABLE peliculas (
  Id int AUTO_INCREMENT PRIMARY KEY,
  Nombrep varchar(50) DEFAULT NULL,
  Estreno date NOT NULL,
  Costo decimal DEFAULT NULL
);

CREATE TABLE personasenpeliculas (
  Id int AUTO_INCREMENT PRIMARY KEY,
  Id_persona int NOT NULL,
  Id_pelicula int NOT NULL,
  id_rol int NOT NULL,

  FOREIGN KEY (Id_rol) REFERENCES roles (id),
  FOREIGN KEY (Id_persona) REFERENCES personas (id),
  FOREIGN KEY (Id_pelicula) REFERENCES peliculas (id)
);

INSERT INTO roles (Descripcion) VALUES 
 ('Actor principal'),
 ('Actor secundario'),
 ('Productor'),
 ('Director')
; 
 
INSERT INTO personas (Nombre,Apellido,Nacimiento) VALUES 
 ('Robert','De Niro','1946-02-19'),
 ('Brad','Pit','1965-12-19'),
 ('Romeo','Santos','2000-12-19'),
 ('Elena','Vinder','2011-12-19'),
 ('Steven','Spilberg','1955-12-19'),
 ('Roman','Polansky','1950-12-19')
; 

INSERT INTO peliculas (Nombrep,Estreno,Costo) VALUES 
 ('EL ALBA','2010-11-11',2000000),
 ('SOMBRAS','1998-10-10',12000000),
 ('COSMOS 1999','1980-01-01',500000)
; 

INSERT INTO personasenpeliculas (Id_persona,Id_pelicula,Id_rol) VALUES
(1,1,1),
(1,1,3),
(4,1,2),
(5,1,4),
(2,2,1),
(3,2,2),
(6,2,4),
(5,2,3),
(1,3,1),
(6,3,1)
;

SELECT p.nombrep, pe.nombre, pe.apellido, r.descripcion 
FROM peliculas p, personas pe, roles r, personasenpeliculas pp  
WHERE pp.id_rol = r.id AND pp.id_persona = pe.id AND pp.id_pelicula = p.id;

SELECT p.nombrep pelicula, pe.nombre , pe.apellido apellido_actor, r.descripcion participacion
FROM personasenpeliculas pp JOIN peliculas p JOIN personas pe JOIN roles r 
on pp.id_pelicula = p.id AND pp.id_persona = pe.id AND pp.id_rol = r.id;
