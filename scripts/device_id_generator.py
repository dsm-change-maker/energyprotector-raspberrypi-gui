import sys
import os
import random
import string
from datetime import datetime
from pathlib import Path


def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent.parent


def usage():
    print('Usage is ...')
    print('\tpython device_id_generator.py [DEVICE ID DIR PATH] [DEVICE ID FILE NAME]')
    exit()


def new_id():
    now = datetime.now()
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4)) + \
           '_' + \
           str(hex(int(str(now.year)[2:] + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(
               now.second))))[2:]


def main():
    if len(sys.argv) != 3:
        usage()

    path_dir = sys.argv[1]
    file_name = sys.argv[2]
    if not os.path.isdir(path_dir):
        os.makedirs(path_dir)

    id = new_id()
    print("Generated: " + id)
    file = open(path_dir + "/" + file_name, "w")
    file.write(id)
    file.close()
    print("... \'" + path_dir + "/" + file_name + "\'")


if __name__ == '__main__':
    main()
