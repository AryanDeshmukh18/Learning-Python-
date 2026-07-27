def decorator (func):
    def wrapper():
        print("I am about to execute the function.")
        func()
        print("I have executed the function.")
    return wrapper
def say_hello():
    print("Hello!")

f = decorator(say_hello)
f()