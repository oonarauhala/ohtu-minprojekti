import sqlite3 as sql
from sqlite3.dbapi2 import OperationalError


class DBFunctions:
    def __init__(self, db="tietokanta.db"):
        self.database = db

    def get_kirjavinkit(self):
        con = sql.connect(self.database)
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("select * from Kirjavinkit")

        rows = cur.fetchall()
        return rows

    def new_kirjavinkki(self, otsikko, kirjoittaja, isbn, kommentti):
        komento = "INSERT INTO Kirjavinkit (Otsikko, kirjoittaja, isbn, kommentti) \
            VALUES (:otsikko, :kirjoittaja, :isbn, :kommentti)"
        con = sql.connect(self.database)
        con.row_factory = sql.Row
        con.isolation_level = None
        cur = con.cursor()
        try:
            cur.execute(
                komento,
                {
                    "otsikko": otsikko,
                    "kirjoittaja": kirjoittaja,
                    "isbn": isbn,
                    "kommentti": kommentti,
                },
            )
        except OperationalError:
            return False
        return True

    def get_blogivinkit(self):
        con = sql.connect(self.database)
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("select * from Blogivinkit")

        rows = cur.fetchall()
        return rows

    def new_blogivinkki(self, nimi, kirjoittaja, url, kommentti):
        komento = "INSERT INTO Blogivinkit (nimi, kirjoittaja, url, kommentti) \
            VALUES (:nimi, :kirjoittaja, :url, :kommentti)"
        con = sql.connect(self.database)
        con.row_factory = sql.Row
        con.isolation_level = None
        cur = con.cursor()
        try:
            cur.execute(
                komento,
                {
                    "nimi": nimi,
                    "kirjoittaja": kirjoittaja,
                    "url": url,
                    "kommentti": kommentti,
                },
            )
        except OperationalError:
            return False
        return True

    def get_podcastvinkit(self):
        con = sql.connect(self.database)
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("select * from Podcastvinkit")

        rows = cur.fetchall()
        return rows

    def new_podcastvinkki(self, nimi, tekija, jakson_nimi, kommentti):
        komento = "INSERT INTO Podcastvinkit (nimi, tekija, jakson_nimi, kommentti) \
            VALUES (:nimi, :tekija, :jakson_nimi, :kommentti)"
        con = sql.connect(self.database)
        con.row_factory = sql.Row
        con.isolation_level = None
        cur = con.cursor()
        try:
            cur.execute(
                komento,
                {
                    "nimi": nimi,
                    "tekija": tekija,
                    "jakson_nimi": jakson_nimi,
                    "kommentti": kommentti,
                },
            )
        except OperationalError:
            return False
        return True

    def get_videovinkit(self):
        con = sql.connect(self.database)
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("select * from Videovinkit")

        rows = cur.fetchall()
        return rows

    def new_videovinkki(self, nimi, tekija, url, kommentti):
        komento = "INSERT INTO Videovinkit (nimi, tekija, url, kommentti) \
            VALUES (:nimi, :tekija, :url, :kommentti)"
        con = sql.connect(self.database)
        con.row_factory = sql.Row
        con.isolation_level = None
        cur = con.cursor()
        try:
            cur.execute(
                komento,
                {"nimi": nimi, "tekija": tekija, "url": url, "kommentti": kommentti},
            )
        except OperationalError:
            return False
        return True

    def tyhjenna(self):
        con = sql.connect(self.database)
        con.isolation_level = None
        cur = con.cursor()
        cur.execute("DELETE FROM Kirjavinkit")
        cur.execute("DELETE FROM Blogivinkit")
        cur.execute("DELETE FROM Podcastvinkit")
        cur.execute("DELETE FROM Videovinkit")

    def merkitse_kirja_luetuksi(self, isbn):
        komento = "UPDATE Kirjavinkit SET luettu = 'kyllä' WHERE isbn = :isbn;"
        con = sql.connect(self.database)
        con.isolation_level = None
        cur = con.cursor()
        try:
            cur.execute(komento, {"isbn": isbn})
        except OperationalError:
            return False
        return True
