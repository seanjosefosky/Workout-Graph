import random, consolidate, openpyxl, path

from openpyxl import load_workbook
import matplotlib.pyplot as plt
import numpy as np

path = path.path
wb = load_workbook(path)
ws = wb.active

# variables
dict = consolidate.vol_dict
linecolor = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']
line = ['-', '--', '-.']

consolidate.Consolidate(ws,path)


for key, total in dict.items():
        print(f"Date: {key[0]}, Title: {key[1]}, Sum: {total}")
        plt.plot(key[0], total, f'o{random.choice(line)}{random.choice(linecolor)}')

plt.show()