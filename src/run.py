"""Точка входа в программу"""
import os
from pprint import pprint


FILEPATH = os.path.join(os.getcwd(),'src\\data\\cookbook.txt')

with open(FILEPATH, encoding='utf8') as f:
    cook_book = {}

    for line in f:
        recipe = line.strip()
        icount = f.readline()
        ilist = []
        for _ in range(int(icount)):
            name, amount, unit = f.readline().strip().split(' | ')
            ilist.append({'ingredient_name': name, 'quantity': int(amount), 'measure': unit})
        f.readline()
        cook_book[recipe] = ilist

pprint(cook_book)
