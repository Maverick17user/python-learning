def isLeap(year):
    dividedBy4 = year % 4 == 0
    dividedBy100 = year % 100 == 0
    dividedBy400 = year % 400 == 0

    if dividedBy4 or (dividedBy100 and dividedBy400):
        print("It's a leap year")
    else:
        print("It's a usual year")

isLeap(1900)