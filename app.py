from twisted.internet import reactor

from api_socket import server as sockets_server
from api_http import server as http_server
from settings import SOCKET_API_PORT, HTTP_API_PORT


if __name__ == '__main__':
    reactor.listenTCP(SOCKET_API_PORT, sockets_server)
    reactor.listenTCP(HTTP_API_PORT, http_server)
    reactor.run()
