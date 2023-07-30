string = input ("enter string")

found = False
position = 0
while not found and position < len(string):
    if string[position].isdigit():
        found = True
    else:
        position= position+1
if found:
    print("First digit position", position)
else:
       print("string dose not contain a digit")