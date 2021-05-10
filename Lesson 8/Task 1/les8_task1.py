"""
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
"""


import hashlib

count_substrings = set()


def substrings(string):
    for i in range(len(string)):
        for j in range(len(string), i, -1):
            hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            if hash_str != hashlib.sha1(' '.encode('utf-8')).hexdigest():
                count_substrings.add(hash_str)
    return count_substrings


string_st = input('Введите строку: ')

print(f'{len(substrings(string_st)) - 1} подстрок в строке: {string_st}')
