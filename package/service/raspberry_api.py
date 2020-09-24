from package.server import Server
from package.utils import process_res
from package.device_setting import DeviceSetting
import requests
import json


class RaspberryApi:
    def __init__(self, server: Server, device_setting: DeviceSetting):
        self.server = server
        self.device_setting = device_setting

    def connect(self):
        headers = {'Content-Type': 'application/json'}
        data = {
            'raspberry_group': self.device_setting.group,
            'raspberry_id': self.device_setting.id,
            'raspberry_pw': self.device_setting.password
        }
        res = requests.post(self.server.url, headers=headers, data=json.dumps(data))
        return process_res(res)

    def get(self, token):
        headers = {'Content-Type': 'application/json', 'Authentication': "Bearer " + token}
        res = requests.get(self.server.url, headers=headers)
        return process_res(res)

    def post(self):
        headers = {'Content-Type': 'application/json'}
        data = {
            'raspberry_group': self.device_setting.group,
            'raspberry_id': self.device_setting.id,
            'raspberry_pw': self.device_setting.password,
            'remote_control': self.device_setting.remote_control
        }
        res = requests.post(self.server.url, headers=headers, data=json.dumps(data))
        return process_res(res)

    def put(self, token):
        headers = {'Content-Type': 'application/json', 'Authentication': "Bearer " + token}
        data = {
            'raspberry_group': self.device_setting.group,
            'raspberry_id': self.device_setting.id,
            'raspberry_pw': self.device_setting.password,
            'remote_control': self.device_setting.remote_control,
            'raspberry_devices': self.device_setting.devices
        }
        res = requests.post(self.server.url, headers=headers, data=json.dumps(data))
        return process_res(res)

    def delete(self, token):
        headers = {'Content-Type': 'application/json', 'Authentication': "Bearer " + token}
        res = requests.delete(self.server.url, headers=headers)
        return process_res(res)