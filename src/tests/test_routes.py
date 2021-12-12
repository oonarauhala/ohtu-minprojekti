import unittest
from unittest import mock
from app import app
from os import environ


class TestRoutes(unittest.TestCase):
    @mock.patch.dict(environ, {"SECRET_KEY": "ASDF"})
    def setUp(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        app.config["SECRET_KEY"] = environ["SECRET_KEY"]
        self.app = app.test_client()
        with self.app.session_transaction() as session:
            session["user_id"] = 2

    def test_list_page(self):
        response = self.app.get("/list")
        self.assertEqual(response.status_code, 200)

    def test_new_book_page(self):
        response = self.app.get("/new_book")
        self.assertEqual(response.status_code, 200)

    def test_new_blog_page(self):
        response = self.app.get("/new_blog")
        self.assertEqual(response.status_code, 200)

    def test_new_podcast_page(self):
        response = self.app.get("/new_podcast")
        self.assertEqual(response.status_code, 200)

    def test_new_video_page(self):
        response = self.app.get("/new_video")
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.app.get("/register")
        self.assertEqual(response.status_code, 200)
