import unittest
from unittest.mock import patch, MagicMock
from DomNom.server import Server

class TestServer(unittest.TestCase):
    @patch('socket.socket')
    def test_server_start(self, mock_socket):
        mock_instance = MagicMock()
        mock_socket.return_value = mock_instance

        # Mock accept to return a tuple with a mock client socket and address
        mock_instance.accept.return_value = (MagicMock(), ('127.0.0.1', 12345))
        mock_instance.recv.return_value = b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
        mock_instance.sendall = MagicMock()

        @self.server.router.route("/", methods=['GET'])
        def home():
            return "HTTP/1.1 200 OK\n\nWelcome to the Home Page!"

        with patch('builtins.print') as mocked_print:
            self.server.start()
            mocked_print.assert_called_with('Server running on http://127.0.0.1:8080')

        # Verify that sendall was called with the correct response
        mock_instance.sendall.assert_called_with(b"HTTP/1.1 200 OK\n\nWelcome to the Home Page!")

    def setUp(self):
        self.server = Server()

    def test_handle_request(self):
        @self.server.router.route("/", methods=['GET'])
        def home():
            return "HTTP/1.1 200 OK\n\nWelcome to the Home Page!"

        request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
        response = self.server.router.handle(request)
        self.assertEqual(response, "HTTP/1.1 200 OK\n\nWelcome to the Home Page!")

if __name__ == '__main__':
    unittest.main()
