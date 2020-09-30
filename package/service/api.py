from package.service.device_api import DeviceApi
from package.service.raspberry_api import RaspberryApi
from package.service.using_time_api import UsingTimeApi


class Apis:
    def __init__(self, server, device_setting):
        self.device = DeviceApi(server)
        self.raspberry = RaspberryApi(server, device_setting)
        self.usage = UsingTimeApi(server, device_setting)
