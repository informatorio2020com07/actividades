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
  Nacimiento date NOT NULL,
  Rol int NOT NULL,
  FOREIGN KEY(Rol) REFERENCES roles(id)
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
  FOREIGN KEY (Id_persona) REFERENCES personas (id),
  FOREIGN KEY (Id_pelicula) REFERENCES peliculas (id)
);

INSERT INTO roles (Descripcion) VALUES 
 ('Actor principal'),
 ('Actor secundario'),
 ('Productor'),
 ('Director')
; 
 
INSERT INTO personas (Nombre,Apellido,Nacimiento,Rol) VALUES 
 ('Robert','De Niro','1946-02-19',1),
 ('Brad','Pit','1965-12-19',1),
 ('Romeo','Santos','2000-12-19',2),
 ('Elena','Vinder','2011-12-19',2),
 ('Roman','Polansky','1950-12-19',4),
 ('Steven','Spilberg','1955-12-19',1),
 ('Steven','Spilberg','1965-12-19',3),
 ('Roman','Polansky','1950-12-19',1)
; 

INSERT INTO peliculas (Nombrep,Estreno,Costo) VALUES 
 ('EL ALBA','2010-11-11',2000000),
 ('SOMBRAS','1998-10-10',12000000),
 ('COSMOS 1999','1980-01-01',500000)
; 

INSERT INTO personasenpeliculas (Id_persona,Id_pelicula) VALUES
(1,1),
(4,1),
(5,1),
(2,2),
(3,2),
(6,2),
(7,2),
(1,3),
(6,3)
;

SELECT p.nombrep, pe.nombre, pe.apellido, r.descripcion 
from peliculas p, personas pe, roles r, personasenpeliculas pp  
where pe.rol = r.id AND pp.id_persona = pe.id AND pp.id_pelicula = p.id;

SELECT p.nombrep pelicula, pe.nombre , pe.apellido apellido_actor, r.descripcion participacion
from personasenpeliculas pp JOIN peliculas p JOIN personas pe JOIN roles r 
on pp.id_pelicula = p.id AND pp.id_persona = pe.id AND pe.rol = r.id;
