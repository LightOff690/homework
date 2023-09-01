#public#

class MyClass:
    def public_method(self):
        print("Это публичный метод")
        
    def __init__(self):
        self.public_attribute = 10
#private#

my_object = MyClass()
my_object.public_method()
print(my_object.public_attribute)

#protected#
class MyClass:
    def __private_method(self):
        print("Это закрытый метод")
        
    def __init__(self):
        self.__private_attribute = 10

my_object = MyClass()
# my_object.__private_method() - вызывает ошибку
# print(my_object.__private_attribute) - вызывает ошибку

class MyClass:
    def _protected_method(self):
        print("Это защищенный метод")
        
    def __init__(self):
        self._protected_attribute = 10

class MySubClass(MyClass):
    def call_protected_method(self):
        self._protected_method()

my_object = MyClass()
# my_object._protected_method() - вызывает ошибку
# print(my_object._protected_attribute) - вызывает ошибку

my_sub_object = MySubClass()
my_sub_object.call_protected_method()