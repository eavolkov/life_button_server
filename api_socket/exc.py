from .commands import commands


class SocketApiError(Exception):
    pass


class UnknownCommandError(SocketApiError):
    def __init__(self, cmd_name: str) -> None:
        super().__init__(f'Unknown command: {cmd_name} (supported: {", ".join(commands.keys())})')


class CommandFormatError(SocketApiError):
    def __init__(self) -> None:
        super().__init___('Wrong command format. Must be: cmd_NAME [param1 [param2 ... ]]')


class MissedDataError(SocketApiError):
    def __init__(self) -> None:
        super().__init__('This command required extra data (params)')


class DataNotSupportedError(SocketApiError):
    def __init__(self) -> None:
        super().__init__('This command doesn\'t support data (params)')


class MissedDeviceIdError(SocketApiError):
    def __init__(self) -> None:
        super().__init__('This command required device_id value (call cmd_id and try again)')
