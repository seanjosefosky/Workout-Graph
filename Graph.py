import ScrapeExcel, random

import matplotlib.pyplot as plt
import numpy as np
import ScrapeExcel as data

# variables
dict = ScrapeExcel.dict
x = []
y = []
linecolor = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']
line = ['-', '--', '-.']

def getallkeys(dict):
    for key, value in dict.items():
        yield key
    if isinstance(value, dict):
        yield from getallkeys(value)


for x in getallkeys(dict):
    # x.append(key)
    # y.append(5)
    plt.plot(x, random.randint(200,500), f'o{random.choice(line)}{random.choice(linecolor)}')

plt.show()
