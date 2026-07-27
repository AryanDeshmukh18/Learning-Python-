try:
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))

    print("What kind of operation do you want to perform?")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")

    o = input("Enter Operation: ")

    match o:
        case "+":
            print(f"The addition is {a + b}")
        case "-":
            print(f"The subtraction is {a - b}")
        case "*":
            print(f"The multiplication is {a * b}")
        case "/":
            if b == 0:
                print("Cannot divide by zero.")
            else:
                print(f"The division is {a / b}")
        case default:
            print("Invalid operation.")

except ValueError:
    print("Please enter valid integers.")

except Exception as e:
    print("An error occurred:", e)
