class Person:
    def __init__(self, fullName, age):
        self.__fullName = fullName
        self.__age = age

    def move(self):
        print(f'{self.__fullName} говорит')

    def talk(self):
        print(f'{self.__fullName} говорит')

    def getFullName(self):
        return self.__fullName

    def setFullName(self, fullName):
        self.__fullName = fullName

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age


person1 = Person("Иван Иванов", 25)
person2 = person = Person("Петр Петров", 30)

person1.move()
person2.talk()