from os import name
import numpy as np
import pandas as pd
import numpy as np
import pandas as pd



def save_map_csv(channel_map_x,channel_map_y,channel_map_n,name):
    unix = []
    uniy = []
    for i in channel_map_x:
        if i not in unix:
            unix.append(i)
    unix.sort()

    for i in channel_map_y:
        if i not in uniy:
            uniy.append(i)
    uniy.sort(reverse=True)


    the_map = np.zeros(shape=(len(uniy),len(unix)))

    for k in range(0,len(channel_map_x)):
        the_map[uniy.index(channel_map_y[k])][unix.index(channel_map_x[k])] = channel_map_n[k]
    print(the_map)
    pd.DataFrame(the_map).to_csv(name,header=None, index=None)

def cut(num, c):
    str_num = str(num)
    return float(str_num[:str_num.index('.') + 1 + c])

def add_pad_channel_number(msp0,bgad,tlpx,tlpy,current_x,current_y,start,end):
    msp0.add_text(str(round((current_x - tlpx + bgad) * 2 + (tlpy - current_y) * 16)),
                 dxfattribs={
                     'height': 0.02}).set_pos(start, align='BOTTOM_LEFT')
    msp0.add_text(str(round((current_x - tlpx + bgad) * 2 + (tlpy - current_y) * 16)),
                 dxfattribs={
                     'height': 0.02}).set_pos(end, align='BOTTOM_LEFT')

def add_intan_channel_number(msp0,bgad,tlpx,tlpy,current_x,current_y,start,end,map_d):
    #print(intan_map_dist[int(round((current_x - tlpx + BGA_distance) * 2 + (top_pad_y - current_y) * 16))])
    msp0.add_text(map_d[int(round((current_x - tlpx + bgad) * 2 + (tlpy - current_y) * 16))],
                 dxfattribs={
                     'height': 0.02}).set_pos(start, align='BOTTOM_LEFT')

    msp0.add_text(map_d[int(round((current_x - tlpx + bgad) * 2 + (tlpy - current_y) * 16))],
                 dxfattribs={
                     'height': 0.02}).set_pos(end, align='BOTTOM_LEFT')

