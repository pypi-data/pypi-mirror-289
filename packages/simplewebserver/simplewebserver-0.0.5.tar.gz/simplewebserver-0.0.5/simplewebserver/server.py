from http.server import HTTPServer
import importlib
import logging
import os
from socketserver import ThreadingMixIn
import threading
import webbrowser

from simplewebserver.handler import RequestHandler
from simplewebserver.utils import get_exception_detail

logger = logging.getLogger()

class SimpleWebServer:
    def __init__(self):
        self._httpd = None
        self._server_thread = None
        self._routes_modules = []

    def include_routes_module(self, module):
        self._routes_modules.append(module.__name__)

    def start(self, port = None):
        try:
            server_address = ('', port)
            self._httpd = ThreadedHTTPServer(server_address, RequestHandler, routes_modules = self._routes_modules)
            self._server_thread = threading.current_thread()
            print('Server running on port', port)
            webbrowser.open('http://localhost:' + str(port))
            self._httpd.serve_forever()
        except KeyboardInterrupt:
            print("Ctrl+C pressed. Exiting...")
            os._exit(130)
        except Exception as e:
            logger.error(get_exception_detail(e))

    def stop(self):
        if self._httpd and self._server_thread and self._server_thread.is_alive():
            print("Shutting down server gracefully...")
            self._httpd.shutdown()

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    def __init__(self, *args, **kwargs) -> None:
        self._routes_modules = kwargs.get('routes_modules', [])
        self._routes_imported = False
        del kwargs['routes_modules']
        super().__init__(*args, **kwargs)
    
    def _import_routes_modules(self):
        for module_name in self._routes_modules:
            importlib.import_module(module_name)
        self._routes_imported = True