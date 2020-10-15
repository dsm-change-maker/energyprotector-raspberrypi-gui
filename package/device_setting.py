# -*- coding: utf-8 -*-

import os
import sys
import json
from functools import reduce
from package.utils import get_project_root
from package.utils import file_read_one
from package.utils import get_type_devices
from package.database import DataBase
from package.server import Server
from package.service.api import Apis
from package.utils import get_device_one


def get_devices():
    devices = []
    with open(get_project_root() + '/conf/devices.json') as devices_json:
        devices_data = json.load(devices_json)
        for i in range(len(devices_data)):
            devices.append(Device(devices_data[i]['id'], devices_data[i]['type'], devices_data[i]['unit_count']))
            devices[i].load()
    return devices


def update_device(device_id, device_type, unit_index, on_off):
    this_device_list = get_device_one(get_devices(), device_id, device_type)
    if len(this_device_list) is not 0:
        this_device = this_device_list[0]
        this_device.units[unit_index] = on_off
        this_device.write()


class Device:
    def __init__(self, device_id: str, device_type: str, unit_count: int):
        self.id = device_id
        self.d_type = device_type
        self.ip = ''
        self.units = [False for _ in range(unit_count)]

        self.db = DataBase(get_project_root() + '/conf/energy_protector')
        self.db.execute(
            'CREATE TABLE IF NOT EXISTS devices (d_id TEXT, d_type TEXT, d_ip TEXT, d_units TEXT)')

        count = self.db.execute('SELECT COUNT(*) FROM devices WHERE d_type = ? AND d_id = ?',
                                (self.d_type, self.id))[0][0]
        if count is 0:
            self.db.execute(
                'INSERT INTO devices(d_id, d_type, d_ip, d_units) values (?, ?, ?, ?)',
                (self.id, self.d_type, self.ip, self.units_to_str())
            )
        else:
            self.load()
            self.write()

    def set_unit(self, i, state):
        self.units[i] = state
        self.write()

    def units_to_str(self):
        return reduce(lambda r, state: r + str(int(state)) + ';', self.units, '')[:-1]

    def str_to_units(self, string):
        self.units = list(map(lambda state: state == '1', string.split(';')))

    def print(self):
        print('id : ' + self.id)
        print('type : ' + self.d_type)
        print('ip : ' + self.ip)
        print('units :', self.units)

    def load(self, ip=True, units=True):
        data = self.db.execute('SELECT * FROM devices WHERE d_type = ? AND d_id = ?',
                               (self.d_type, self.id))[0]
        if ip:
            self.ip = data[2]
        if units:
            self.str_to_units(data[3])

    def write(self):
        self.db.execute(
            'UPDATE devices SET d_ip = ?, d_units = ? WHERE d_type = ? AND d_id = ?',
            (self.ip, self.units_to_str(), self.d_type, self.id))


class DeviceSetting:
    def __init__(self):
        self.is_registered = False
        self.group = ''
        self.id = ''
        self.password = ''
        self.auto_control = True
        self.remote_control = True
        self.devices = get_devices()
        self.switch_devices = get_type_devices(self.devices, 'switch')
        self.plug_devices = get_type_devices(self.devices, 'plug')

        self.get_group()
        self.get_id()

        self.db = DataBase(get_project_root() + '/conf/energy_protector')
        self.db.execute(
            'CREATE TABLE IF NOT EXISTS device_setting (is_registered INT, d_group TEXT, d_id TEXT, d_password TEXT, d_auto_control INT, d_remote_control INT)')

        count = \
            self.db.execute('SELECT COUNT(*) FROM device_setting WHERE d_group = ? AND d_id = ?',
                            (self.group, self.id))[0][0]
        if count is 0:
            self.db.execute(
                'INSERT INTO device_setting(is_registered, d_group, d_id, d_password, d_auto_control, d_remote_control) values (?, ?, ?, ?, ?, ?)',
                (int(self.is_registered), self.group, self.id, self.password, int(self.auto_control),
                 int(self.remote_control)))
        else:
            self.load_conf()

    def get_id(self):
        file_name = get_project_root() + "/conf/device_id.txt"
        if not os.path.isfile(file_name):
            sys.stderr.write("No file: %s\n" % file_name)
            exit(1)
        self.id = file_read_one(file_name)

    def get_group(self):
        file_name = get_project_root() + "/conf/device_group.txt"
        if not os.path.isfile(file_name):
            sys.stderr.write("No file: %s\n" % file_name)
            exit(1)
        self.group = file_read_one(file_name)

    def load_conf(self):
        data = self.db.execute('SELECT * FROM device_setting WHERE d_group = ? AND d_id = ?', (self.group, self.id))[0]
        self.is_registered = data[0] == 1
        self.group = data[1]
        self.id = data[2]
        self.password = data[3]
        self.auto_control = data[4] == 1
        self.remote_control = data[5] == 1

        if len(self.group) is 0:
            return False
        if len(self.id) is 0:
            return False
        if len(self.password) is 0:
            return False
        return True

    def print(self):
        print("group:'" + self.group + "'")
        print("id:'" + self.id + "'")
        print("pw:'" + str(self.password) + "'")
        print("auto control:'" + str(self.auto_control) + "'")
        print("remote_control:'" + str(self.remote_control) + "'")

    def write(self):
        self.db.execute(
            'UPDATE device_setting SET is_registered = ?, d_password = ?, d_auto_control = ?, d_remote_control = ? WHERE d_group = ? AND d_id = ?',
            (int(self.is_registered), self.password, int(self.auto_control), int(self.remote_control), self.group,
             self.id))

    def device_setting_init(self):
        self.get_group()
        self.get_id()
        self.password = ""
        self.auto_control = True
        self.remote_control = True

    def register(self, server: Server):
        self.load_conf()
        if self.is_registered:
            return False

        apis = Apis(server, self)
        res = apis.raspberry.post()
        if res[0] and res[1] == 201:
            self.is_registered = True
            self.write()
            return True
        return None
