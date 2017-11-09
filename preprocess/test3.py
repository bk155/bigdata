from os import rename, listdir
import os
import gzip
import tarfile
import csv

def fighting(dicpath):
    index = 0
    matrix = []
    DTGdir = os.listdir(dicpath)
    for dir in DTGdir:
        a = open(dicpath+dir,"r")
        for num in a :
            a = num.split('|')
            if(a[3]==str(11)):

                c = [a[4],a[7]]

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
