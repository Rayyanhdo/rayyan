weight = float(input("enter your weight by Kg: "))
height = float(input("enter your height by cm: "))

heigth_m = height / 100
BIM = (weight / (height)**2)
print (BIM)

if (BIM <= 18.5):
    print("under weight")
elif (18.5<= BIM <25.5):
    print("normal")
elif (25.5 <= BIM <30.5):
    print("over")
else:
    print("obase")