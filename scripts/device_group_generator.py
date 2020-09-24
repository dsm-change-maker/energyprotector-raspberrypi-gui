import sys
import os
from datetime import datetime
from pathlib import Path


def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent.parent


def usage():
    print('Usage is ...')
    print(
        '\tpython device_group_generator.py [DEVICE GROUP NAME STRING] [DEVICE GROUP DIR PATH] [DEVICE GROUP FILE NAME]')
    exit()


def new_group(group_name):
    now = datetime.now()
    return group_name + '_' + str(hex(
        int(str(now.year)[2:] + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second))))[2:]


def main():
    if len(sys.argv) != 4:
        usage()

    group_str = sys.argv[1]
    path_dir = sys.argv[2]
    file_name = sys.argv[3]
    if not os.path.isdir(path_dir):
        os.makedirs(path_dir)

    group_name = new_group(group_str)
    print("Generated: " + group_name)
    file = open(path_dir + str(get_project_root()) + "/" + file_name, "w")
    file.write(group_name)
    file.close()
    print("... \'" + path_dir + "/" + file_name + "\'")


if __name__ == '__main__':
    main()
