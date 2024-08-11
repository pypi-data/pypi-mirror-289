# DomNom/router.py
class Router:
    def __init__(self):
        self.routes = {}

    def add_route(self, path, handler, methods=['GET']):
        if path not in self.routes:
            self.routes[path] = {}
        for method in methods:
            self.routes[path][method.upper()] = handler

    def get_handler(self, path, method):
        return self.routes.get(path, {}).get(method, self.default_handler)

    def default_handler(self, *args, **kwargs):
        return "HTTP/1.1 404 Not Found\n\nThe requested URL was not found on this server."

    def route(self, path, methods=['GET']):
        def wrapper(handler):
            self.add_route(path, handler, methods)
            return handler
        return wrapper
