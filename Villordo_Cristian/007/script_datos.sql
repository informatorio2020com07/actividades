use cinematografia;

insert into Actores(Nombre,Apellido,fecha_de_nacimiento) values("Marck","Ruffalo", "1967-11-22"),("James","McAvoy","1979-04-21"),("Ashton","Kutcher", "1978-02-07"),("Rachel","McAdams","1978-11-17"),("Ryan","Gosling", null);
insert into Peliculas(Nombre,Estreno,Costo) values("La Isla Siniestra","2010-02-18", null),("Fragmentado","2017-01-19", null),("El Efecto Mariposa","2004-06-24", null),("Diario de una Pasion","2004-10-28",null);
insert into Directores(Nombre,Apellido,fecha_de_nacimiento) values ("Martin", "Escorsese", null),("Night","Shyamalan", null),("Eric","Bress", null),("Mackye","Gruber", null),("nick","Cassavetes",null);
insert into Actores_Peliculas(Id_actor,Id_peliculas) values (5,4);
insert into Actores_Peliculas(Id_actor,Id_peliculas) values (4,4);
insert into Directores_Peliculas(Id_directores,Id_peliculas) values (1,1);
insert into Directores_Peliculas(Id_directores,Id_peliculas) values (3,4);
select * from Actores;
select * from Directores;
select * from Peliculas;
select * from Actores_Peliculas;
select * from Directores_Peliculas;