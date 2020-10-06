#Se carga la tabla Director
insert into director (nombre, apellido, fecha_nacimiento) VALUES
( 'Anthony', 'Russo', '1970-02-03'),
( 'James', 'Cameron', '1940-09-11');


#Se carga la tabla Actor
insert into actor(nombre, apellido, fecha_nacimiento) VALUES
('Robert John','Downey Jr','1965-04-04'),
('Christopher Robert', 'Evans', '1981-06-13'),
('Scarlett Ingrid', 'Johansson ', '1984-11-22'),
('Samuel Henry John', 'Worthington ', '1976-08-02'),
('Leonardo Wilhelm', 'DiCaprio', '1974-11-11'),
('Kate Elizabeth', 'Winslet Bridges', '1975-10-05');


#Se carga la tabla Pelicula
INSERT INTO pelicula (nombre, fecha_estreno, costo_total) VALUES
('Avengers: Endgame', '2019-04-25','2797800564'),
('Avatar', '2009-12-18','2787965087'),
('Titanic', '1997-12-19','2187463944'),
('Avengers: Infinity War','2018-04-23','2048359754');

#Se carga la tabla Actores_Peliculas
INSERT INTO actores_peliculas(id_actor, id_pelicula) VALUES
('1','1'),
('2','1'),
('3','1'),
('4','2'),
('5','3'),
('6','3'),
('1','4'),
('2','4'),
('3','4');

#Se carga la tabla Directores_Peliculas
INSERT INTO directores_peliculas (id_director, id_pelicula) VALUES
('1','1'),
('1','4'),
('2','2'),
('2','3');