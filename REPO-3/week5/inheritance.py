# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Some generic animal sound")

    def info(self):
        print(f"I am a {self.species} named {self.name}")

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
    
    def make_sound(self):
        print("Woof! Woof!")
    
    def info(self):
        super().info()
        print(f"I am a {self.breed}")

# Another child class inheriting from Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color
    
    def make_sound(self):
        print("Meow! Meow!")
    
    def info(self):
        super().info()
        print(f"I have {self.color} fur")

# Creating instances of Dog and Cat
dog = Dog(name="Buddy", breed="Golden Retriever")
cat = Cat(name="Whiskers", color="black")

# Calling methods
dog.info()
dog.make_sound()

cat.info()
cat.make_sound()
