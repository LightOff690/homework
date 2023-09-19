import sqlite3

# Создаем базу данных и подключаемся к ней
conn = sqlite3.connect('shopIT.db')
cursor = conn.cursor()

# Создаем таблицу "Компьютеры"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Компьютеры (
        id INTEGER PRIMARY KEY,
        тип TEXT,
        бренд TEXT,
        стоимость INTEGER
    )
''')

# Добавляем данные в таблицу
cursor.execute('INSERT INTO Компьютеры (тип, бренд, стоимость) VALUES (?, ?, ?)', ('ноутбук', 'HP', 35000))
cursor.execute('INSERT INTO Компьютеры (тип, бренд, стоимость) VALUES (?, ?, ?)', ('стационарный компьютер', 'Dell', 45000))
cursor.execute('INSERT INTO Компьютеры (тип, бренд, стоимость) VALUES (?, ?, ?)', ('моноблок', 'HP', 55000))
cursor.execute('INSERT INTO Компьютеры (тип, бренд, стоимость) VALUES (?, ?, ?)', ('ноутбук', 'Lenovo', 28000))
cursor.execute('INSERT INTO Компьютеры (тип, бренд, стоимость) VALUES (?, ?, ?)', ('стационарный компьютер', 'HP', 42000))

# Сохраняем изменения
conn.commit()

# Запрос 1: Показать все компьютеры бренда "HP"
cursor.execute('SELECT * FROM Компьютеры WHERE бренд = "HP"')
computers_hp = cursor.fetchall()
print("Компьютеры бренда HP:")
for computer in computers_hp:
    print(computer)

# Запрос 2: Показать компьютеры стоимостью более 40000
cursor.execute('SELECT * FROM Компьютеры WHERE стоимость > 40000')
expensive_computers = cursor.fetchall()
print("\nКомпьютеры стоимостью более 40000:")
for computer in expensive_computers:
    print(computer)

# Запрос 3: Показать компьютеры типа "ноутбук" и стоимостью менее 30000
cursor.execute('SELECT * FROM Компьютеры WHERE тип = "ноутбук" AND стоимость < 30000')
affordable_laptops = cursor.fetchall()
print("\nНоутбуки со стоимостью менее 30000:")
for laptop in affordable_laptops:
    print(laptop)

# Закрываем соединение с базой данных
conn.close()