import re
from typing import Tuple, Callable, Any

from twisted.internet import protocol

from . import exc
from .commands import commands


class Protocol(protocol.Protocol):
    MSG_REGEX = re.compile('^cmd_(?P<cmd>\S+) ?(?P<data>.+)?$')

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.device_id = None

    def dataReceived(self, data: bytes):
        cmd, cmd_data = self._parse_cmd(data.decode())
        self._get_handler(cmd)(self, cmd_data)

    def _get_handler(self, cmd_name: str) -> Callable[[str], Any]:
        try:
            return commands[cmd_name]
        except KeyError as e:
            raise exc.UnknownCommandError(cmd_name)

    def _parse_cmd(self, cmd_str: str) -> Tuple[str, str]:
        m = self.MSG_REGEX.match(cmd_str.strip())

        if m is None:
            raise exc.CommandFormatError()

        return m.group('cmd'), m.group('data')


class ServerFactory(protocol.Factory):
    protocol = Protocol


server = ServerFactory()
