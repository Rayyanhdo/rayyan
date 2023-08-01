lis=[10,20,30,90]
limit = 90
position = 0

found = False
while position <len(lis) and not found:
    if lis[position] == limit:
        found = True
    else:
        position += 1
if found:
    print(" the position is : ", position)
else:
    print("not found")