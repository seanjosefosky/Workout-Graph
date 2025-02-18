import random, consolidate, openpyxl, path

from openpyxl import load_workbook
import matplotlib.pyplot as plt
import numpy as np

path = path.path
wb = load_workbook(path)
ws = wb.active

# variables
dict = consolidate.vol_dict
titles = []
linecolor = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']
line = ['-', '--', '-.']

consolidate.Consolidate(ws)
consolidate.GetTitles(ws,titles)

# print(f"Date: {key[0]}, Title: {key[1]}, Sum: {total}")
for key, total in dict.items():
        t = 0       
        if key[1] == titles[t]:    
                l = 0 # Line design
                c = 0 # Line color
                plt.plot(key[0], t, f'o{linecolor[c]}{line[l]}')
                t += 1
                if c != len(linecolor):
                        c += 1
                else:
                        c = 0
                
print(titles)
print(dict)
plt.show()