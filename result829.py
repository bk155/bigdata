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

def processingData(dicpath,result):
    index = 0
    matrix = []
    DTGdir = os.listdir(dicpath)
    #csvW = open("E:\\829result.csv","w",newline='')
    #cw = csv.writer(csvW, delimiter=',',quotechar=' ')
    for dir in DTGdir:
        a = open(dicpath+dir,"r")
        for num in a :
            a = num.split('|')
            if(a[3]==str(11)):
                k = a[21]
                day = k[0:6]
                time = k[6:12]
                loY = a[13][1:3]+"."+a[13][3:]#37...
                loX = a[12][0:3]+"."+a[12][3:]#127...
                c = [a[20],a[4],day, time,a[9],a[7],loY,loX]

                y = float(c[6]) #37...
                x = float(c[7]) #127...
                i = 0
                j = 0
                while y>= lat[i+1] and i<400:
                    i += 1
                    while x>= lon[j+1] and j<400:
                        j += 1
        
                squre=(i)*400+(j)

                if(squre >= 160000 or squre == 0):
                    squre = 99999999
                
                c.append(squre)
            
                if(index==0):
                    key = c[1]
                if(c[1]!=key):
                    writeFile = open(result
                                     +key+".csv","ab")
                    newW = csv.writer(writeFile, delimiter=',',quotechar=' ')
                    newW.writerows(matrix)
                    writeFile.close()
                    matrix = []
                    key = c[1]
                if(c[1] == key):
                    matrix.append(c)
                index += 1
    a.close()

def busRouteProcess(stationInfoPath, resultFile):
    csvB = open(stationInfoPath,"r")
    read = csv.reader(csvB)

    writeFile = open(resultFile,"w",newline='')
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

def readRouteData(filePath, result):
    a = open(filePath,"r")
    b = a.readline()
    c = b.split("^")

    csvR = open(result,"w",newline='')
    cw = csv.writer(csvR,  delimiter=',',quotechar=' ')

    for num in c:
    d = num.split("|")
    cw.writerow(d)

    csvR.close()
    a.close()

def timeLapse():
    


processingData("E:\\wow829\\20170829 DTG\\data\\dtg\\","E:\\wow829\\20170829 DTG\\result3\\")
busRouteProcess("C:\\Users\\변강륜\\Desktop\\경기도정류장\\Station.csv","C:\\Users\\변강륜\\Desktop\\경기도정류장\\"
                        +"StationSquare"+".csv")
readRouteData("C:\\Users\\변강륜\\Desktop\\경기도정류장\\route20170829.txt", "C:\\Users\\변강륜\\Desktop\\경기도정류장\\Route.csv")
