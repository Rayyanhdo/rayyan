str = input("enter th santenc:")
n=int(input("enter the number: "))

new_list = []
text = str.split(" ")
for x in text:
	if len(x) > n:
		new_list.append(x)
print(new_list)