# Seconds in a year, including leap years.
days_this_year = int(input("How many days are in this year?"))

days_in_year = 365
days_in_leap_yaer = 366
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60

leapyear_reults = days_in_leap_yaer * hours_in_day * minutes_in_hour * seconds_in_minute

results = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute

if days_this_year  == 366:
 print("Number of seconds in a leap year are", leapyear_reults)
else:
 print("Number of seconds in a year are", results)
