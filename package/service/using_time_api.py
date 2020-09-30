from package.utils import process_res
import requests


class UsingTimeApi:
    def __init__(self, server, device_setting):
        self.uri = '/api/web/using-time'
        self.server = server
        self.device_setting = device_setting

    def get(self, year=False, year_n=0, month=False, month_n=0, day=False, day_n=0):
        params = {'raspberry_group': self.device_setting.group,
                  'raspberry_id': self.device_setting.id,
                  'year': year,
                  'year_n': year_n,
                  'month': month,
                  'month_n': month_n,
                  'day': day,
                  'day_n': day_n}
        res = requests.get(self.server.url + self.uri, params=params)
        return process_res(res)

    def get_year(self, year):
        params = {'raspberry_group': self.device_setting.group, 'raspberry_id': self.device_setting.id}
        res = requests.get(self.server.url + self.uri + '/' + str(year), params=params)
        return process_res(res)
