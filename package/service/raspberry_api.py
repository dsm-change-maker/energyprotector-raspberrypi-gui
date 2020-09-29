from package.server import Server
from package.utils import process_res
from package.device_setting import DeviceSetting
import requests
import json


class RaspberryApi:
    def __init__(self, server: Server, device_setting: DeviceSetting):
        self.uri = '/api/raspberry'
        self.server = server
        self.device_setting = device_setting

    def connect(self):
        headers = {'Content-Type': 'application/json'}
        data = {
            'raspberry_group': self.device_setting.group,
            'raspberry_id': self.device_setting.id,
            'raspberry_pw': self.device_setting.password
        }
        res = requests.post(self.server.url + self.uri + '/connect', headers=headers, data=json.dumps(data))
        return process_res(res)

    def get(self, token):
        headers = {'Content-Type': 'application/json', 'Authentication': "Bearer " + token}
        res = requests.get(self.server.url + self.uri, headers=headers)
        return process_res(res)

    def post(self):
        headers = {'Content-Type': 'application/json'}
        data = {
            'raspberry_group': self.device_setting.group,
            'raspberry_id': self.device_setting.id,
            'raspberry_pw': self.device_setting.password,
            'remote_control': self.device_setting.remote_control
        }
        res = requests.post(self.server.url + self.uri, headers=headers, data=json.dumps(data))
        return process_res(res)

    def put(self, token):
        headers = {'Content-Type': 'application/json', 'Authentication': "Bearer " + token}
        data = {
            'raspberry_group': self.device_setting.group,
            'raspberry_id': self.device_setting.id,
            'raspberry_pw': self.device_setting.password,
            'remote_control': self.device_setting.remote_control
        }
        res = requests.post(self.server.url + self.uri, headers=headers, data=json.dumps(data))
        return process_res(res)

    def delete(self, token):
        headers = {'Authentication': "Bearer " + token}
        res = requests.delete(self.server.url + self.uri, headers=headers)
        return process_res(res)

    # dsm
    # dsm11
    # 1234


if __name__ == "__main__":
    server = Server()
    device_setting = DeviceSetting()
    device_setting.group = 'dsm'
    device_setting.id = 'dsm11'
    device_setting.password = '1234'

    # Raspberry API Test
    print('Raspberry API Test')
    ## Connect TEST
    print('- Connect API Test')
    rasp_api = RaspberryApi(server, device_setting)
    res = rasp_api.connect()
    print(res)
    print('access_token : ' + res[2]['access_token'])
    print('refresh_token : ' + res[2]['refresh_token'])

    ## Get Test
    print('- Get API TEST')