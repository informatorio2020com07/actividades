INSERT INTO persona (id, nombre, apellido, fecha_nacimiento) VALUES
    (1, "Jack",     "Nicholson",    "1937-04-22"),
    (2, "Malcolm",  "McDowell",     "1943-06-13"),
    (3, "Michael",  "Bay",          "1965-02-17"),
    (4, "Bruce",    "Willis",       "1955-03-19"),
    (5, "Steven",   "Spielberg",    "1946-12-18")
;

INSERT INTO pelicula (id, nombre, fecha_estreno, costo_total) VALUES
    (1, "A Clockwork Orange",   "1971-12-19",   2200000),
    (2, "Halloween",            "2007-09-30",   15000000),
    (3, "Armageddon",           "1998-07-01",   140000000),
    (4, "The Shining",          "1980-05-23",   19000000),
    (5, "Die Hard",             "1988-07-15",   25000000),
    (6, "12 Monkeys",           "1995-12-29",   29000000),
    (7, "Jurassic Park",        "1993-06-09",   63000000)
;

INSERT INTO persona_pelicula (id_persona, id_pelicula, rol) VALUES
    (1, 4, "actor"),    -- Jack Nicholson/The Shining
    (2, 1, "actor"),    -- Malcolm Mcdowell/A Clockwork Orange
    (2, 2, "actor"),    -- Malcolm Mcdowell/Halloween
    (3, 3, "director"), -- Michael Bay/Armageddon
    (3, 3, "actor"),    -- Michael Bay/Armageddon
    (4, 5, "actor"),    -- Bruce Willis/Die Hard
    (4, 6, "actor"),    -- Bruce Willis/12 Monkeys
    (4, 3, "actor"),    -- Bruce Willis/Armageddon
    (5, 7, "director")  -- Steven Spielberg/Jurassic Park
;
