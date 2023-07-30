str = input("enter the cvv in the format xxxx-xxx")
valid = len(str) == 8
position = 0
while valid and position < len(str):
    if position == 4:
        valid = str [position] == "-"
    else:
        valid = str [position].isdigit()
    position += 1
if valid:
    print(" the string contain a cvv")
else:
    print (" the string not contain a cvv")