import sqlite3 as sql
from sqlite3.dbapi2 import OperationalError, IntegrityError


class DBFunctions:
    def __init__(self, db="tietokanta.db"):
        self.database = db

    def get_kirjavinkit(self, id):
        con = sql.connect(self.database)
        con.row_factory = sql.Row
        con.isolation_level = None

        cur = con.cursor()
        komento = "select * from Kirjavinkit where kayttaja_id=:id"

        rows = cur.execute(komento, {"id":id}).fetchall()

        return rows

    def new_kirjavinkki(self, otsikko, kirjoittaja, isbn, kommentti, kayttaja_id):
        komento = "INSERT INTO Kirjavinkit (Otsikko, kirjoittaja, isbn, kommentti, kayttaja_id) \
            VALUES (:otsikko, :kirjoittaja, :isbn, :kommentti, :kayttaja_id)"
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
                    "kayttaja_id": kayttaja_id
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
        cur.execute("DELETE FROM Kayttajat")

    def merkitse_kirja_luetuksi(self, book_id):
        komento = "UPDATE Kirjavinkit SET luettu = 'kyllä' WHERE id = :book_id;"
        con = sql.connect(self.database)
        con.isolation_level = None
        cur = con.cursor()
        try:
            cur.execute(komento, {"book_id": book_id})
        except OperationalError:
            return False
        return True

    def merkitse_blogi_luetuksi(self,blog_id):
        komento = "UPDATE Blogivinkit SET luettu = 'kyllä' WHERE id = :blog_id;"
        con = sql.connect(self.database)
        con.isolation_level = None
        cur = con.cursor()
        try:
            cur.execute(komento, {"blog_id": blog_id})
        except OperationalError:
            return False
        return True

    def merkitse_podcast_kuunnelluksi(self, pod_id):
        komento = "UPDATE Podcastvinkit SET luettu = 'kyllä' WHERE id = :pod_id;"
        con = sql.connect(self.database)
        con.isolation_level = None
        cur = con.cursor()
        try:
            cur.execute(komento, {"pod_id": pod_id})
        except OperationalError:
            return False
        return True

    def merkitse_video_katsotuksi(self, video_id):
        komento = "UPDATE Videovinkit SET luettu = 'kyllä' WHERE id = :video_id;"
        con = sql.connect(self.database)
        con.isolation_level = None
        cur = con.cursor()
        try:
            cur.execute(komento, {"video_id": video_id})
        except OperationalError:
            return False
        return True

    def get_kayttajat(self):
        con = sql.connect(self.database)
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("select * from Kayttajat")

        rows = cur.fetchall()
        return rows


    def uusi_kayttaja(self, tunnus, salasana):
        komento = "INSERT INTO Kayttajat (tunnus, salasana) \
            VALUES (:tunnus, :salasana)"
        con = sql.connect(self.database)
        con.row_factory = sql.Row
        con.isolation_level = None
        cur = con.cursor()
        try:
            cur.execute(
                komento,
                {
                    "tunnus": tunnus,
                    "salasana": salasana
                },
            )
        except IntegrityError:
            return False
        return True

    def etsi_kayttaja(self, username):
        komento =   "SELECT * FROM Kayttajat WHERE tunnus=:username"
        con = sql.connect(self.database)
        con.row_factory = sql.Row
        con.isolation_level = None
        cur = con.cursor()
        user = cur.execute(komento, {"username":username}).fetchone()
        return user

    def get_kayttaja_id(self, tunnus):
        komento =   "SELECT id FROM Kayttajat WHERE tunnus=:tunnus"
        con = sql.connect(self.database)
        con.row_factory = sql.Row
        con.isolation_level = None
        cur = con.cursor()
        id = cur.execute(komento, {"tunnus":tunnus}).fetchone()[0]
        return id

