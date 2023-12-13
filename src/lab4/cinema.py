class Cinema:
    
    """
    Класс, содержаший функции, реализующие подбор фильма по вкусам
    """

    def __init__(self, films, history, user_views):
        self.films_file = films
        self.history_file = history
        self.films = self.load_films()
        self.history = self.load_history()
        self.user_views = list(map(int, user_views.split(',')))

    def load_films(self):
        films = {}
        with open(self.films_file, 'r', encoding="utf-8") as file:
            for line in file:
                movie_id, movie_name = line.strip().split(',')
                films[int(movie_id)] = movie_name
        return films

    def load_history(self):
        history = []
        with open(self.history_file, 'r', encoding="utf-8") as file:
            for line in file:
                viewed_films = list(map(int, line.strip().split(',')))
                history.append(viewed_films)
        return history

    # def get_user_views(self):
    #     user_input = input("Введите список просмотренных фильмов (через запятую): ")
    #     user_views = list(map(int, user_input.split(',')))
    #     return user_views

    def filter_users(self, user_views):
        filtered_users = []
        for user in self.history:
            user_set = set(user)
            if len(user_set.intersection(self.user_views)) >= len(self.user_views) / 2:
                filtered_users.append(user)
        return filtered_users

    def exclude_watched_films(self, user_views, filtered_users):
        user_views = self.user_views
        unwatched_films = []
        for user in filtered_users:
            for movie in user:
                if movie not in user_views:
                    unwatched_films.append(movie)
        return unwatched_films

    def recommend_movie(self):
        user_views = self.user_views
        filtered_users = self.filter_users(user_views)
        unwatched_films = self.exclude_watched_films(user_views, filtered_users)

        movie_views_count = {}
        for movie in unwatched_films:
            if movie in movie_views_count:
                movie_views_count[movie] += 1
            else:
                movie_views_count[movie] = 1

        recommended_movie_id = max(movie_views_count, key=movie_views_count.get)
        recommended_movie_name = self.films[recommended_movie_id]

        print("Рекомендуемый фильм:", recommended_movie_name)

films_file = 'src/lab4/films.txt'
history_file = 'src/lab4/history.txt'
user_views = '1, 2'
recommendation_service = Cinema(films_file, history_file, user_views)
recommendation_service.recommend_movie()
