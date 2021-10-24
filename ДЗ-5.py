#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов
#favorite_movies
# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# TODO здесь ваш код
favorite_movies = ['matrix', 'snatch', 'Lock Stock and Two Smoking Barrels','rocknrolla']
print(favorite_movies[0], favorite_movies[-1], favorite_movies[1], favorite_movies[-2])