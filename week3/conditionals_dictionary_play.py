import math


def square(val):
    return val*val

def add2(val):
    return val + 2

def sqrt(val):
    return math.sqrt(val)


dic = {1:add2,2:square,3:sqrt}

for x in range(1,5):
    try:
        print(dic[x](x))
    except KeyError:
        print (" not a key in the dictionary")

