from os import rename, listdir
import os
import gzip
import tarfile
import csv

'''dataF = tarfile.open("E:\\새 폴더\\20170829 DTG\\dps_10.tar","r")
d = dataF.extractall("E:\\새 폴더\\20170829 DTG\\data")
dataF.close'''
'''lis = []
DTGdir = os.listdir("E:\\새 폴더\\20170829 DTG\\data")
for dir in DTGdir:
    gzF = gzip.open("E:\\새 폴더\\20170829 DTG\\data\\"+dir,"rb")
    for num, data in enumerate(gzF):
        d = gzF.extractall("E:\\새 폴더\\20170829 DTG\\data\\")
        #line = gzF.readline()
        #print(line)
        #print(a[0])
        #lis.append(line)
        #print(lis[num].split('|'))'''
'''b = line.split('|')
        k = b[21]
        day = k[0:6]
        time = k[6:12]
        loY = b[13][1:3]+"."+b[13][3:]#37...
        loX = b[12][0:3]+"."+b[12][3:]#127...
    
        c = [b[20],b[4],day, time,b[9],loY,loX]
        print(c)'''

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
    
def fighting(dicpath):
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
                    writeFile = open("E:\\wow829\\20170829 DTG\\result3\\"
                                     +key+".csv","ab")
                    newW = csv.writer(writeFile, delimiter=',',quotechar=' ')
                    newW.writerows(matrix)
                    writeFile.close()
                    matrix = []
                    key = c[1]
                if(c[1] == key):
                    matrix.append(c)
                index += 1

                
            #cw.writerow(c)
    #csvW.close()


    a.close()

fighting("E:\\wow829\\20170829 DTG\\data\\dtg\\")
