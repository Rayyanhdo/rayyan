state = input("enter y or n: ")
age = int(input("enter your age: "))

if(age >= 18):
    if(state == "y"):
         print("graduated & 18 above years old")
    else:
         print("not graduated & 18 above years old")
else:
    print("under 18 yeas")
    
   
    