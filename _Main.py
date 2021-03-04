from lib.lib import cin, error
from cls.cls import FM 

class Main():
    def __init__(self):
        self.uin = ""
        self.uinarr = ""
        self.quit = False
        self.path_pointer = ""
        
        self.fman = FM.FileManager()

    def init(self):
        self.fman.load_drives()
        return self

    def show_initial(self):
        print("-- File Manager --")

        self.show_drives()
        return self
    
    def end(self):
        print("-- File Manager --")

    def main_loop(self):
        while not self.quit:
            self.uin = cin.input("[=] ->")

            if self.uin == False or self.uin == 'q' or self.uin == 'quit':
                self.quit = True
                continue
            else:
                self.uinarr = self.uin.split(" ")
            if self.uin == "help":
                pass  
            elif self.uin[:3] == "op ":
                if not error.array_over_under_load_error(2, 2, self.uinarr):
                    self.fman.open_directory(self.uinarr[1])
                    print("Path pointer moved: " + self.fman.get_path_pointer())

            elif self.uin == "fad":
                fad = self.fman.files_and_directories()
                print("Folder is empty!") if len(fad) <= 0 else print(*fad, sep="\n") 

            elif self.uin == "cup":
                print(self.fman.get_path_pointer())

            elif self.uin[:3] == "ct ":
                if not error.array_over_under_load_error(3, 3, self.uinarr) and\
                   not error.char_compare_at_pos_error("-", 0, self.uinarr[1]) and\
                   not self.fman.create(self.uinarr[1], self.uinarr[2]):
                    print("Created!")

            elif self.uin[:3] == "rv ":
                 if not error.array_over_under_load_error(3, 3, self.uinarr) and\
                   not error.char_compare_at_pos_error("-", 0, self.uinarr[1]) and\
                   not self.fman.remove(self.uinarr[1], self.uinarr[2]):
                    print("Removed!")

            elif self.uin[:5] == "copy ":
                if not error.array_over_under_load_error(3, 3, self.uinarr) and\
                   self.fman.copy(self.uinarr[1], self.uinarr[2]):
                    print("File copied!")

            elif self.uin[:5] == "move ":                
                if not error.array_over_under_load_error(3, 3, self.uinarr) and\
                   self.fman.copy(self.uinarr[1], self.uinarr[2]):
                    print("File moved!")

            else:
                print("Unknown Command!")

        return self

    def show_drives(self):
        print("Drives:")
        for drive in self.fman.get_drives():
            print(drive["letter"] + ":" + "\t" + drive["name"])
        
        return self