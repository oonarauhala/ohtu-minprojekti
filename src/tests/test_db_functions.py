import unittest
from db_functions import DBFunctions


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
