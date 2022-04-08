import os
import functools as func


IMAGES = [
    'jpg',
    'jpeg',
    'png',
    'gif'
]
ROOT = './'

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
        if list[-1].lower() in IMAGES:
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