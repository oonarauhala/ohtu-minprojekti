CREATE TABLE Kirjavinkit (
    id INTEGER PRIMARY KEY,
    Otsikko TEXT,
    kirjoittaja TEXT,
    isbn TEXT,
    kommentti TEXT
);

CREATE TABLE Blogivinkit (
    id INTEGET PRIMARY KEY,
    nimi TEXT,
    kirjoittaja TEXT,
    url TEXT,
    kommentti TEXT
);

CREATE TABLE Videovinkki (
    id INTEGER PRIMARY KEY,
    nimi TEXT,
    tekija TEXT,
    url TEXT,
    kommentti TEXT
);

CREATE TABLE Podcastvinkki (
    id INTEGER PRIMARY KEY,
    nimi TEXT,
    tekija TEXT,
    jakson_nimi TEXT,
    kommentti TEXT
);

