INSERT INTO actor (nombre_actor, apellido_actor,fecha_nac_actor) VALUES
( 'Al', 'Pacino', '1940-04-11'),  
( 'Marlon', 'Brandon', '1924-04-03'),
( 'James', 'Caan', '1940-03-11'),
( 'Richard', 'Castellano', '1933-09-04'),
( 'Robert', 'Duval', '1931-01-05'),
( 'Sterling', 'Hayden', '1916-03-11'),
( 'Diane', 'Keaton', '1946-01-05'),
( 'Woody', 'Allen', '1946-01-05');

INSERT INTO director (nombre_dir, apellido_dir,fecha_nac_dir) VALUES
( 'Woody', 'Allen', '1946-01-05'),  
( 'Brian', 'De Palma', '1940-09-11'),
( 'Francis', 'Ford Coppola', '1939-04-07'),
( 'Taylor', 'Hackford', '1944-12-11');


INSERT INTO pelicula (nombre_pel, fech_estreno,costo_total) VALUES
('El Padrino', '1972-03-11','6000000'),  
('Scarface', '1984-02-09','25000000'),
('El abogado del diablo', '1998-01-01','57000000'),
('Manhattan', '1980-05-11','9000000'),
('Hanna y sus hermanas', '1986-09-11','6400000');

INSERT INTO Actua_en (id_actor, id_pelicula) VALUES
('1','1'),
('2','1'),
('3','2');

INSERT INTO Es_dirigida (id_director, id_pelicula) VALUES
('1','1'),
('2','3');





 