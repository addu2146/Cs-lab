def is_leap(year):
    
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

def days_in_month(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        return 29 if is_leap(year) else 28
    else:
        return "Invalid month"

year = int(input("Enter a year: "))
month = int(input("Enter a month (1-12): "))

days = days_in_month(month, year)
print(f"The number of days in month {month} of year {year} is {days}.")

