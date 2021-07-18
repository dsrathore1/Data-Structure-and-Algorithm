"""
In the Gregorian calendar, three conditions are used to identify leap years:

#! The year can be evenly divided by 4, is a leap year, unless:
    #! The year can be evenly divided by 100, it is NOT a leap year, unless:
        #! The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

"""


def is_year(year):

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return('this is an leap year')
            else:
                return('This not an leap year')
        else:
            return('Is an leap year')
    else:
        return('It in not an leap year')


year = int(input('Enter your leap year: '))

print(is_year(year))
