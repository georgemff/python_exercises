# 12. Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.
import calendar

try:
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))

    print(calendar.month(year, month))
except:
    print('Something went wrong')