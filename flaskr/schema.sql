
DROP TABLE IF EXISTS Groupe;

CREATE TABLE Groupe (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nom TEXT,
	description TEXT
);

INSERT INTO Groupe(nom, description) VALUES("Silverchair", "the best grunge");