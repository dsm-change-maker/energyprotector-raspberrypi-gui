import os
from package.utils import get_project_root
from package.utils import hash_password

class DeviceSetting():
    def __init__(self):
        self.id = ""
        self.password = ""
        self.is_hash = False
        self.auto_control = False
        self.remote_control = False

    def set_password(self, pw):
        self.password = pw
        self.is_hash = False

    def get_id(self):
        f = open(str(get_project_root()) + "/device_id.txt", "r")
        self.id = f.readline()
        f.close()

    def load_conf(self):
        conf_path = str(get_project_root()) + "/conf/config.txt"
        if not os.path.isfile(conf_path):
            return
        f = open(str(get_project_root()) + "/conf/config.txt", "r")
        self.id = f.readline()[:-1]
        f.readline()
        self.auto_control = bool(f.readline()[:-1])
        self.remote_control = bool(f.readline()[:-1])
        f.close()
        self.print()

    def hash(self):
        if not self.is_hash:
            self.password = hash_password(self.password)
        self.is_hash = True

    def print(self):
        print("id:'"+self.id+"'")
        print("pw:'"+str(self.password)+"'")
        print("auto control:'"+str(self.auto_control)+"'")
        print("remote_control:'"+str(self.remote_control)+"'")

    def write(self):
        self.hash()
        conf_path = str(get_project_root()) + "/conf"
        if not os.path.isdir(conf_path):
            os.mkdir(conf_path)
        f = open(conf_path + "/config.txt", "w")
        f.write(str(self.id) + '\n')
        f.write(str(self.password) + '\n')
        f.write(str(self.auto_control) + '\n')
        f.write(str(self.remote_control) + '\n')
        f.close()