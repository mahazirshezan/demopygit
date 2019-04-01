x = 4
try:
    print("resource open")
    y = int(input("enter a num: "))
    print(x/y)

except ZeroDivisionError as e:
    print("you cannot ", e)

except ValueError:
    print("invalid num")

finally:
    print("resource closed")

