# the code is fine for linear electrodes, but it might not work for nonstandard probes
from os import name
import numpy as np
import pandas as pd
import dxfgrabber
import ezdxf
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

