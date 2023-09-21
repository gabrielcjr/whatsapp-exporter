import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

def open_file(mode):
    return open(f"{BASE_PATH}/lista.txt", mode)

def turn_file_into_list(mode):
    file = open_file(mode)
    raw_list = file.readlines()
    list = []
    for item in raw_list:
        list.append(item.strip())
    return list