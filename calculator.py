def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def multi(a,b):
    return a * b

def div(a,b):
    return a / b


print("select operation : \n 1: addition \n 2: subtraction \n 3: multiply \n 4: divition")


choice = input("Enter choice(1 or 2 or 3 or 4):" )

num1 = int(input("enter the first number: "))
num2 = int(input("enter the last number: "))

if choice == '1':
   print(num1, "+", num2,"=" , add(num1,num2))

elif choice == '2':
    print(num1, "-", num2, "=", sub(num1, num2))

elif choice == '3':
    print(num1, "x", num2, "=", multi(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", div(num1, num2))

else :
    print("Invalid Number")



