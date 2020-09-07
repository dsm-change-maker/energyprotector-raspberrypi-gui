import sys
import random
import string
from datetime import datetime

def usage():
	print('Usage is ...')
	print('\tpython device_id_generator.py [DEVICE ID FILE PATH]')
	exit()

def new_id():
    now = datetime.now()
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4)) + \
              '_' + \
              str(hex(int(str(now.year)[2:] + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(
                  now.second))))[2:]

def main():
    if len(sys.argv) != 2:
        usage()

    path = sys.argv[1]
    id = new_id()
    print("Generated: " + id)
    file = open(path, "w")
    file.write(id)
    file.close()
    print("... \'" + path + "\'")

if __name__ == '__main__':
    main()