class animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("generic animal sound")
class dog(animal):
    def speak(self):
        print("Woof!")
class cat(animal):
    def speak(self):
        print("Meow!")
my_dog = dog("Tommy")
my_cat = cat("Kitty")
print(my_dog.name)
print(my_cat.name)
my_dog.speak()
my_cat.speak()

