class Season:
    def __init__(self, name, num_episodes, episodes):
        self.name = name
        self.num_episodes = num_episodes
        self.episodes = episodes
        
        
class Serial:
    def __init__(self, title, year, actors, director, genre, seasons):
        self.title = title
        self.year = year
        self.actors = actors
        self.director = director
        self.genre = genre
        self.seasons = seasons
    
    def add_favorite_season(self, season_name):
        for season in self.seasons:
            if season.name == season_name:
                # Добавление в список любимых сезонов
                # (можно добавить атрибут-список в класс Serial или использовать отдельный список)
                favorite_seasons.append(season)
                print(f"Сезон '{season_name}' добавлен в список любимых сезонов сериала '{self.title}'.")
                break
        else:
            print(f"Сезон '{season_name}' не найден у сериала '{self.title}'.")
    
    def add_favorite_serial(self):
        # Добавление сериала в список любимых сериалов
        # (можно добавить атрибут-список в класс Serial или использовать отдельный список)
        favorite_serials.append(self)
        print(f"Сериал '{self.title}' добавлен в список любимых сериалов.")

# Примеры использования

# Создание сериала
season1 = Season("Сезон 1", 10, ["Эпизод 1", "Эпизод 2", "Эпизод 3", "Эпизод 4", "Эпизод 5", "Эпизод 6", "Эпизод 7", "Эпизод 8", "Эпизод 9", "Эпизод 10"])
season2 = Season("Сезон 2", 8, ["Эпизод 1", "Эпизод 2", "Эпизод 3", "Эпизод 4", "Эпизод 5", "Эпизод 6", "Эпизод 7", "Эпизод 8"])
season3 = Season("Сезон 3", 12, ["Эпизод 1", "Эпизод 2", "Эпизод 3", "Эпизод 4", "Эпизод 5", "Эпизод 6", "Эпизод 7", "Эпизод 8", "Эпизод 9", "Эпизод 10", "Эпизод 11", "Эпизод 12"])
serial = Serial("Великий Сериал", 2022, ["Актер 1", "Актер 2", "Актер 3"], "Режиссер 1", "Жанр 1", [season1, season2, season3])

# Добавление сериала в список любимых сериалов
favorite_serials = []
serial.add_favorite_serial()

# Добавление сезона в список любимых сезонов
favorite_seasons = []
serial.add_favorite_season("Сезон 1")
