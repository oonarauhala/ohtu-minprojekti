import sqlite3 as sql

def get_kirjavinkit():
    con = sql.connect("tietokanta.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from Kirjavinkit")

    rows = cur.fetchall()
    return rows

def new_kirjavinkki(otsikko, kirjoittaja, isbn, kommentti):
    komento = "INSERT INTO Kirjavinkit (Otsikko, kirjoittaja, isbn, kommentti) VALUES (:otsikko, :kirjoittaja, :isbn, :kommentti)"
    con = sql.connect("tietokanta.db")
    con.row_factory = sql.Row
    con.isolation_level = None
    cur = con.cursor()
    try:
        cur.execute(komento, {"otsikko":otsikko, "kirjoittaja":kirjoittaja, "isbn":isbn, "kommentti":kommentti})
    except:
        return False
    return True

def get_blogivinkit():
    con = sql.connect("tietokanta.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from Blogivinkit")

    rows = cur.fetchall()
    return rows

def new_blogivinkki(nimi, kirjoittaja, url, kommentti):
    komento = "INSERT INTO Blogivinkit (nimi, kirjoittaja, url, kommentti) VALUES (:nimi, :kirjoittaja, :url, :kommentti)"
    con = sql.connect("tietokanta.db")
    con.row_factory = sql.Row
    con.isolation_level = None
    cur = con.cursor()
    try:
        cur.execute(komento, {"nimi":nimi, "kirjoittaja":kirjoittaja, "url":url, "kommentti":kommentti})
    except:
        return False
    return True

def get_podcastvinkit():
    con = sql.connect("tietokanta.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from Podcastvinkit")

    rows = cur.fetchall()
    return rows

def new_podcastvinkki(nimi, tekija, jakson_nimi, kommentti):
    komento = "INSERT INTO Podcastvinkit (nimi, tekija, jakson_nimi, kommentti) VALUES (:nimi, :tekija, :jakson_nimi, :kommentti)"
    con = sql.connect("tietokanta.db")
    con.row_factory = sql.Row
    con.isolation_level = None
    cur = con.cursor()
    try:
        cur.execute(komento, {"nimi":nimi, "tekija":tekija, "jakson_nimi":jakson_nimi, "kommentti":kommentti})
    except:
        return False
    return True

def get_videovinkit():
    con = sql.connect("tietokanta.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from Videovinkit")

    rows = cur.fetchall()
    return rows

def new_videovinkki(nimi, tekija, url, kommentti):
    komento = "INSERT INTO Videovinkit (nimi, tekija, url, kommentti) VALUES (:nimi, :tekija, :url, :kommentti)"
    con = sql.connect("tietokanta.db")
    con.row_factory = sql.Row
    con.isolation_level = None
    cur = con.cursor()
    try:
        cur.execute(komento, {"nimi":nimi, "tekija":tekija, "url":url, "kommentti":kommentti})
    except:
        return False
    return True
