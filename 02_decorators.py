def decorator(func):
    def wrapper():
        print("Something will happen")
        func()
        print("Something has happened")
    return wrapper


@decorator
def my_hello():
    print("Hello!")


my_hello()