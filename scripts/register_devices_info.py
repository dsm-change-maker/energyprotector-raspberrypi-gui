import json
import requests
from package.utils import get_project_root
from package.server import SERVER_URL


def req():
    with open(get_project_root() + '/conf/devices.json') as devices_json:
        devices_data = json.load(devices_json)
        for device in devices_data:
            headers = {'Content-Type': 'application/json'}
            data = {
                'device_id': device['id'],
                'device_type': device['type'],
                'unit_count': device['unit_count'],
                'device_ip': '0.0.0.0'
            }
            res = requests.post(SERVER_URL + '/api/device', headers=headers, data=json.dumps(data))
            print(device['id'], res, res.json())


if __name__ == '__main__':
    print('START - 디바이스 등록')
    req()
    print('END - 디바이스 등록 완료')
