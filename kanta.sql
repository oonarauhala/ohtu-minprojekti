DROP TABLE IF EXISTS Kirjavinkit;
DROP TABLE IF EXISTS Blogivinkit;
DROP TABLE IF EXISTS Videovinkit;
DROP TABLE IF EXISTS Podcastvinkit;

CREATE TABLE Kirjavinkit (
    id INTEGER PRIMARY KEY,
    Otsikko TEXT,
    kirjoittaja TEXT,
    isbn TEXT,
    kommentti TEXT,
    luettu text default "ei"
);

CREATE TABLE Blogivinkit (
    id INTEGET PRIMARY KEY,
    nimi TEXT,
    kirjoittaja TEXT,
    url TEXT,
    kommentti TEXT,
    luettu text default "ei"
);

CREATE TABLE Videovinkit (
    id INTEGER PRIMARY KEY,
    nimi TEXT,
    tekija TEXT,
    url TEXT,
    kommentti TEXT,
    luettu text default "ei"
);

CREATE TABLE Podcastvinkit (
    id INTEGER PRIMARY KEY,
    nimi TEXT,
    tekija TEXT,
    jakson_nimi TEXT,
    kommentti TEXT,
    luettu text default "ei"
);

