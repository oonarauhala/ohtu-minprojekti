import unittest
from db_functions import DBFunctions

class TestApp(unittest.TestCase):
    def setUp(self):
        self.db_functions = DBFunctions(db="testit.db")
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

    def test_get_blogivinkit_tyhjä(self):
        result = list(self.db_functions.get_blogivinkit())
        self.assertEqual(len(result), 0)

    def test_get_podcastvinkit_tyhjä(self):
        result = list(self.db_functions.get_podcastvinkit())
        self.assertEqual(len(result), 0)
