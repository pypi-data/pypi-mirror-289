import socket

class Router:
    def __init__(self):
        self.routes = {}

    def route(self, path, methods=['GET']):
        def decorator(func):
            self.routes[path] = {'methods': methods, 'func': func}
            return func
        return decorator

    def handle(self, request):
        try:
            request_line = request.split("\r\n")[0]
            method, path, _ = request_line.split(" ")

            route = self.routes.get(path, {})
            if method in route.get('methods', []):
                return route.get('func')()
            else:
                return "HTTP/1.1 405 Method Not Allowed\n\n"
        except Exception:
            return "HTTP/1.1 400 Bad Request\n\n"

class Server:
    def __init__(self, host='127.0.0.1', port=8080):
        self.host = host
        self.port = port
        self.router = Router()

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(1)
        print(f'Server running on http://{self.host}:{self.port}')

        while True:
            client, addr = s.accept()
            with client:
                request = client.recv(1024).decode('utf-8')
                response = self.router.handle(request)
                client.sendall(response.encode('utf-8'))
