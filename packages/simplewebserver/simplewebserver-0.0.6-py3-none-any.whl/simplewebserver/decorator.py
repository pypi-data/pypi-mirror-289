from typing import Literal


routes = []

def route(path, method, match_type:Literal['exact','prefix'] = 'exact'):
    '''
    path / method combination should be unique
    '''
    def wrapper(func):
        routes.append({
            'path':path,
            'func':func,
            'method':method,
            'match_type':match_type
        })
        return func
    return wrapper

def sort_route(route):
    path = route.get('path')
    segments = path.strip('/').split('/')
    return (-len(segments), -len(path))