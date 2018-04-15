import re

from db import Device


views = {}


def view(regex: str):
    def decorator(f):
        views[re.compile(regex)] = f
        return f
    return decorator


@view('/device/(?P<device_id>\d+)/locations')
def get_locations(request, device_id: int):
    device = Device.objects(id=device_id).first()

    return f'[{",".join(loc.to_json() for loc in device.locations)}]'


@view('/device/(?P<device_id>\d+)/keepalive')
def get_keepalive(request, device_id: int):
    device = Device.objects(id=device_id).first()

    return f'[{",".join(ka.datetime.strftime("%s") for ka in device.keepalive)}]'
