import unittest
from flask import Flask
import sqlite3 as sql
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING']=True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
