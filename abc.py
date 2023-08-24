from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} says Meow!"

# Попробуем создать экземпляр абстрактного класса - вызовет ошибку
# animal = Animal("Generic Animal")

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.make_sound())
print(cat.make_sound())