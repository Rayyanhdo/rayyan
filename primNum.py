n = [] # list 
print("Number | primstiat")
for x in range(1, 31): # this for add the number inside the empty list 

    if x == 1:
        print(f"{x}|false")
    elif x > 1:
        prime = True
        
        for i in range(2, x):
            if x % i == 0:
                prime = False
                break
            
        if prime:
            print (f"{x}|true")
        else:
            print(f"{x}|false")