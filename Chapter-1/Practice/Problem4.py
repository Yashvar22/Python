import os

# specify the directory path
path = "./"

# get list of files and directories
contents = os.listdir(path)

# print the contents
print("Contents of the directory:")
for item in contents:
    print(item)