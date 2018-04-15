from twisted.web.resource import Resource
from twisted.web.server import Site

from . import exc
from .views import views


class Root(Resource):
    isLeaf = True

    def render_GET(self, request):
        path = request.path.decode()
        handler = None

        for pattern, f in views.items():
            m = pattern.match(path)

            if m is not None:
                handler = f
                kwargs = m.groupdict()
                break

        if handler is None:
            raise exc.UnknownViewError(path)

        resp = handler(request, **kwargs)

        if isinstance(resp, str):
            resp = resp.encode()

        return resp


server = Site(Root())
