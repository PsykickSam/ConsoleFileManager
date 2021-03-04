import os
import string 
import shutil
import win32api
from ctypes import windll

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            data = win32api.GetVolumeInformation(letter + ":\\\\")
            drive = {
                "letter": letter, 
                "name": data[0], # drive name
                "size": data[3], # drive size
                "type": data[4], # drive type
            }
            drives.append(drive)
        bitmask >>= 1

    return drives

def get_files_and_directories(path):
    return os.listdir(path)

def create_folder(name):
    os.makedirs(name)
    return True

def create_file(name):
    with open(name, "w"): pass
    return True

def delete_folder(name):
    shutil.rmtree(name)
    return True

def delete_file(name):
    os.unlink(name)
    return True

def copy(src, dest):
    shutil.copy2(src, dest)
    return True
    
def move(src, dest):
    shutil.move(src, dest)
    return True