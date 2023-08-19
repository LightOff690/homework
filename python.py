class Tower:
    def __init__(self, health=100, armor=50):
        self.health = health
        self.armor = armor
    
    def increase_health(self, amount):
        self.health += amount
    
    def decrease_health(self, amount):
        self.health -= amount
    
    def increase_armor(self, amount):
        self.armor += amount
    
    def decrease_armor(self, amount):
        self.armor -= amount


class ArcherTower(Tower):
    def shoot(self):
        # Логика стрельбы стрелковой башни
        print("Выстрел стрелковой башни")

# Пример использования классов
tower = Tower(100, 50)
print(tower.health)  # Выведет: 100

archer_tower = ArcherTower(100, 50)
archer_tower.shoot()  # Выведет: "Выстрел стрелковой башни"class Tower:
def __init__(self, health=100, armor=50):
        self.health = health
        self.armor = armor
    
def increase_health(self, amount):
        self.health += amount
    
def decrease_health(self, amount):
        self.health -= amount
    
def increase_armor(self, amount):
        self.armor += amount
    
def decrease_armor(self, amount):
        self.armor -= amount


class ArcherTower(Tower):
 def shoot(self):
        # Логика стрельбы стрелковой башни
        print("Выстрел стрелковой башни")

# Пример использования классов
tower = Tower(100, 50)
print(tower.health)  # Выведет: 100

archer_tower = ArcherTower(100, 50)
archer_tower.shoot()  # Выведет: "Выстрел стрелковой башни"