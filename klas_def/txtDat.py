# coding = utf-8
import os.path


class SourceFiles():
    def __init__(self, folder_path=""):
        self.__folder_path = folder_path
        self.files = None

    @property
    def folder_path(self):
        return self.__folder_path

    @folder_path.setter
    def folder_path(self, value):
        if os.path.isdir(value):
            self.__folder_path = value

    def print_path(self):
        if self.__folder_path is None:
            print("folder path is not settled!")
            return
        print(self.__folder_path)