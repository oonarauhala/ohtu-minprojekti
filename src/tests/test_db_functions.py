import unittest
from db_functions import DBFunctions
from werkzeug.security import generate_password_hash


class TestApp(unittest.TestCase):
    def setUp(self):
        self.db_functions = DBFunctions(db="testit.db")
        self.db_functions2 = DBFunctions(db="feikki.db")
        self.db_functions.tyhjenna()

    def test_tyhjenna(self):
        self.db_functions.new_kirjavinkki("Testikirja", "Testaaja", "1", "Lue tämä")
        self.db_functions.tyhjenna()
        result = list(self.db_functions.get_kirjavinkit())
        self.assertEqual(len(result), 0)

    def test_get_kirjavinkit_tyhjä(self):
        result = list(self.db_functions.get_kirjavinkit())
        self.assertEqual(len(result), 0)

    def test_new_kirjavinkki(self):
        self.db_functions.new_kirjavinkki("Testikirja", "Testaaja", "1", "Lue tämä")
        result = list(self.db_functions.get_kirjavinkit())
        self.assertEqual(len(result), 1)

    def test_new_kirjavinkki_ei_tietokantaa(self):
        result = self.db_functions2.new_kirjavinkki("Testi", "Testaaja", "1", "Lue")
        self.assertFalse(result)

    def test_get_blogivinkit_tyhjä(self):
        result = list(self.db_functions.get_blogivinkit())
        self.assertEqual(len(result), 0)

    def test_new_blogivinkki(self):
        self.db_functions.new_blogivinkki(
            "Testiblogi", "Testaaja", "www.com", "Hyvä blogi"
        )
        result = list(self.db_functions.get_blogivinkit())
        self.assertEqual(len(result), 1)

    def test_new_blogivinkki_ei_tietokantaa(self):
        result = self.db_functions2.new_blogivinkki(
            "Testi", "Testaaja", "www.com", "Lue"
        )
        self.assertFalse(result)

    def test_get_podcastvinkit_tyhjä(self):
        result = list(self.db_functions.get_podcastvinkit())
        self.assertEqual(len(result), 0)

    def test_new_podcastvinkki(self):
        self.db_functions.new_podcastvinkki(
            "Testipodcast", "Testaaja", "Testijakso", "Hyvä podcast"
        )
        result = list(self.db_functions.get_podcastvinkit())
        self.assertEqual(len(result), 1)

    def test_new_podcastvinkki_ei_tietokantaa(self):
        result = self.db_functions2.new_podcastvinkki("Testi", "Testaaja", "1", "Lue")
        self.assertFalse(result)

    def test_get_videovinkit_tyhjä(self):
        result = list(self.db_functions.get_videovinkit())
        self.assertEqual(len(result), 0)

    def test_new_videovinkki(self):
        self.db_functions.new_videovinkki(
            "Testivideo", "Testaaja", "www.com", "Hyvä video"
        )
        result = list(self.db_functions.get_videovinkit())
        self.assertEqual(len(result), 1)

    def test_new_videovinkki_ei_tietokantaa(self):
        result = self.db_functions2.new_videovinkki(
            "Testi", "Testaaja", "www.com", "Hyvä video"
        )
        self.assertFalse(result)

    def test_kirjavinkin_merkinta_luetuksi(self):
        self.db_functions.new_kirjavinkki("Testikirja", "Testaaja", "1", "Lue tämä")
        self.db_functions.merkitse_kirja_luetuksi("1")
        result = self.db_functions.get_kirjavinkit()[0]["luettu"]
        self.assertEqual(result, "kyllä")

    def test_blogivinkin_merkinta_luetuksi(self):
        self.db_functions.new_blogivinkki("Testi", "Testaaja", "testi.fi", "lue")
        self.db_functions.merkitse_blogi_luetuksi("1")
        result = self.db_functions.get_blogivinkit()[0]["luettu"]
        self.assertEqual(result, "kyllä")

    def test_podcastvinkin_merkinta_kuunnelluksi(self):
        self.db_functions.new_podcastvinkki("Testicasti", "Testaaja", "jakso 1", "tää on hyvä")
        self.db_functions.merkitse_podcast_kuunnelluksi("1")
        result = self.db_functions.get_podcastvinkit()[0]["luettu"]
        self.assertEqual(result, "kyllä")

    def test_videovinkin_merkinta_katsotuksi(self):
        self.db_functions.new_videovinkki("Video", "Kuvaaja", "video.fi", "kato tää")
        self.db_functions.merkitse_video_katsotuksi("1")
        result = self.db_functions.get_videovinkit()[0]["luettu"]
        self.assertEqual(result, "kyllä")

    def test_merkitse_kirjavinkki_luetuksi_database_error(self):
        result = self.db_functions2.merkitse_kirja_luetuksi("1")
        self.assertFalse(result)

    def test_merkitse_blogivinkki_luetuksei_database_error(self):
        result = self.db_functions2.merkitse_blogi_luetuksi("1")
        self.assertFalse(result)

    def test_merkitse_podcastvinkki_luetuksei_database_error(self):
        result = self.db_functions2.merkitse_podcast_kuunnelluksi("1")
        self.assertFalse(result)

    def test_merkitse_videovinkki_luetuksei_database_error(self):
        result = self.db_functions2.merkitse_video_katsotuksi("1")
        self.assertFalse(result)

    def test_get_kayttajat(self):
        result = list(self.db_functions.get_kayttajat())
        self.assertEqual(len(result), 1)

    def test_uusi_kayttaja_onnistuneesti(self):
        self.db_functions.uusi_kayttaja("matti", generate_password_hash("kissa123"))
        result = list(self.db_functions.get_kayttajat())
        self.assertEqual(len(result), 1)

    def test_uusi_kayttaja_ei_onnistuneesti(self):
        self.db_functions.uusi_kayttaja("matti", generate_password_hash("kissa123"))
        self.db_functions.uusi_kayttaja("matti", generate_password_hash("koira123"))
        result = list(self.db_functions.get_kayttajat())
        self.assertEqual(len(result), 1)


