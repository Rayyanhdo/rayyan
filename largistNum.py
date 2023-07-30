n1 = int(input(" enter the number 1: "))
n2 = int(input(" enter the number 2: "))
n3 = int(input(" enter the number 3: "))

def largist(n1,n2,n3):
    if (n1 > n2 and n1> n3):
          return n1
    elif (n2 > n1 and n2> n3):
          return n2
    else:
        return n3
 
    return largist
largist_number = largist(n1,n2,n3)
print("the largist number ", largist_number)
    

