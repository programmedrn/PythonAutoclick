import functools as func
import math

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
