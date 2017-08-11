from haishoku import Haishoku
import math
import time
import os


image_path = 'demo/demo_01.png'

def diff_val(palette1, palette2):
    #palette should be a list contains 8 tuples, each tuple stands for an RGB.
    assert len(palette1)==len(palette2)==8,'length of palettes should be 8'
    diff_val = 0
    for i in range(8):
        for j in range(3):
            diff_val += (palette1[i][j]-palette2[i][j])**2
    return math.sqrt(diff_val)

def palettes(times):
    #yield palette for chosen times
    palettes=[]
    for i in range(times):
        palettes.append(Haishoku.getPalette(image_path))
    return palettes

def new_palettes(times):
    new_palettes=[]
    for i in range(times):
        new_palettes.append(Haishoku.new_getPalette(image_path))

    return new_palettes

def get_diff(times, func_p):
    assert times>=2,'the parameter should be greater than 1'
    Palettes = func_p(times)
    diffs=[]
    for i in range(1,times):
        diffs.append(round(diff_val(Palettes[i-1],Palettes[i]),2))
    return diffs








def time_to_getpalette():
    t1=time.time()
    Haishoku.getPalette(image_path)
    t2=time.time()
    return round(t2-t1,2)

def time_to_get_diff_val():
    t1=time.time()
    diff_val(Haishoku.getPalette(image_path),Haishoku.getPalette(image_path))
    t2=time.time()
    return round(t2-t1,2)

def time_to_get_diff(times):
    t1=time.time()
    get_diff(times)
    t2=time.time()
    return round(t2-t1,2)

def time_to_get_palettes(times):
    t1=time.time()
    palettes(times)
    t2=time.time()
    return round(t2-t1,2)


#print(time_to_getpalette())
#print(time_to_get_diff(3))
#print(time_to_get_palettes(3))
#print(time_to_get_diff_val())


# origin_diff = get_diff(5, palettes)
# new_diff = get_diff(5, new_palettes)

# print(origin_diff)
# print(new_diff)


# print('origin:')
# for i in palettes(5):    
#     print(i)
# print()
# print('new:')
# for i in new_palettes(5):
#     print(i)


