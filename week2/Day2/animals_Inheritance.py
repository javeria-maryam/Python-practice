# Parent class: Animal with method speak().
# Child classes:
# Dog → override speak() to print "Woof!".
# Cat → override speak() to print "Meow!".
# Bird → override speak() to print "Chirp!".
# Create a list of animals and loop through them, calling speak() on each.


class Animal:
    def speak(self):
        print("This animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")
class Cat(Animal):
    def speak(self):
        print("Meow!")
class Bird(Animal):
    def speak(self):
        print("Chirp!")

#List of animals
animals = [Animal(),Dog(),Cat(),Bird()]

#Looping through the list
for animal in animals:
    animal.speak()
    
