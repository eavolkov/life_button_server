import re
import datetime
from functools import wraps

from db import Device
from . import exc


LOCATION_REGEX = re.compile('(?P<lat>\d+\.\d+) (?P<lng>\d+\.\d+)')

commands = {}


def cmd_handler(name, with_data=True, requires_device_id=False, with_ack=True):
    def decorator(f):
        @wraps(f)
        def wrapper(protocol, data=None):
            if with_data and not data:
                raise exc.MissedDataError()
            elif not with_data and data:
                raise exc.DataNotSupportedError()

            if requires_device_id and not protocol.device_id:
                raise exc.MissedDeviceIdError()

            f(protocol, data)

            if with_ack:
                protocol.transport.write(b'ack\n')

        commands[name] = wrapper
        return wrapper
    return decorator


@cmd_handler('id')
def cmd_id(protocol, data: str):
    protocol.device_id = int(data)


@cmd_handler('location', requires_device_id=True)
def cmd_location(protocol, data: str):
    m = LOCATION_REGEX.match(data)
    lat = float(m.group('lat'))
    lng = float(m.group('lng'))

    Device.objects(id=protocol.device_id) \
        .update(
            add_to_set__locations=[{'lat': lat, 'lng': lng}],
            upsert=True
        )


@cmd_handler('keepalive', with_data=False, requires_device_id=True)
def cmd_keepalive(protocol, data: None):
    Device.objects(id=protocol.device_id) \
        .update(
            add_to_set__keepalive=[{'datetime': datetime.datetime.now()}],
            upsert=True
        )
