Hour1 = int(input("enter the hour1:  "))
Mint1 = int(input("enter the mint2:  "))

Hour2 = int(input("enter the hour2:  "))
Mint2 = int(input("enter the mint2:  "))

if (Hour1 < Hour2):
    print (Hour1, "is fist")
else:
    if( Hour1 == Hour2):
    
        if (Mint1 <= Mint2):
            print (Hour1, ":",  Mint1 , "first")
        else:
            print(Hour2, "fist")
    else:
        print(Hour2)