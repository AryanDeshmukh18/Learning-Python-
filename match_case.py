a = int(input("Enter your lucky number"))
match a:
    case 1:
        print("You Won a charger")
    case 3:
        print("You won 3$")
    case 6:
        print('You won 10$')
    case 9:
        print('You won a car')
    case _:
        print("Better luck next time")    