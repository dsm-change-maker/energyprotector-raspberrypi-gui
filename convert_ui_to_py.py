import os
import sys

def usage():
	print('Usage is ...')
	print('\tpython convert_to_py.py [UI FILES DIR PATH]')
	print('\tpython convert_to_py.py [UI FILES DIR PATH] [PY FILES DIR PATH]')
	exit()

def is_ext_ui(file_name):
	_, file_ext = os.path.splitext(file_name)
	return file_ext == '.ui'

def convertUiToPy(ui_dir, py_dir):
	ui_files = list(filter(is_ext_ui, os.listdir(ui_dir)))

	if len(ui_files) is 0:
		print('Ui File Not Found : ' + ui_dir)
		return

	for ui_file in ui_files:
		os.system('pyuic5 -x ./' + ui_dir + '/' + ui_file + ' -o ' + py_dir + '/' + ui_file[:-3] + '_ui.py')
		print('Converted: ' + ui_dir + '/' + ui_file + ' -> ' + py_dir + '/' + ui_file[:-3] + '_ui.py')

def main():
	if (len(sys.argv) is 1 or len(sys.argv) > 3) or not os.path.isdir(sys.argv[1]):
		usage()

	if len(sys.argv) is 2:
		convertUiToPy(sys.argv[1], sys.argv[1])
		exit()

	if not os.path.isdir(sys.argv[2]):
		os.mkdir(sys.argv[2])

	convertUiToPy(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
	main()