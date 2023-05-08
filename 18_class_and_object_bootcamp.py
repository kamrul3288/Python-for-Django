# a class is a template definition of the methods and variables in a particular kind of object

class Greeting:
    def greeting(self):
        print("Hello From greeting")


greet = Greeting()
greet.greeting()


class Robot:
    #create constructor
    def __init__(self, name: str, color: str, weight: int):
        self.name = name
        self.color = color
        self.weight = weight

    # it's a private
    __power = 10

    def introduce_self(self):
        print("My name is " + self.name)
        print("My color is " + self.color)
        print("My weight is ", self.weight)
        print("My Power is ", self.__power)


r1 = Robot(name="Optimus Prime", color="Blue", weight=1000)
r1.introduce_self()

r2 = Robot(name="Bumblebee", color="Yellow", weight=500)
r2.introduce_self()

# Inheritance
class Transformer(Robot):
    value = 10


t1 = Transformer(name="Optimus Prime", color="Blue", weight=1000)
print(t1.introduce_self())
