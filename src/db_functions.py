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
