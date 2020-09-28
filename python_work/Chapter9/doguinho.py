class Dog:
    """A simple attempt to model a dog"""
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulates a dog sitting command"""
        print(f'{self.name} is now sitting')

    def roll(self):
        """Simulates a dog roll command"""
        print(f'{self.name} is now rolling')


my_dog = Dog('Serena', 3)
my_otherdog = Dog('Mali', 12)
print(f"My Dog's name is {my_dog.name} and her age is {my_dog.age}")
print(f"My Dog's name is {my_otherdog.name} and her age is {my_otherdog.age}")

my_dog.sit()
my_otherdog.sit()
my_dog.roll()
