import os, csv

#DTGdir = os.listdir("E:\\wow829\\20170829 DTG\\result3")

#dada = open("C:\\Users\\변강륜\\Desktop\\ee\\-2009329258.csv", "r")
#csvD = reader(dada)

#for dir in DTGdir:
def station(ProcessedDTG)# '-2009329258.csv'
Result = open(ProcessedDTG,"r")
cr = csv.reader(Result)
count = 0
count2 = 0
for index, num in enumerate(cr):
    save = ''
    date = num[2]
    time = num[3]
    #print(date, time)
    #날짜 맞추고...
    if(date == str(170106) and 157734==int(num[8]) and count==0):#시점 157734
        global startT
        startT = time
        T = "시점 : "+startT[:-4]+"시"+startT[2:-2]+"분"+startT[4:]+"초"
        print(T)
        count = 1
        count2 = 0
        
    '''if(date != str(170106) or 130600 != int(num[8])):#종점 130600
        endT = save
        print(save)'''
        
            
    if(date == str(170106) and 130600 == int(num[8]) and count2 == 0):
        T2 = "종점 : "+time[:-4]+"시"+time[2:-2:]+"분"+time[4:]+"초"
        T = "시점 : "+startT[:-4]+"시"+startT[2:-2]+"분"+startT[4:]+"초"
        a = (int(time[:-4])-int(startT[:-4]))*3600
        b = (int(time[2:-2])-int(startT[2:-2:]))*60
        c = int(time[4:])-int(startT[4:])
        R = a+b+c
        Ti = R/3600
        Mi = (R%3600)/60
        Se = ((R%3600)%60)
        print(T2)
        M = "경과 : "+str(int(Ti))+"시"+str(int(Mi))+"분"+str(Se)+"초\n"
        print(M)
        
        count = 0
        count2 = 1

        

Result.close()
#소요시간 계산
#"E:\\wow829\\20170829 DTG\\result3\\-2009329258.csv" DTG데이터  
