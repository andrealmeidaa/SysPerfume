CREATE TABLE "Essencia_Perfume" (
	"id_perfume"	INTEGER,
	"id_essencia"	INTEGER,
	PRIMARY KEY("id_perfume","id_essencia"),
	FOREIGN KEY("id_perfume") REFERENCES "Perfumes"("id")
);
CREATE TABLE "Essencias" (
	"id"	INTEGER,
	"nome"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE "Fixacoes" (
	"id"	INTEGER,
	"nome"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE "Marcas" (
	"id"	INTEGER,
	"nome"	TEXT UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE "Perfumes" (
	"id"	INTEGER,
	"nome"	TEXT,
	"quantidade"	INTEGER,
	"id_volume"	INTEGER,
	"id_marca"	INTEGER,
	"id_fixacao"	INTEGER,
	FOREIGN KEY("id_marca") REFERENCES "Marcas"("id"),
	FOREIGN KEY("id_fixacao") REFERENCES "Fixacoes"("id"),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_volume") REFERENCES "Volumes"("id")
)
CREATE TABLE "Volumes" (
	"id"	INTEGER,
	"nome"	TEXT UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE sqlite_sequence(name,seq)