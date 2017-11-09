import os, csv

dataDIR = os.listdir("E:\\wow829\\100km")
matrix = []

for dir in dataDIR:
    a = open("E:\\wow829\\100km\\"+dir,"r")
    cr = csv.reader(a)
    b = open("E:\\wow829\\100km\\res\\"+"a"+dir,"w",newline='')
    cw = csv.writer(b, delimiter=',',quotechar=' ')
    for index, num in enumerate(cr):
        a1 = (float(num[4])+float(num[5]))*0.00038/2
        a2 = (float(num[8])+float(num[9]))*0.001067/2
        a3 = ((float(num[6])+float(num[7])+float(num[10])+
                  float(num[11])+float(num[12])+float(num[13])+
                  float(num[14]))*0.014543/7)
        a4 = a1+a2+a3
        num.append(a1)
        num.append(a2)
        num.append(a3)
        num.append(a4)
        cw.writerow(num)
    b.close()
    a.close()
            

            
            
