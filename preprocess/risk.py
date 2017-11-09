from os import rename, listdir
import os
import gzip
import tarfile
import csv

lat = [0]*402#세로
lon = [0]*402#가로

maxA = 127.708141
maxB = 37.797130
minA = 126.372253
minB = 36.906024#y최소
p = 0
l = 0

squre = 99999999

for i in range(0,401):
    p = 0.002 * i
    lat[i] = minB+p

for i in range(0,401):
    l = 0.003 * i
    lon[i] = minA+l


a = 37.693138#36....
b = 126.776015#157734
i = 0
j = 0
while a>= lat[i+1] and i<400:
    i += 1
    while b>= lon[j+1] and j<400:
        j += 1
        
squre=(i)*400+(j)
    
if(squre >= 160000 or squre == 0):
    squre = 99999999

print(squre)
