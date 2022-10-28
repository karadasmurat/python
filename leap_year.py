# In the Gregorian calendar, a normal year consists of 365 days. 
# Because the actual length of a sidereal year (the time required for the Earth to revolve once about the Sun) is actually 365.2425 days, 
# a "leap year" of 366 days is used once every four years to eliminate the error caused by three normal (but short) years. 
# Any year that is evenly divisible by 4 is a leap year: 
# 
# However, there is still a small error that must be accounted for. 
# To eliminate this error, the Gregorian calendar stipulates that a year that is evenly divisible by 100 
# (for example, 1900) is a leap year only if it is also evenly divisible by 400.



def is_leap_year(year):

    leap = False
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    if year % 100 == 0 and year % 400 == 0:
        leap = True;
    
    return leap

years = [1600, 1700, 1800, 1900, 1996, 2000, 2100, 2200, 2300, 2400]
for y in years:
    print(f"{y}: {is_leap_year(y)}")