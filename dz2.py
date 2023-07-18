import random

class Student:
    def __init__(self, name):
        self.name = name
        self.id = random.randint(1, 100)  # Генерация случайного числа от 1 до 100

    def __repr__(self):
        return f"Student(name='{self.name}', id={self.id})"

# Создание списка студентов
students = [
    Student("Alice"),
    Student("Bob"),
    Student("Charlie"),
    Student("David"),
    Student("Eve")
]

# Сортировка списка студентов по убыванию атрибута id
students.sort(key=lambda student: student.id, reverse=True)

# Вывод отсортированного списка студентов
for student in students:
    print(student)
#Пример вывода:
Student(name='David', id=92)
Student(name='Eve', id=85)
Student(name='Charlie', id=76)
Student(name='Bob', id=59)
Student(name='Alice', id=12)
