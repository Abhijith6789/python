def loop_year(year):
    x = 0
    while x < 20:
        if year % 4 != 0 and year % 400 != 0:
            year +=1
            ##print("%s is a common year") %(year)
        elif year % 100 != 0:
            year +=1
            print("%s is a leap year") % (year)
            x += 1
