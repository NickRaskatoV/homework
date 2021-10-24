#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
#Moscow = (550, 370)
#London = (510, 510)
#Paris = (480, 480)
# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2


moskow_x = 550
moskow_y = 370

london_x = 510
london_y = 510

paris_x = 480
paris_y = 480
Moskow_london = (moskow_x - london_x) ** 2 + (moskow_y - london_y) ** 2
Moskow_paris = (moskow_x - paris_x) ** 2 + (moskow_y - paris_y) ** 2

london_paris = (paris_x - london_x) ** 2 + (paris_y - london_y) ** 2
london_moskow = Moskow_london

paris_london = london_paris
paris_moskow = Moskow_paris

slovar = {'москва-лондон': Moskow_london, 'москва-париж': Moskow_paris}
slovar_2 = {'лондон-париж': london_paris, 'лондон-москва': london_moskow}
slovar_3 = {'париж-лондон': paris_london, 'париж-москва': paris_moskow}
slovar_slovarei = {1: slovar, 2: slovar_2, 3: slovar_3}
print(slovar_slovarei)
