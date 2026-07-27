a = int(input("Enter 1st no: "))
b = int(input("Enter 2nd no: "))

if b == 0:
    raise  ValueError("Please don't divide by 0")

print(f"The output is {a/b}")