import csv

a = open("C:\\Users\\변강륜\\Desktop\\경기도정류장\\route20170829.txt","r")
b = a.readline()
c = b.split("^")

csvR = open("C:\\Users\\변강륜\\Desktop\\경기도정류장\\Route.csv","w",newline='')
cw = csv.writer(csvR,  delimiter=',',quotechar=' ')

for num in c:
    d = num.split("|")
    cw.writerow(d)

csvR.close()
a.close()
