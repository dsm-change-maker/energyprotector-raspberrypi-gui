import os
import sys

def usage():
	print('Usage is ...')
	print('\tpython convert_to_py.py [RESOURCE FILES PATH ...]')
	print('\tpython convert_to_py.py [UI FILES DIR PATH] [PY FILES DIR PATH]')
	print('\tpython convert_to_py.py [RESOURCE FILES PATH ...] [UI FILES DIR PATH] [PY FILES DIR PATH]')
	exit()

def countNotDirInArgv(sys_argv):
	count = 0
	for argv in sys_argv:
		if not os.path.isdir(argv):
			count+=1
	return count

def parseArgv(sys_argv):
	res_files_path = []
	ui_path_dir = ""
	py_path_dir = ""

	for name in sys_argv:
		if os.path.isfile(name):
			_, file_ext = os.path.splitext(name)
			if file_ext == '.qrc':
				res_files_path.append(name)
				continue
			print('Not a \'.qrc\' File : ' + name)
			continue
		elif os.path.isdir(name):
			if len(ui_path_dir) == 0:
				ui_path_dir = name
				continue
			py_path_dir = name
			continue
		print('Path Not Found: ' + name)

	return [res_files_path, ui_path_dir, py_path_dir]

def convertQrcToPy(res_files):
	if len(res_files) > 0:
		for res_file in res_files:
			os.system('pyrcc5 ' + res_file + ' > ./' + res_file[:-4] + '_rc.py')
			print('Converted: ' + res_file + ' -> ' + res_file[:-4] + '_rc.py')

def convertUiToPy(ui_dir, py_dir):
	if len(ui_dir) is 0:
		return

	if len(py_dir) is 0:
		py_dir = ui_dir

	ui_files = []
	ui_dir_files = os.listdir(ui_dir)

	for files in ui_dir_files:
		_, file_ext = os.path.splitext(files)
		if file_ext == '.ui':
			ui_files.append(files)

	if len(ui_files) is 0:
		print('Ui File Not Found : ' + ui_dir)
		return

	for ui_file_name in ui_files:
		_, file_ext = os.path.splitext(ui_file_name)
		if file_ext == '.ui':
			os.system('pyuic5 -x ./' + ui_dir + '/' + ui_file_name + ' -o ./' + py_dir + '/' + ui_file_name[:-3] + '_ui.py')
			print('Converted: ' + ui_dir + '/' + ui_file_name + ' -> ' + py_dir + '/' + ui_file_name[:-3] + '_ui.py')

def main():
	if (len(sys.argv) is 1) or (countNotDirInArgv(sys.argv[1:]) + 2 < len(sys.argv[1:])):
		usage()

	res_files, ui_dir, py_dir = parseArgv(sys.argv[1:])

	convertQrcToPy(res_files)
	convertUiToPy(ui_dir, py_dir)


if __name__ == '__main__':
	main()