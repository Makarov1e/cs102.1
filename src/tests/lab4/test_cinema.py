import unittest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".."))
sys.path.append(parent_dir)

from src.lab4.cinema import Cinema, history_file, films_file, user_views

class TestCinema(unittest.TestCase):

    def test_load_movies(self):
        expected_movies = {
            1: 'Мстители: Финал',
            2: 'Хатико',
            3: 'Дюна',
            4: 'Унесенные призраками'
        }
        recommendation_service = Cinema(films_file, history_file, user_views)
        result = recommendation_service.load_films()
        self.assertEqual(result, expected_movies)

    def test_load_history(self):
        expected_history = [
            [2, 1, 3],
            [1, 4, 3],
            [2, 2, 2, 2, 2, 3]
        ]
        recommendation_service = Cinema(films_file, history_file, user_views)
        result = recommendation_service.load_history()
        self.assertEqual(result, expected_history)

    def test_filter_users(self):
        expected_filtered_users = [
            [2, 1, 3],
            [1, 4, 3],
            [2, 2, 2, 2, 2, 3]
        ]
        recommendation_service = Cinema(films_file, history_file, user_views)
        result = recommendation_service.filter_users(user_views)
        self.assertEqual(result, expected_filtered_users)

    def test_exclude_watched_movies(self):
        filtered_users = [
            [1, 2, 3],
            [1, 2],
            [1, 2, 4, 5]
        ]
        expected_unwatched_movies = [3, 4, 5]
        recommendation_service = Cinema(films_file, history_file, user_views)
        result = recommendation_service.exclude_watched_films(user_views, filtered_users)
        self.assertEqual(result, expected_unwatched_movies)

if __name__ == '__main__':
    unittest.main()