import unittest
from app import app


class TestRoutes(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        self.app = app.test_client()

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
