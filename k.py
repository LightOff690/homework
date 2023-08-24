class A:     
 def method_a(self):               
  print("Method A from class A")

class B:
    def method_b(self):
        print("Method B from class B")

class C(A, B):
    def method_c(self):     
       print("Method C from class C")

# Создаем объект класса C
obj = C()


obj
# Методы от класса A
obj.method_a()

# Методы от класса B
obj.method_b()


obj.method
# Методы от класса C
obj.method_c()