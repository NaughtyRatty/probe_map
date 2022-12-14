#create by LIL HANNAH 04/23/2021
# %%import
from os import name
import dxfgrabber
import ezdxf
import numpy as np
import pandas as pd
import my_f as fun

# %% get data
dxf = dxfgrabber.readfile("f:\\Projects\\channel_map_py\\dxfin\\jiada2.dxf")
doc = ezdxf.readfile("f:\\Projects\\channel_map_py\\dxfin\\jiada2.dxf")
#intan_channel_data = pd.read_csv("bga_intan1.csv")
#intan_channel_data = pd.read_csv("bluebga_intan.csv")
#intan_channel_data = pd.read_csv("0518map.csv")
intan_channel_data = pd.read_csv("f:\\Projects\\channel_map_py\\input\\scj.csv")
msp = doc.modelspace()

pad_per_row = 0
pad_n = 1
row = 0
BGA_distance = 0.5

xlist = []
ylist = []
clean_ylist = []

for e in dxf.entities:
        ylist.append(fun.cut((e.points[0][1]),5))
        ylist.append(fun.cut((e.points[-1][1]),5))

top_pad_y = max(ylist)
temp = top_pad_y

for e in dxf.entities:
    if fun.cut(e.points[0][1],5) == top_pad_y:
        xlist.append(fun.cut(e.points[0][0],5))
    elif fun.cut(e.points[-1][1],5) == top_pad_y:
        xlist.append(fun.cut(e.points[-1][0],5))

topleft_pad_x = min(xlist)

for i in ylist:
    if i not in clean_ylist:
        clean_ylist.append(i)

clean_ylist.sort(reverse=True)
clean_ylist = clean_ylist[:int(len(ylist)/(2*len(xlist)))]
array_y = np.array(clean_ylist)

dis_list = np.diff(array_y).tolist()
print(dis_list)




print("Row number:",len(clean_ylist))
print("Pad per row:",len(xlist))
print("Total pad number:",int(len(ylist)/2))
print("Top left x coordinate:",topleft_pad_x)
print("Top left y coordinate:",top_pad_y)



