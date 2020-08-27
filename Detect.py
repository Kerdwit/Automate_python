#! python3
#Detect.py                  Program for Date Detection - JARUWIT KERDPHRA
"""
Problem

Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range
from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day
or month is a single digit, it’ll have a leading zero.

    The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept
nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and
year, and write additional code that can detect if it is a valid date. April, June, September, and November
have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap
years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year
is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized
regular expression that can detect a valid date.


Month have 30 days
April, June, September, and November
"""
import re

# Create a regex object for date detection (date format: DD/MM/YYYY)
DateRegex = re.compile(r'''
#Example 28/2/2999, 31/2/2020, 29/02/2020, 31/06/2021
(
#Group of Day number
([^0]|0[^0]|[1-2][0-9]|3[0-1])           # Range of date number 1-9 or 01-31
(\/)                                       # 1st slash

#Group of Month number
([^0]|0[^0]|1[1-2])                        # Range of month number 1-9 or 01-12
(\/)                                       # 2nd slash

#Group of Year number
([1-2]\d{3})                               # Range of year number 1000-2999
)''',re.VERBOSE)

result = DateRegex.findall('28/2/2999, 31/2/2020, 29/02/2020, 31/6/2021, 9/9/2020')

day = []
month = []
year = []


# Extract value from result to variable's list
for dayNumber in result:
    day.append(dayNumber[1])
for monthNumber in result:
    month.append(monthNumber[3])
for yearNumber in result:
    year.append(yearNumber[5])
print(day);print(month);print(year)

# Check leap year for add leap day in February and fulfill digit of February
for i in range(len(day)):
    #check leap year
    if (int(year[i])%100 == 0 and int(year[i])%400 != 0):  # This year is not leap year.
        continue
    elif int(year[i])%4 == 0:                                   # This year is leap year.
        if int(month[i]) == 2 and int(day[i]) >= 28:
            day[i] = '29'
            month[i] = '02'
    elif int(month[i])==2:
        month[i] = '02'


# TODO: Check count of Day's digit number and replace with valid value

for daynum in range(len(day)):
    if len(day[daynum])==1:
        day[daynum] = day[daynum].rjust(2,'0')



# Check count of Month's digit number and replace with valid value
lsMonthdetect = [4,6,9,11]
for monthnum in range(len(day)):
    if int(month[monthnum]) in lsMonthdetect and int(day[monthnum]) == 31:          # modify the 31th to the 30th
        day[monthnum]= '30'
    if len(month[monthnum]) == 1:                                    # modify digit number of month
        month[monthnum] = month[monthnum].rjust(2,'0')


print(day);print(month);print(year)



