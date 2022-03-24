# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pyautogui
import os
import functools as func
import math
from time import sleep

def find_loc(file_name):
    i = pyautogui.locateOnScreen(file_name)
    print(i)
    return i

def click_center(loc):
    q = pyautogui.center(loc)
    pyautogui.click(q)

def move_to_near_zero():
    pyautogui.moveTo(10,10)

def find_click(file_name):
    try:
        click_center(
            find_loc(file_name)
        )
        move_to_near_zero()
    except Exception as e:
        print("Failed to Find", e)

def get_file(root_dir):
    path = root_dir

    try:
        files = os.listdir(path)
        print("Files : ", files)
    except Exception as e:
        print("Failed to get files")
        print("Message : ", e)
    return files

def get_images(root_dir):
    files = get_file(root_dir)
    images = []
    for item in files:
        list = item.split('.')
        if list[-1] in IMAGES:
            temp = []
            temp.append(func.reduce(lambda pre, post : pre +'.'+ post, list[:-1]))
            temp.append(list[-1])
            print("Image item : ", item, "name is ", func.reduce(lambda pre, post : pre +'.'+ post, list[:-1]))
            images.append(temp)
    return images

def split_by_underbar(list):
    dict = {}
    try:
        for item in list:
            terms = item[0].split('_')
            dict[item[0]+'.'+item[1]] = int(terms[1])
    except Exception as e:
        print("!!! Failed to convert ", item)
        print("!!! Among ", list)
        print("message : ", e)
    return dict

def get_gcd(dict: dict):
    keys = dict.keys()
    times = []
    for key in keys:
        times.append(dict[key])
    return func.reduce(math.gcd, times)

def get_multi(dict: dict):
    keys = dict.keys()
    times = []
    for key in keys:
        times.append(dict[key])
    return func.reduce(lambda x, y : x * y, times)

IMAGES = [
    'jpg',
    'jpeg',
    'png',
    'gif'
]
ROOT = './'
TERM = 1
TILL = 10
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = get_images(ROOT)
    b = split_by_underbar(a)
    print(b)
    TERM = get_gcd(b)
    TILL = get_multi(b)
    time = 0
    while True:
        sleep(TERM)
        time += TERM
        now = filter(lambda x:time%b[x]==0, b)
        print("it's ", time)
        if now is None:
            print("pass : ", now)
        for item in now:
            print(item)
            find_click(item)
        if time == TILL:
            time = 0

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
