import os
import sys


def usage():
    print('Usage is ...')
    print('\tpython convert_qrc_to_py.py [RESOURCE FILES DIR PATH]')
    print('\tpython convert_qrc_to_py.py [RESOURCE FILES DIR PATH] [PY FILES DIR PATH]')
    exit()


def is_ext_qrc(file_name):
    _, file_ext = os.path.splitext(file_name)
    return file_ext == '.qrc'


def convertQrcToPy(res_dir, py_dir):
    res_files = list(filter(is_ext_qrc, os.listdir(res_dir)))

    if len(res_files) == 0:
        print('Qrc File Not Found : ' + res_dir)
        return

    for res_file in res_files:
        os.system('pyrcc5 ' + res_dir + '/' + res_file + ' > ' + py_dir + '/' + res_file[:-4] + '_rc.py')
        print('Converted: ' + res_dir + '/' + res_file + ' -> ' + py_dir + '/' + res_file[:-4] + '_rc.py')


def main():
    if (len(sys.argv) is 1 or len(sys.argv) > 3) or not os.path.isdir(sys.argv[1]):
        usage()

    if len(sys.argv) is 2:
        convertQrcToPy(sys.argv[1], sys.argv[1])
        exit()

    if not os.path.isdir(sys.argv[2]):
        os.mkdir(sys.argv[2])

    convertQrcToPy(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
