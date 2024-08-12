routes = []

def route(path, method):
    '''
    path / method combination should be unique
    '''
    def wrapper(func):
        routes.append({
            'path':path,
            'func':func,
            'method':method
        })
        return func
    return wrapper