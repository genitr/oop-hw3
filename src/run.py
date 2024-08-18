"""Точка входа в программу"""

from settings import get_file_in_data

cookbook_file = get_file_in_data('cookbook.txt')
chapters = [
    get_file_in_data('chapter1.txt'),
    get_file_in_data('chapter2.txt'),
    get_file_in_data('chapter3.txt')
    ]

def file_assembling(files_list: list, new_file_name: str):
    """Сортировка предоставленного списка файлов и запись всего содержимого в один файл"""
    num_of_lines = []

    # Определение количества строк, объединение с путями до файлов
    # и сортировка по увеличению количества строк
    for item in files_list:
        with open(item, encoding='utf8') as f:
            num_of_lines.append(len(f.readlines()))

    data = list(zip(files_list, num_of_lines))
    data_sorted = sorted(data, key=lambda x: x[1])

    # Запись в новый файл согласно отсортированному списку
    with open(get_file_in_data(new_file_name), 'a', encoding='utf8') as new_file:
        for index in data_sorted:
            with open(index[0], encoding='utf8') as source_file:

                source_filename = index[0].split('\\')[-1] + '\n'
                source_lines = str(index[1]) + '\n'

                new_file.write(source_filename + source_lines)

                for line in source_file:
                    new_file.write(line)

                new_file.write('\n')

    return data_sorted


def get_cookbook(filename: str) -> dict:
    """Получаем список всех рецептов"""
    with open(filename, encoding='utf8') as f:
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
    cooks = get_cookbook(cookbook_file)
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
    pprint(get_cookbook(cookbook_file))
    print()
    pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 4))
    print()
    pprint(file_assembling(chapters, 'novel.txt'))
