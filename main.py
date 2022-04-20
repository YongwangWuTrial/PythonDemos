

from klas_def import *


def print_hi():

    print_source_file_path()
    # Use a breakpoint in the code line below to debug your script.
    txt_files = SourceFiles(r"d:\ProgramPractice")
    txt_files.print_path()
    print(txt_files._SourceFiles__folder_path)
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
