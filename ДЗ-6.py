#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
#my_family = []


# список списков приблизителного роста членов вашей семьи
#my_family_height = [['имя', рост],[],]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
wife = polina = 165
son = Ilya = 190
brother = Denis = 195
height = wife+son+brother

my_family = ['wife', 'son', 'brother']
print(my_family)

my_family_height = [['Polina', wife],['Ilya', son],['Denis', brother]]
print(my_family_height)

print('Рост моей жены - ', wife, 'см')
print('общий рост моей семьи - ', height, 'см')