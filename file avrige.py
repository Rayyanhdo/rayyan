input_file = open("set.txt", "r")


#calculat the avrege of the number in file txt 
averge = 0 
total = 0
count = 0
for line in input_file:
    total+= float(line)
    count+=1
    averge = total /count
print(averge)
print(total)
    
