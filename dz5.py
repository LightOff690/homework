import sqlite3

# Создаем базу данных и подключаемся к ней
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# Создаем таблицу "Salespeople"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Salespeople (
        id INTEGER PRIMARY KEY,
        sname TEXT,
        city TEXT,
        comm REAL
    )
''')

# Создаем таблицу "Customers"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        id INTEGER PRIMARY KEY,
        cname TEXT,
        city TEXT,
        rating INTEGER,
        id_sp INTEGER,
        FOREIGN KEY (id_sp) REFERENCES Salespeople (id)
    )
''')

# Сохраняем изменения и закрываем соединение с базой данных
conn.commit()
conn.close()
# сылка на фаил не открывалась 