from package.utils import process_res
import requests
import json


def device_control_api(server_url, device_id, device_type, on_off, unit_index, token):
    headers = {'Content-Type': 'application/json', 'Authorization': "Bearer " + token}
    data = {
        'device_id': device_id,
        'device_type': device_type,
        'on_off': on_off,
        'unit_index': unit_index
    }
    res = requests.post(server_url + '/api/device/control', headers=headers, data=json.dumps(data))
    return process_res(res)


class DeviceApi:
    def __init__(self, server):
        self.uri = '/api/device'
        self.server = server

    def get(self, device_id, device_type, token):
        headers = {'Content-Type': 'application/json', 'Authorization': "Bearer " + token}
        params = {'device_id': device_id, 'device_type': device_type}
        res = requests.get(self.server.url + self.uri, headers=headers, params=params)
        return process_res(res)

    def control(self, device_id, device_type, on_off, unit_index, token):
        return device_control_api(self.server.url, device_id, device_type, on_off, unit_index, token)

    def get_devices(self, token):
        headers = {'Authentication': "Bearer " + token}
        res = requests.get(self.server.url + '/api/web/devices', headers=headers)
        return process_res(res)
