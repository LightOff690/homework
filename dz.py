import random

class Student:
    def __init__(self, name):
        self.name = name
        self.id = random.randint(1, 100)  # Генерация случайного числа от 1 до 100

    def __repr__(self):
        return f"Student(name='{self.name}', id={self.id})"

# Создание списка студентов
students = [
    Student("A"),
    Student("B"),
    Student("C"),
    Student("D"),
    Student("E")
]

# Сортировка списка студентов по убыванию атрибута id
students.sort(key=lambda student: student.id, reverse=True)

# Вывод отсортированного списка студентов
for student in students:
    print(student)
#Пример вывода:
Student(name='A', id=92)
Student(name='B', id=85)
Student(name='C', id=76)
Student(name='D', id=59)
Student(name='E', id=12)
