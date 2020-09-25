from package.server import Server
from package.device_setting import DeviceSetting
from package.service.device_api import DeviceApi
from package.service.raspberry_api import RaspberryApi


class Apis:
    def __init__(self, server:Server, device_setting:DeviceSetting):
        self.device = DeviceApi(server)
        self.raspberry = RaspberryApi(server, device_setting)
