import csv
import os
from os.path import isfile, isdir, islink, join, getsize


def get(path):
	dirs, files, size, errors = [], [], [], []
	try:
		for item in os.listdir(path):
			full_name = join(path, item)
			if isfile(full_name):
				files.append(full_name)
				size.append(getsize(full_name))
			elif isdir(full_name):
				dirs.append(full_name)
			elif islink(full_name):
				pass # print(full_name)
	
	except PermissionError:
		errors.append(path)

	return dirs, [files, size], errors


def stamp(path, file=None, delimiter='|', quotechar='"', quoting=csv.QUOTE_ALL):
	list_path = [path]
	index = 0
	list_err = []
	while index < len(list_path):
		if isdir(list_path[index]):
			dirs, files, err = get(list_path[index])
			list_err.extend(err)
			dirs_and_files = sorted(dirs) + files[0]
			for i in range(1,len(dirs_and_files)):
				list_path.insert(index + i, (dirs_and_files)[i])
		index += 1

	if file:
		with open(file, 'w', newline='') as csv_file:
			spamwriter = csv.writer(csv_file, delimiter=delimiter, quotechar=quotechar, quoting=quoting)
			for i in range(len(list_path)):
				spamwriter.writerow([list_path[i]])

	if DEBUG:
		print('ERRORS:' , list_err)

	return list_path

if __name__ == "__main__":
	DEBUG = 1
	print(len(stamp('/usr', file='csv.csv')))