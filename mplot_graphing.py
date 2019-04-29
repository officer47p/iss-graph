import matplotlib.pyplot as plt
import numpy as np

# Just some configuration I found on forums for having a fullscreen view of the plot :)
plt.figure(num=None, figsize=(9.2, 6), dpi=200, facecolor='w', edgecolor='k')

lats = []
longs = []

file = open("coordinates_demo.csv", "r")
lines = file.readlines()

for line in lines:
    lats.append(float(eval(line)["pos"]["lat"]))
    longs.append(float(eval(line)["pos"]["lon"]))

plt.plot(longs, lats)
plt.show()
