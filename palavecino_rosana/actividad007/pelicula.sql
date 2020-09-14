# Creación de la tabla Actor 
CREATE TABLE  Actor ( 
	id_actor int auto_increment,  
	nombre_actor   varchar (30) NOT NULL, 
	apellido_actor  varchar (20) NOT NULL, 
	fecha_nac_actor  date NOT NULL,
	PRIMARY KEY (id_actor)
	
	);

# Creación de la tabla Director 
CREATE TABLE  Director ( 
	id_director int auto_increment, 
	nombre_dir  varchar (30) NOT NULL, 
	apellido_dir  varchar (20) NOT NULL, 
	fecha_nac_dir  date NOT NULL,
	
	PRIMARY KEY (id_director)
	);


# Creación de la tabla Pelicula 
CREATE TABLE  Pelicula ( 
	id_pelicula int auto_increment, 
	nombre_pel varchar (30) NOT NULL , 
	fech_estreno date NOT NULL , 
	costo_total decimal NOT NULL,
	PRIMARY KEY (id_pelicula)
	
	);
# Creación de la tabla intermedia Actua_en
CREATE TABLE Actua_en (
	id_actor int  NOT NULL,
	id_pelicula int NOT NULL,
	PRIMARY KEY (id_actor, id_pelicula),
	FOREIGN KEY (id_actor) references Actor(id_actor),
	FOREIGN KEY (id_pelicula) references Pelicula (id_pelicula)
	
	);

#Creación de la tabla intermedia es_dirigida
CREATE TABLE Es_dirigida (
	id_director int NOT NULL,
	id_pelicula int NOT NULL,
	PRIMARY KEY (id_director, id_pelicula),

	FOREIGN KEY (id_director) REFERENCES Director(id_director),
	FOREIGN KEY (id_pelicula) REFERENCES Pelicula(id_pelicula)
	
	);
 


	

