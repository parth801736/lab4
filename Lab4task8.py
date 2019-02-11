import hashlib
import os


def md5(file_name):
    hash_md5 = hashlib.md5()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

PATH = os.getenv("HOME")
def findfile(extension):
    for root, subFolder, files in os.walk(PATH):
        for item in files:
            if item.endswith("."+ str(extension)):
                fileNamePath = str(os.path.join(root,item))
                print(fileNamePath," ",md5(fileNamePath))


x = input("enter file extension for Search:")
findfile(x)

