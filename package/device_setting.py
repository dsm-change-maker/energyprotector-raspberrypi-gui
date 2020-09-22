import os
from package.utils import get_project_root

class DeviceSetting():
    def __init__(self):
        self.id = ""
        self.password = ""
        self.auto_control = True
        self.remote_control = True

    def get_id(self):
        f = open(str(get_project_root()) + "/conf/device_id.txt", "r")
        self.id = f.readline()
        f.close()

    def load_conf(self):
        conf_path = str(get_project_root()) + "/conf/config.txt"
        if not os.path.isfile(conf_path):
            return False
        f = open(str(get_project_root()) + "/conf/config.txt", "r")
        self.id = f.readline()[:-1]
        if len(self.id) is 0:
            return False
        self.password = f.readline()[:-1]
        if len(self.password) is 0:
            return False
        auto_control_str = f.readline()[:-1]
        if len(auto_control_str) is 0:
            return False
        self.auto_control = auto_control_str == 'True'
        remote_control_str = f.readline()[:-1]
        if len(remote_control_str) is 0:
            return False
        self.remote_control = remote_control_str == 'True'
        f.close()
        return True

    def print(self):
        print("id:'"+self.id+"'")
        print("pw:'"+str(self.password)+"'")
        print("auto control:'"+str(self.auto_control)+"'")
        print("remote_control:'"+str(self.remote_control)+"'")

    def write(self):
        conf_path = str(get_project_root()) + "/conf"
        if not os.path.isdir(conf_path):
            os.mkdir(conf_path)
        f = open(conf_path + "/config.txt", "w")
        f.write(str(self.id) + '\n')
        f.write(str(self.password) + '\n')
        f.write(str(self.auto_control) + '\n')
        f.write(str(self.remote_control) + '\n')
        f.close()

    def device_setting_init(self):
        conf_path = str(get_project_root()) + "/conf"
        if not os.path.isdir(conf_path):
            os.mkdir(conf_path)
        f = open(conf_path + "/config.txt", "w")
        for i in range(4):
            f.write('\n')
        f.close()
        self.id = ""
        self.password = ""
        self.auto_control = False
        self.remote_control = False

if __name__ == "__main__":

    device_setting = DeviceSetting()
    device_setting.load_conf()
    device_setting.print()