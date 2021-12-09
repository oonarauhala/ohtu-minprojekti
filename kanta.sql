DROP TABLE IF EXISTS Kirjavinkit;
DROP TABLE IF EXISTS Blogivinkit;
DROP TABLE IF EXISTS Videovinkit;
DROP TABLE IF EXISTS Podcastvinkit;
DROP TABLE IF EXISTS Kayttajat;

CREATE TABLE Kirjavinkit (
    id INTEGER PRIMARY KEY,
    Otsikko TEXT,
    kirjoittaja TEXT,
    isbn TEXT,
    kommentti TEXT,
    luettu text default "ei",
    kayttaja_id INTEGER REFERENCES Kayttajat (id)
);

CREATE TABLE Blogivinkit (
    id INTEGER PRIMARY KEY,
    nimi TEXT,
    kirjoittaja TEXT,
    url TEXT,
    kommentti TEXT,
    luettu text default "ei",
    kayttaja_id INTEGER REFERENCES Kayttajat (id)
);

CREATE TABLE Videovinkit (
    id INTEGER PRIMARY KEY,
    nimi TEXT,
    tekija TEXT,
    url TEXT,
    kommentti TEXT,
    luettu text default "ei",
    kayttaja_id INTEGER REFERENCES Kayttajat (id)
);

CREATE TABLE Podcastvinkit (
    id INTEGER PRIMARY KEY,
    nimi TEXT,
    tekija TEXT,
    jakson_nimi TEXT,
    kommentti TEXT,
    luettu text default "ei",
    kayttaja_id INTEGER REFERENCES Kayttajat (id)
);

CREATE TABLE Kayttajat (
    id INTEGER PRIMARY KEY,
    tunnus TEXT UNIQUE,
    salasana TEXT
);
