import random
import string
from datetime import datetime

class DeviceSetting():
    def __init__(self):
        self.id = ""
        self.password = ""
        self.auto_off = False
        self.remote_control = False

    def new_id(self):
        now = datetime.now()
        self.id = ''.join(random.choice(string.ascii_uppercase+string.digits)for _ in range(4)) + \
                  '_' +\
                  str(hex(int(str(now.year)[2:] + str(now.month) + str(now.day) +str(now.hour) +str(now.minute) +str(now.second))))[2:]

