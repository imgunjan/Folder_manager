import os
import shutil

path = input("Enter the path : ")
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension_name = extension[1:]
    folder_path = path + "\\" + extension_name

    if os.path.exists(folder_path):
        shutil.move(path + "\\" + file, path + "\\" + extension_name + "\\" + file)
    else:
        os.makedirs(folder_path)
        shutil.move(path + "\\" + file, path + "\\" + extension_name + "\\" + file)