intan_map_dist=dict(zip(intan_channel_data['BGA'],intan_channel_data['Intan']))
print(intan_map_dist)
#intan_map_dist = {1: '32', 2: '33', 3: '29', 4: '30', 5: '98', 6: '97', 7: '94', 8: '95', 9: '35', 10: '36', 11: '34', 12: '28', 13: '100', 14: '99', 15: '92', 16: '93', 17: '37', 18: '38', 19: '27', 20: '26', 21: '102', 22: '101', 23: '90', 24: '91', 25: '39', 26: '40', 27: '25', 28: '24', 29: '104', 30: '103', 31: '88', 32: '89', 33: '41', 34: '42', 35: '23', 36: '22', 37: '106', 38: '105', 39: '86', 40: '87', 41: '43', 42: '44', 43: '21', 44: '20', 45: '108', 46: '107', 47: '84', 48: '85', 49: '45', 50: '46', 51: '19', 52: '18', 53: '110', 54: '109', 55: '82', 56: '83', 57: '47', 58: '48', 59: '17', 60: '16', 61: '112', 62: '111', 63: '80', 64: '81', 65: '49', 66: '50', 67: '15', 68: '14', 69: '114', 70: '113', 71: '78', 72: '79', 73: '51', 74: '52', 75: '13', 76: '12', 77: '116', 78: '115', 79: '76', 80: '77', 81: '53', 82: '54', 83: '11', 84: '10', 85: '118', 86: '117', 87: '74', 88: '75', 89: '55', 90: '56', 91: '9', 92: '8', 93: '120', 94: '119', 95: '72', 96: '73', 97: '57', 98: '58', 99: '7', 100: '6', 101: '122', 102: '121', 103: '70', 104: '71', 105: '59', 106: '60', 107: '5', 108: '4', 109: '124', 110: '123', 111: '68', 112: '69', 113: '61', 114: '1', 115: '3', 116: '2', 117: '126', 118: '125', 119: '66', 120: '67', 121: '63', 122: '62', 123: '0', 124: 'NA1', 125: 'NA2', 126: '127', 127: '65', 128: '64'}
#soft pcb
#intan_map_dist = {1: 39, 2: 37, 3: 35, 4: 33, 5: 96, 6: 94, 7: 92, 8: 90, 9: 40, 10: 38, 11: 36, 12: 34, 13: 95, 14: 93, 15: 91, 16: 89, 17: 47, 18: 45, 19: 43, 20: 41, 21: 88, 22: 86, 23: 84, 24: 82, 25: 48, 26: 46, 27: 44, 28: 42, 29: 87, 30: 85, 31: 83, 32: 81, 33: 50, 34: 49, 35: 24, 36: 25, 37: 104, 38: 105, 39: 80, 40: 79, 41: 52, 42: 51, 43: 22, 44: 23, 45: 106, 46: 107, 47: 78, 48: 77, 49: 54, 50: 53, 51: 20, 52: 21, 53: 108, 54: 109, 55: 76, 56: 75, 57: 56, 58: 55, 59: 18, 60: 19, 61: 110, 62: 111, 63: 74, 64: 73, 65: 58, 66: 57, 67: 16, 68: 17, 69: 112, 70: 113, 71: 72, 72: 71, 73: 60, 74: 59, 75: 14, 76: 15, 77: 114, 78: 115, 79: 70, 80: 69, 81: 62, 82: 61, 83: 12, 84: 13, 85: 116, 86: 117, 87: 68, 88: 67, 89: 64, 90: 63, 91: 10, 92: 11, 93: 118, 94: 119, 95: 66, 96: 65, 97: 26, 98: 1, 99: 8, 100: 9, 101: 120, 102: 121, 103: 128, 104: 103, 105: 28, 106: 27, 107: 6, 108: 7, 109: 122, 110: 123, 111: 102, 112: 101, 113: 30, 114: 29, 115: 4, 116: 5, 117: 124, 118: 125, 119: 100, 120: 99, 121: 32, 122: 31, 123: 2, 124: 3, 125: 126, 126: 127, 127: 98, 128: 97}
###blue hard pcb
#intan_map_dist = {128: 32, 127: 31, 120: 30, 119: 29, 112: 28, 111: 27, 104: 26, 37: 25, 38: 24, 45: 23, 46: 22, 53: 21, 54: 20, 61: 19, 62: 18, 69: 17, 70: 16, 77: 15, 78: 14, 85: 13, 86: 12, 93: 11, 94: 10, 101: 9, 102: 8, 109: 7, 110: 6, 117: 5, 118: 4, 125: 3, 126: 2, 103: 1, 5: 33, 13: 34, 6: 35, 14: 36, 7: 37, 15: 38, 8: 39, 16: 40, 21: 41, 29: 42, 22: 43, 30: 44, 23: 45, 31: 46, 24: 47, 32: 48, 39: 49, 40: 50, 47: 51, 48: 52, 55: 53, 56: 54, 63: 55, 64: 56, 71: 57, 72: 58, 79: 59, 80: 60, 87: 61, 88: 62, 95: 63, 96: 64, 4: 96, 12: 95, 3: 94, 11: 93, 2: 92, 10: 91, 1: 90, 9: 89, 20: 88, 28: 87, 19: 86, 27: 85, 18: 84, 26: 83, 17: 82, 25: 81, 34: 80, 33: 79, 42: 78, 41: 77, 50: 76, 49: 75, 58: 74, 57: 73, 66: 72, 65: 71, 74: 70, 73: 69, 82: 68, 81: 67, 90: 66, 89: 65, 121: 97, 122: 98, 113: 99, 114: 100, 105: 101, 106: 102, 97: 103, 36: 104, 35: 105, 44: 106, 43: 107, 52: 108, 51: 109, 60: 110, 59: 111, 68: 112, 67: 113, 76: 114, 75: 115, 84: 116, 83: 117, 92: 118, 91: 119, 100: 120, 99: 121, 108: 122, 107: 123, 116: 124, 115: 125, 124: 126, 123: 127, 98: 128}
#sanchaji
#intan_map_dist = {1:106,2:103,3:100,4:97,5:None,6:29,7:26,8:23,9:105,10:102,11:99,12:96,13:None,14:28,15:25,16:22,17:104,18:101,19:98,20:None,21:None,22:27,23:24,24:21,25:109,26:108,27:107,28:16,29:17,30:20,31:19,32:18,33:122,34:119,35:116,36:113,37:14,38:11,39:8,40:5,41:121,42:118,43:115,44:112,45:13,46:10,47:7,48:4,49:120,50:117,51:114,52:15,53:12,54:9,55:6,56:3,57:125,58:124,59:123,60:126,61:127,62:2,63:1,64:0,65:85,66:88,67:91,68:94,69:33,70:36,71:39,72:42,73:86,74:89,75:92,76:95,77:34,78:37,79:40,80:43,81:87,82:90,83:93,84:32,85:35,86:38,87:41,88:44,89:82,90:83,91:84,92:81,93:80,94:45,95:46,96:47,97:69,98:72,99:75,100:78,101:49,102:52,103:55,104:58,105:70,106:73,107:76,108:79,109:50,110:53,111:56,112:59,113:71,114:74,115:77,116:48,117:51,118:54,119:57,120:60,121:66,122:67,123:68,124:65,125:64,126:61,127:62,128:63}

