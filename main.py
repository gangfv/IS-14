import re
from itertools import zip_longest
from transliterate import translit

FILE_NAME = 'data_fio_number_sepped.txt'


def read_file(file: str):
    with open(file, encoding='utf-8') as f:
        return (re.sub("\n", "", i).split(';') for i in f.readlines())


def translit_en(list_ru):
    return [translit(i, 'ru', True) for i in list_ru]


def num_read(file: str):
    return [i[1] for i in read_file(file)]


def fio_read(file: str):
    return [i[0] for i in read_file(file)]


def num_ref(file: str):
    num = []
    for index, i in enumerate(num_read(file)):
        split = re.split('\(|\)', i)
        if len(split[1]) > 3:
            split[1] = split[1][1:]
        elif len(split[1]) < 3:
            split[1] = f"9{split[1]}"
        num.append(f"{split[0]}({split[1]}){split[2]}")
    return num


def fix_list(file: str):
    return [*zip_longest(fio_read(file), num_ref(file))]


result = 0
for i in fix_list(FILE_NAME):
    result += 1
    with open(f"{translit(i[0], 'ru', True)}.txt", "w", encoding='utf-8') as file:
        print(*i)
        file.write("{};{}".format(*i))

print(f"Cгенерировано {result}")
