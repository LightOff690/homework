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

def add_salesperson():
    sname = input("Введите имя продавца: ")
    city = input("Введите город продавца: ")
    comm = float(input("Введите комиссионные продавца: "))
    cursor.execute('INSERT INTO Salespeople (sname, city, comm) VALUES (?, ?, ?)', (sname, city, comm))
    conn.commit()
    print("Продавец добавлен успешно.")

def add_customer():
    cname = input("Введите имя заказчика: ")
    city = input("Введите город заказчика: ")
    rating = int(input("Введите рейтинг заказчика: "))
    id_sp = int(input("Введите номер продавца, который обслуживает этого заказчика: "))
    cursor.execute('INSERT INTO Customers (cname, city, rating, id_sp) VALUES (?, ?, ?, ?)', (cname, city, rating, id_sp))
    conn.commit()
    print("Заказчик добавлен успешно.")

def edit_salesperson():
    salesperson_id = int(input("Введите ID продавца, которого вы хотите отредактировать: "))
    sname = input("Введите новое имя продавца: ")
    city = input("Введите новый город продавца: ")
    comm = float(input("Введите новые комиссионные продавца: "))
    cursor.execute('UPDATE Salespeople SET sname=?, city=?, comm=? WHERE id=?', (sname, city, comm, salesperson_id))
    conn.commit()
    print("Продавец отредактирован успешно.")

def edit_customer():
    customer_id = int(input("Введите ID заказчика, которого вы хотите отредактировать: "))
    cname = input("Введите новое имя заказчика: ")
    city = input("Введите новый город заказчика: ")
    rating = int(input("Введите новый рейтинг заказчика: "))
    id_sp = int(input("Введите новый номер продавца, который обслуживает этого заказчика: "))
    cursor.execute('UPDATE Customers SET cname=?, city=?, rating=?, id_sp=? WHERE id=?', (cname, city, rating, id_sp, customer_id))
    conn.commit()
    print("Заказчик отредактирован успешно.")

def delete_salesperson():
    salesperson_id = int(input("Введите ID продавца, которого вы хотите удалить: "))
    cursor.execute('DELETE FROM Salespeople WHERE id=?', (salesperson_id,))
    conn.commit()
    print("Продавец удален успешно.")

def delete_customer():
    customer_id = int(input("Введите ID заказчика, которого вы хотите удалить: "))
    cursor.execute('DELETE FROM Customers WHERE id=?', (customer_id,))
    conn.commit()
    print("Заказчик удален успешно.")

while True:
    print("\nМеню:")
    print("1. Добавить продавца")
    print("2. Добавить заказчика")
    print("3. Редактировать продавца")
    print("4. Редактировать заказчика")
    print("5. Удалить продавца")
    print("6. Удалить заказчика")
    print("7. Выйти")

    choice = input("Введите номер действия: ")

    if choice == '1':
        add_salesperson()
    elif choice == '2':
        add_customer()
    elif choice == '3':
        edit_salesperson()
    elif choice == '4':
        edit_customer()
    elif choice == '5':
        delete_salesperson()
    elif choice == '6':
        delete_customer()
    elif choice == '7':
        break
    else:
        print("Некорректный ввод. Пожалуйста, выберите действие из меню.")

# Закрываем соединение с базой данных
conn.close()