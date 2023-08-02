"""input_file = open("infile.txt", "r")
line = input_file.readline() #this to read each line 
print(line)
input_file.close()
# this for read all lines use loop to visit each line and read
for line in input_file:
    if int(line) % 2 == 0:  # when we want calaulat in file we need change int() , float()
        print(line)"""


input_file = open("input.txt", "w")
input_file.write("6") #this to read each line 
input_file.close()