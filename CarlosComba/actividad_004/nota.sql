CREATE DATABASE nota;
USE nota;

CREATE TABLE titulo(
    id_nota int auto_increment primary key,
    titulo varchar(50)
);

CREATE TABLE renglones(
    id int auto_increment primary key,
    renglones varchar(400),
    id_nota int,
    foreign key(id_nota) references titulo(id_nota)
);

INSERT INTO titulo(titulo) values ("despido");
INSERT INTO titulo(titulo) values ("renuncia");
INSERT INTO renglones(id_nota,renglones) values (1,"Sr. destinatario: me dirijo a usted a fin de comunicarle, que se");
INSERT INTO renglones(id_nota,renglones) values (1,"encuentra fuera de la nomina de la empresa. Debido a sus sucesibas");
INSERT INTO renglones(id_nota,renglones) values (1,"faltas, esta decision fue comunicada a contabilidad pase a cobrar.");
INSERT INTO renglones(id_nota,renglones) values (1,"atentamente remitente");
INSERT INTO renglones(id_nota,renglones) values (2,"Sr. destinatario: me dirijo a usted a fin de comunicarle,");
INSERT INTO renglones(id_nota,renglones) values (2,"mi renuncia a la empresa debido a motivos personas.");
INSERT INTO renglones(id_nota,renglones) values (2,"atentamente remitente");
