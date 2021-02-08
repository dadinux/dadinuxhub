#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
#c = calendar.TextCalendar(calendar.MONDAY)
#st = c.formatmonth(2021, 1, 0, 0)
#print(st)

# create an HTML formatted calendar
cc = calendar.HTMLCalendar(calendar.MONDAY)
sth = cc.formatmonth(2021,1)
print(sth)



# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for name in calendar.month_name:
    print(name)

for name in calendar.day_name:
    print(name)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms


# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

