from typing import Union, Optional, Any


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def check_country_and_rating(movie: dict[str, Any]) -> Optional[float]:
            countries: list[str] = movie["country"].split(",")
            rating: float = float(movie["rating_kinopoisk"]) if movie["rating_kinopoisk"] else 0

            if len(countries) >= 2 and rating > 0:
                return rating
            return None

        ratings: list[float] = list(filter(None, map(check_country_and_rating, list_of_movies)))
        avg_rating: float = sum(ratings) / len(ratings)
        return avg_rating

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def check_instances(movie: dict) -> int:
            return movie["name"].count("и")

        def check_rating(movie: dict) -> Optional[dict]:
            movie_rating: float = (
                float(movie["rating_kinopoisk"]) if movie["rating_kinopoisk"] else 0
            )
            if movie_rating >= rating:
                return movie
            return None

        movies_above_threshold: list[dict] = list(filter(check_rating, list_of_movies))
        chars_count: int = sum(map(check_instances, movies_above_threshold))
        return chars_count
