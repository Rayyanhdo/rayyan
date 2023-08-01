def readDate():
    print("enter a date : ")
    month = int(input("month: "))
    day = int(input("day: "))
    year = int(input("year: "))
    return (month, day, year)

date = readDate()
print(date)
(month, day, year) = readDate()
print(month, day, year)

