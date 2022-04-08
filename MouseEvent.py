import pyautogui

def find_loc(file_name):
    i = pyautogui.locateOnScreen(file_name)
    print(i)
    return i

def click_center(loc):
    q = pyautogui.center(loc)
    pyautogui.click(q)

def find_click(file_name):
    try:
        click_center(
            find_loc(file_name)
        )
        move_to_near_zero()
    except Exception as e:
        print("Failed to Find", e)

def move_to_near_zero():
    pyautogui.moveTo(10, 10)