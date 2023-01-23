class Animal:
    fur_color = "Orange"

    def speak(self):
        print("Roarrrrr!")

    def eat(self):
        pass

    def chase(self):
        pass

class Tiger(Animal):
    def speak(self):
        print("They're Great!")

class HouseCat(Animal):
    fur_color = "Gray"
    def speak(self):
        print("Meow")

tiger = Tiger()
tiger.speak()
cat = HouseCat()
cat.speak()
print(HouseCat.fur_color)