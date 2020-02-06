import os

files = os.listdir()

for i in range(len(files)):
	old_name = files[i]
	new_name = files[i][files[i].find('c'):]
	os.rename(old_name, new_name)