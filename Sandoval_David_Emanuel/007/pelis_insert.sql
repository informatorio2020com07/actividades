USE pelis;
INSERT INTO personas VALUES(NULL, "emanuel", "sandoval", NULL);
INSERT INTO personas VALUES(NULL, "lucas", "sandoval", NULL);
INSERT INTO personas VALUES(NULL, "clarisa", "sandoval", NULL);
INSERT INTO personas VALUES(NULL, "margarita", "cabral", NULL);
INSERT INTO personas VALUES(NULL, "ramón", "piero", NULL);
INSERT INTO personas VALUES(NULL, "pedro", "zuásquita", NULL);
INSERT INTO personas VALUES(NULL, "chancho", "moro", NULL);
INSERT INTO personas VALUES(NULL, "damián", "soto", NULL);


INSERT INTO peliculas VALUES(NULL, "el zorro", NULL, NULL);
INSERT INTO peliculas VALUES(NULL, "el secreto de sus ojos", NULL, NULL);
INSERT INTO peliculas VALUES(NULL, "matrix", NULL, NULL);
INSERT INTO peliculas VALUES(NULL, "titanic", NULL, NULL);
INSERT INTO peliculas VALUES(NULL, "jurassic park", NULL, NULL);
INSERT INTO peliculas VALUES(NULL, "la rueda", NULL, NULL);
INSERT INTO peliculas VALUES(NULL, "siniestro", NULL, NULL);

INSERT INTO actores VALUES(1);
INSERT INTO actores VALUES(2);
INSERT INTO actores VALUES(3);
INSERT INTO actores VALUES(4);
INSERT INTO actores VALUES(5);
INSERT INTO actores VALUES(6);
INSERT INTO actores VALUES(7);

INSERT INTO directores VALUES(1);
INSERT INTO directores VALUES(3);
INSERT INTO directores VALUES(5);
INSERT INTO directores VALUES(6);

INSERT INTO actores_peliculas VALUES(1, 2);
INSERT INTO actores_peliculas VALUES(4, 1);
INSERT INTO actores_peliculas VALUES(3, 7);

INSERT INTO directores_peliculas VALUES(4, 1);
INSERT INTO directores_peliculas VALUES(1, 3);
INSERT INTO directores_peliculas VALUES(6, 5);

SELECT * FROM personas;
SELECT * FROM peliculas;
SELECT * FROM actores;
SELECT * FROM directores;
SELECT * FROM directores_peliculas;
SELECT * FROM actores_peliculas;
