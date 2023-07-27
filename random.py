import random
result = ""
#print(result.isalnum())

while(result != "Q"):
    a = random.randint(1,10)
    b = random.randint(1,10)
    add= a + b
    print("number 1 ", a)
    print("number 2 ", b)
    result=input("enter result:")
    print(result)
#int input("result: ", add)
    if (result.isalnum()):
        if (add == int(result)):
            print("correct")
        else:
            print("error")
        result=input("enter result:")
        
  