# Simple Web Server

A simple web server package built using Python's `http.server` module. This library provides an easy way to serve files and handle HTTP requests with custom routing.

## Features

- Lightweight and easy to use.
- Modular route management through dynamic import of modules.
- Threading support for handling multiple requests concurrently.
- Custom request handlers for specific endpoints.

## Installation

You can install the package via `pip`:

```bash
pip install simplewebserver
```

## Usage
```python
from simplewebserver import SimpleWebServer
import my_routes  # Your custom route module

# Create a new server instance
server = SimpleWebServer()

# Include your custom route module
server.include_routes_module(my_routes)

# Start the server on port 5000
server.start(port=5000)
```

```
# my_routes.py
from simplewebserver import route, Request, Response

@route('/hello')
def hello_world(request:Request):
    return Response({'message': 'Hello, World!'})

```