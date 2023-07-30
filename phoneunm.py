str = input("enter the number in the format ((xxx)xxxx-xxxx)")
valid = len(str) == 13
position = 0
while valid and position < len(str):
    if position == 0:
        valid = str[position] == "("
    elif position == 4:
        valid = str[position] == ")"
    elif position == 8:
        valid = str[position] == "-"
    else:
        valid = str[position].isdigit()
    position += 1
if valid:
    print("the number is valid")
else:
    print(" the number not valid")
    
      
