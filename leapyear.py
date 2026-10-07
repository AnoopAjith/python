current_year=int(input("enter the cuurent year:"))
final_year=int(input("enter the final year:"))
year=[]
def leap_year():
    for i in range(current_year,final_year+1):
        if(i%4==0 and i%100!=0) or(i%400==0):
            year.append(i)
    print(year)
leap_year()    
