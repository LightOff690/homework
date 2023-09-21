import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()
# Создание таблицы players и вставка данных
cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY,
        name TEXT,
        best_score INTEGER
    )
""")

players_data = [
    ("Миша", 200),
    ("Ваня", 154),
    ("Дима", 178),
    ("Коля", 210)
]

cursor.executemany("INSERT INTO players (name, best_score) VALUES (?, ?)", players_data)

# Создание таблицы games и вставка данных
cursor.execute("""
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY,
        name TEXT,
        score INTEGER,
        id_player INTEGER
    )
""")

games_data = [
    ("Миша", 110, 1),
    ("Миша", 200, 1),
    ("Дима", 178, 3),
    ("Коля", 10, 4),
    ("Коля", 30, 4),
    ("Коля", 40, 4),
    ("Ваня", 154, 2),
    ("Коля", 210, 4)
]

cursor.executemany("INSERT INTO games (name, score, id_player) VALUES (?, ?, ?)", games_data)

# Сохраните изменения в базе данных
conn.commit()
# Показать игроков и их количество игр
cursor.execute("""
    SELECT p.name, COUNT(g.id)
    FROM players p
    LEFT JOIN games g ON p.id = g.id_player
    GROUP BY p.name
""")
players_and_game_count = cursor.fetchall()
print("Игроки и их количество игр:")
for player in players_and_game_count:
    print(f"{player[0]}: {player[1]} игр")

# Показать игроков и их итоговый счет за все сыгранные игры
cursor.execute("""
    SELECT p.name, SUM(g.score)
    FROM players p
    LEFT JOIN games g ON p.id = g.id_player
    GROUP BY p.name
""")
players_and_total_score = cursor.fetchall()
print("\nИгроки и их итоговый счет:")
for player in players_and_total_score:
    print(f"{player[0]}: {player[1]} очков")

# Найти общее количество игр
cursor.execute("SELECT COUNT(*) FROM games")
total_games = cursor.fetchone()[0]
print(f"\nОбщее количество игр: {total_games}")

# Найти худший результат у каждого игрока
cursor.execute("""
    SELECT p.name, MIN(g.score)
    FROM players p
    LEFT JOIN games g ON p.id = g.id_player
    GROUP BY p.name
""")
worst_scores = cursor.fetchall()
print("Худшие результаты игроков:")
for player in worst_scores:
    print(f"{player[0]}: {player[1]} очков")

# Закрыть соединение с базой данных
conn.close()