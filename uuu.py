import random

#print(result.isalnum())

while 1:
    a = random.randint(1,10)
    b = random.randint(1,10)
    add= a + b
    print("number 1 ", a)
    print("number 2 ", b)
    result=input("enter result:")
  
#int input("result: ", add)
    if (result != "Q"):
        if (add == int(result)):
            print("correct")
        else:
            print("error")
        
    else:
        break 
      