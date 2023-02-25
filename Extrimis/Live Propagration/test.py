# import OS module
import os

path = os.getcwd()


# List all files and directories in the specified path
print("Files and Directories in '% s':" % path)
obj = os.scandir(path)
for entry in obj:
	if entry.is_dir() :
		print(entry.name,' [Directory]')

obj = os.scandir(path)
print(40*'*')
for entry in obj:
	if entry.is_file(): 
		print(entry.name,' [File]')
    

