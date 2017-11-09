from os import rename, listdir
import os
import gzip
import tarfile
import csv

csvB = open("C:\\Users\\변강륜\\Desktop\\경기도정류장\\Station.csv","r")
read = csv.reader(csvB)

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

writeFile = open("C:\\Users\\변강륜\\Desktop\\경기도정류장\\"
                        +"StationSquare"+".csv","w",newline='')
newW = csv.writer(writeFile, delimiter=',',quotechar=' ')
for line in read:
    #print(line[])
    a = float(line[5])#36....
    b = float(line[4])#127....
    i = 0
    j = 0
    while a>= lat[i+1] and i<400:
        i += 1
        while b>= lon[j+1] and j<400:
            j += 1
        
    squre=(i)*400+(j)
    
    if(squre >= 160000 or squre == 0):
        squre = 99999999
    c = [line[0],line[1],line[2],line[3],str(a),str(b),line[6],line[7],line[8],str(squre)]
    #print(c)
    newW.writerow(c)

writeFile.close()
csvB.close()
        
