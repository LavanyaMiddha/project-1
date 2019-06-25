#Question 1

import csv
m_age=100
f_age=100
with open("athlete_events.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=",")
    for row in reader:
        data=dict(row)
        if(data['Age']=='NA'):
            continue
        elif(data['Year']=='1996'):
            if(data['Sex']=='M'):
                if(int(data['Age'])< m_age):
                    m_age=int(data['Age'])
            elif(data['Sex']=='F'):
                if(int(data['Age'])< f_age):
                    f_age=int(data['Age'])
print("In the 1996 Olympics") 
print("The youngest male participants was:",m_age,"years")
print("The youngest female participant was:",f_age,"years")
        
csvfile.close()

#Question 2
import csv
s_name=set()
s_gymn=set()

with open("athlete_events.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=",")
    for row in reader:
        data=dict(row)
        if(data['Sex']=='M' and data['Year']=='2000'):
            s_name.add(data['Name'])
            if(data['Sport']=='Gymnastics'):
                s_gymn.add(data['Name'])
    per=(len(s_gymn)/len(s_name))*100

print("The percentage of male Gymnasts is:",round(per,1),"%")
csvfile.close()

#Question 3
import csv
SUM=0
height=list()
stand=list()
#question 2
with open("athlete_events.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=",")
    for row in reader:
        data=dict(row)
        if(data['Sex']=='F' and data['Year']=='2000' and data['Sport']=='Basketball' and data['Height']!='NA'):
            height.append(int(data['Height']))
    mean=sum(height)/len(height)
    mean=round(mean,1)
    for x in height:
        x=int(x)
        a=(x-mean)**2
        stand.append(a)
    standard=(sum(stand)/len(stand))**(0.5)
    standard=round(standard,1)
print("The mean is:",mean)
print("The Standard Deviation is:",standard)
csvfile.close()

#Question 4
import csv
weight=-1
#question 2
with open("athlete_events.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=",")
    for row in reader:
        data=dict(row)
        if(data['Year']=='2002' and data['Weight']!='NA'):
            if(float(data['Weight'])> weight):
                name=data['Name']
                sport=data['Sport']
print("The name of the sportsperson is:",name)
print("The sport played by him is:",sport)
csvfile.close()

#Question 5
import csv
year=set()
with open("athlete_events.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=",")
    for row in reader:
        data=dict(row)
        if(data['Name']=='Pawe Abratkiewicz'):
            year.add(data['Year'])
print("The number of times Pawe Abratkiewicz participateed in Olympics is:",len(year))
csvfile.close()

#Question 6
import csv
count=0
with open("athlete_events.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=",")
    for row in reader:
        data=dict(row)
        if(data['Year']=='2000' and data['Sport']=='Tennis' and data['Team']=='Australia'):
            if(data['Medal']=='Silver'):
                count=count+1
print("The number of Silver medals won are:",count)
csvfile.close()

#Question 7
import csv
swit=0
serb=0
with open("athlete_events.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=",")
    for row in reader:
        data=dict(row)
        if(data['Year']=='2016'):
            if(data['Medal']!='NA' and data['Team']=='Switzerland'):
                swit=swit+1
            elif(data['Medal']!='NA' and data['Team']=='Serbia'):
                serb=serb+1
    if(swit>serb):
        print('Yes')
    else:
        print('No')
csvfile.close()

#Question 8
import csv
c1=0
c2=0
c3=0
c4=0
with open("athlete_events.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=",")
    for row in reader:
        data=dict(row)
        if(data['Year']=='2014' and data['Age']!='NA'):
            if(15<= int(data['Age']) <=25):
                c1=c1+1
            elif(25<= int(data['Age']) <=35):   
                c2=c2+1
            elif(35<= int(data['Age']) <=45):
                c3=c3+1
            if(45<= int(data['Age']) <=55):
                c4=c4+1
print(c1)
print(c2)
print(c3)
print(c4)
print("fewest participants were from the age-group [45-55]")
print("Most participants were from the age-group [15-25]")
csvfile.close()


#Question 9
import csv
flag1=0
flag2=0
with open("athlete_events.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=",")
    for row in reader:
        data=dict(row)
        if(data['City']=='Lake Placid' and data['Season']=='Summer'):
            flag1=1
        elif(data['City']=='Sankt Moritz' and data['Season']=='Winter'):
            flag2=1
if(flag1==1):
    print("YES")
else:
    print("NO")
if(flag2==1):
    print("YES")
else:
    print("NO")

csvfile.close()


#Question 10
import csv
s1996=set()
s2016=set()
#question 2
with open("athlete_events.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=",")
    for row in reader:
        data=dict(row)
        if(data['Year']=='1996'):
            s1996.add(data['Sport'])
        if(data['Year']=='2016'):
            s2016.add(data['Sport'])
print("The number of unique sports are:",abs(len(s2016)-len(s1996))) 
csvfile.close()
