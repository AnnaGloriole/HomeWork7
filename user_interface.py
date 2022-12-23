from model import get_info
from log import writing_scv, read_contact, writing_txt

def ui_start():
    while True:
        print('please write a number to choose mode')
        print('1. to record new subscriber; 2. to print directory on display; 3. Exit the program')
        mode = int(input())
        if mode == 1:
            a = get_info()
            writing_txt(a)
            writing_scv(a)
        elif mode == 2:
            print(read_contact())
        elif mode == 3:
            print('exit program')
            break
