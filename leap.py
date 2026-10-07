import datetime
year1=datetime.date.today().year
print("current year",year1)
year=int(input("enter the last year"))
for i in range(year1,year):
    if(i%4==0 and i%100!=0 or i%400==0):
        print(i)
