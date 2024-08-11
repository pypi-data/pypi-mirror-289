import unittest
from DomNom.router import Router

class TestRouter(unittest.TestCase):

    def setUp(self):
        self.router = Router()

    def test_add_and_get_route(self):
        @self.router.route("/test", methods=['GET'])
        def test_handler():
            return "Test Handler"
        
        handler = self.router.get_handler("/test", "GET")
        self.assertEqual(handler(), "Test Handler")

    def test_default_handler(self):
        handler = self.router.get_handler("/non-existent", "GET")
        self.assertEqual(handler(), "HTTP/1.1 404 Not Found\n\nThe requested URL was not found on this server.")

    def test_http_methods(self):
        @self.router.route("/test_post", methods=['POST'])
        def test_post_handler():
            return "POST Handler"

        get_handler = self.router.get_handler("/test_post", "GET")
        post_handler = self.router.get_handler("/test_post", "POST")
        
        self.assertEqual(get_handler(), "HTTP/1.1 404 Not Found\n\nThe requested URL was not found on this server.")
        self.assertEqual(post_handler(), "POST Handler")

if __name__ == "__main__":
    unittest.main()
