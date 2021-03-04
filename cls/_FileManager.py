import sys
from lib.lib import fm

class FileManager():
    def __init__(self):
        self.path_pointer = ""
        self.drives = []

    def get_path_pointer(self):
        return self.path_pointer

    def get_drives(self):
        return self.drives

    def quit_handler(self):
        sys.exit()

    def load_drives(self):
        self.drives = fm.get_drives()

    def open_directory(self, path):
        if path == ".":
            self.path_pointer = self.path_pointer
        elif path == "..":
            self.path_pointer = "/".join(self.path_pointer.split("/")[:-2]) + "/"
        else:
            self.path_pointer += path + "/"
        return self.path_pointer

    def files_and_directories(self): 
        return fm.get_files_and_directories(self.path_pointer)

    def create(self, type, name):
        if type == "-folder": 
            fm.create_folder(self.path_pointer + name)
            return True
        elif type == "-file": 
            fm.create_file(self.path_pointer + name)
            return True
        return False

    def remove(self, type, name):
        if type == "-folder": 
            fm.delete_folder(self.path_pointer + name)
            return True
        elif type == "-file": 
            fm.delete_file(self.path_pointer + name)
            return True

        return False

    def copy(self, src, dest):
        fm.copy(src, dest)
        return True

    def move(self, src, dest):
        fm.move(src, dest)
        return True
