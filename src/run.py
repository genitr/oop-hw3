"""Точка входа в программу"""

from settings import FILEPATH


def get_cookbook(cookbook_file: str) -> dict:
    """Получаем список всех рецептов"""
    with open(cookbook_file, encoding='utf8') as f:
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

    return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    """Получаем количество ингредиентов для указанных блюд"""
    cooks = get_cookbook(FILEPATH)
    shop_list = {}
    for dish in dishes:
        if dish in cooks:
            for index in range(len(cooks[dish])):
                i = cooks[dish][index]['ingredient_name']
                q = cooks[dish][index]['quantity'] * person_count
                m = cooks[dish][index]['measure']
                if i in shop_list:
                    q += q
                shop_list[i] = {'quantity': q, 'measure': m}

    return shop_list

if __name__ == '__main__':
    from pprint import pprint
    pprint(get_cookbook(FILEPATH))
    print()
    pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 4))
