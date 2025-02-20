year = int(input("Enter a year\n"))
if(year%400==0):
    print(f"{year} is a leap year")
elif(year%100==0):
    print(f"{year} is not a leap year")
elif(year%4==0):
    print(f"{year} is a leap year")
