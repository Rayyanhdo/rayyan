import random

num = random.randint(0, 10)
guess = 0

while guess != num:
    guess = int(input("Enter the number : "))

    if (guess == num):
        print("that is correct number")
        break
    elif (guess > num):
        print(" the number is less")
    else:
        print ("the number is greter ")