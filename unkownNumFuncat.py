# when we want send unkown number we call inside the funcation (*n)
def total(*n):
    sums = 0
 
    for t in n:
        sums = sums + t
        
    return sums

result1 = total(1, 2, 3)
print(round(result1))