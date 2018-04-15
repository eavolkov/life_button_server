class HttpApiError(Exception):
    pass


class UnknownViewError(HttpApiError):
    def __init__(self, path):
        super().__init__(f'Unknown view: {path}')
