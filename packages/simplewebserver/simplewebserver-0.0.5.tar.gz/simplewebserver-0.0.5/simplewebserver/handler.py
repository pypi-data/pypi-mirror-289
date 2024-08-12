from dataclasses import dataclass
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
import json
import logging
import types
from typing import Optional
from urllib.parse import parse_qs, urlparse
from simplewebserver.decorator import routes, sort_route
from simplewebserver.utils import get_exception_detail
from simplewebserver.utils import CustomEncoder

logger = logging.getLogger()

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_request('GET')

    def do_POST(self):
        self.handle_request('POST')

    def do_PUT(self):
        self.handle_request('PUT')

    def do_DELETE(self):
        self.handle_request('DELETE')

    def handle_request(self, method):
        try:
            if not self.server._routes_imported:
                self.server._import_routes_modules()
                sorted_routes = sorted(routes, key=sort_route)

            parsed_url = urlparse(self.path)
            path = parsed_url.path
            query_params = parse_qs(parsed_url.query)
            headers = self.headers

            content_length = int(self.headers['Content-Length'] or '0')
            body:bytes = self.rfile.read(content_length).decode() if content_length > 0 else None

            path_matched = False
            method_matched = False
            handler = None

            for route in sorted_routes:
                if route.get('method') == method:
                    method_matched = True

                if route.get('match_type') == 'exact' and route.get('path') == path:
                    path_matched = True
                
                if route.get('match_type') == 'prefix' and path.startswith(route.get('path')):
                    path_matched = True

                if method_matched and path_matched:
                    handler = route.get('func')
                    break

            response = None
            if method_matched and path_matched:
                response = handler(Request(
                    path = path,
                    query_params = query_params,
                    body = body,
                    headers = headers
                ))

                if response is None:
                    response = Response(status_code=200)
                if isinstance(response, dict) or isinstance(response, list) or isinstance(response, str):
                    response = Response(body = response, status_code=200)
            elif path_matched:
                response = Response(headers={"Content-type":"text/plain"}, body = HTTPStatus(405).phrase, status_code=405)
            else:
                response = Response(headers={"Content-type":"text/plain"}, body = HTTPStatus(404).phrase, status_code=404)

            self.send_response(response.status_code)
            for hn, hv in response.headers.items():
                self.send_header(hn,hv)
            self.end_headers()

            if isinstance(response.body, types.GeneratorType):
                gen = response.body
                for content in gen:
                    self.wfile.write(content.encode())
                    self.wfile.flush()
            elif isinstance(response.body, str):
                str_body = response.body
                self.wfile.write(str_body.encode())
            elif isinstance(response.body, bytes):
                bytes_body = response.body
                self.wfile.write(bytes_body)
            elif isinstance(response.body, dict) or isinstance(response.body, list):
                json_body = json.dumps(response.body, cls=CustomEncoder)
                self.wfile.write(json_body.encode())

        except ConnectionAbortedError as ca_e:
            logger.error(get_exception_detail(ca_e))

@dataclass
class Request:
    path: str
    query_params: Optional[dict] = None
    body: Optional[any] = None
    headers: Optional[dict] = None


class Response:
    headers: Optional[dict] = None
    body: Optional[any] = None
    status_code: int = 200

    def __init__(self, body = None, **kwargs):
        self.body = body
        self.headers = {
            "Content-type":"application/json"
        }
        self.status_code = 200
        for k, v in kwargs.items():
            if k == 'headers':
                v = getattr(self, 'headers', {}) | v
            setattr(self, k, v)