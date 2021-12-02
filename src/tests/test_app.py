import unittest
from flask import Flask
import sqlite3 as sql

class TestApp(unittest.TestCase):
    def test_eka_testi(self):
        self.assertEqual(1, 1)