# %% main code


channel_map_x = []
channel_map_y = []
channel_map_n = []
while pad_n < len(ylist)/2+1 and row <= len(dis_list):
    #print(len(ylist) / 2 + 1)
    #print(len(dis_list))
    #print(len(xlist))
    #print(pad_per_row)

    if pad_per_row == len(xlist):
        temp += dis_list[row]
        pad_per_row = 0
        row += 1


    for e in dxf.entities:
        e1 = fun.cut(e.points[0][1],5)
        e2 = fun.cut(e.points[-1][1],5)


        #print(e.points)
        if e1 == temp:
            print('row:',row+1)
            print('Pad:', row * 8 + 1 + int(round((fun.cut(e.points[0][0], 5) - topleft_pad_x) / 0.5)))
            #print('pad:', pad_n)
            #print(e.points[0], e.points[-1])
            #print(e.points[0][0], e.points[0][1], e.points[0], e.points[-1]
            print('x:',fun.cut((e.points[0][0]),5))
            print('y:',temp,'\n')
            pad_n += 1
            pad_per_row += 1
            #fun.add_pad_channel_number(msp,BGA_distance,topleft_pad_x,top_pad_y,e.points[0][0],e.points[0][1], e.points[0], e.points[-1])
            fun.add_intan_channel_number(msp,BGA_distance,topleft_pad_x,top_pad_y,e.points[0][0], e.points[0][1], e.points[0], e.points[-1],intan_map_dist)
            channel_map_x.append(fun.cut((e.points[-1][0]), 1))
            channel_map_y.append(fun.cut((e.points[-1][1]), 2))
            channel_map_n.append(intan_map_dist[int(round
            ((e.points[0][0] - topleft_pad_x + BGA_distance) * 2 + (top_pad_y - e.points[0][1]) * 16))])
        elif e2 == temp:
            print('row:', row+1)
            print('Pad:',row*8+1+int(((fun.cut(e.points[-1][0], 5) - topleft_pad_x) / 0.5)))
            #print("pad:", pad_n)
            #print(e.points[-1], e.points[0])
            
            print('x:',fun.cut((e.points[-1][0]),5))
            print('y:',temp,'\n')
            #print(e.points[0][0], e.points[0][1], e.points[0], e.points[-1])
            pad_n += 1
            pad_per_row += 1
            #fun.add_pad_channel_number(msp,BGA_distance,topleft_pad_x,top_pad_y,e.points[-1][0], e.points[-1][1], e.points[0], e.points[-1])
            fun.add_intan_channel_number(msp,BGA_distance,topleft_pad_x,top_pad_y,e.points[-1][0], e.points[-1][1], e.points[0], e.points[-1],intan_map_dist)
            channel_map_x.append(fun.cut((e.points[1][0]), 1))
            channel_map_y.append(fun.cut((e.points[1][1]), 2))
            channel_map_n.append(intan_map_dist[int(round
                                                    ((e.points[-1][0] - topleft_pad_x + BGA_distance) * 2 + (
                                                                top_pad_y - e.points[-1][1]) * 16))])
doc.saveas("f:\\Projects\\channel_map_py\\dxfout\\jiada2_map.dxf")
#doc.saveas("the_map.dxf")
name = 'kkk_map.csv'
print(channel_map_x)
#fun.save_map_csv(channel_map_x, channel_map_y, channel_map_n,name)


