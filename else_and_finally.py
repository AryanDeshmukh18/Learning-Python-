a = int(input("Enter 1st no: "))
b = int(input("Enter 2nd no: "))
try:
    c = a/b
    print(c)
except Exception as e:
    print(e)
finally:
    print("This is always executed")