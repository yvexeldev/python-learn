number = int(input("Enter a number: "))

if number > 10:
    print("Number is greater than 10")
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
    
isOdd = number % 2 != 0
if isOdd:
    print("Number is odd")
else:
    print("Number is even")
    