from package.server import Server
from package.utils import process_res
import requests


class DeviceApi:
    def __init__(self, server:Server):
        self.server = server

    def get(self, device_id, token):
        headers = {'Content-Type': 'application/json', 'Authentication': "Bearer " + token}
        params = {'device_id': device_id}
        res = requests.get(self.server.url, headers=headers, params=params)
        return process_res(res)
