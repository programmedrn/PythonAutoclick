# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from time import sleep
from Util import *
from MouseEvent import *
from ReadImages import *


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
