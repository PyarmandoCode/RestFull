CREATE TABLE GRUPOS(
CODGRUPO SERIAL PRIMARY KEY,
	NOMBRE_GRUPO VARCHAR(100),
	DESCRIPCION_GRUPO TEXT,
	ESTADO BOOL
);

INSERT INTO GRUPOS(nombre_grupo,descripcion_grupo,estado) 
values('GRUPO','DESCRIPCION DE PRUEBA',True);

select * from grupos;