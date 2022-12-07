# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import functions

# первый многочлен из файла и его обратное преобразование в словарь
path = r'expression1.txt'
with open(path, 'r', encoding='UTF-8') as file1:
    data1 = file1.readline()

dictionary1 = functions.polynomial_to_dictionary(data1)
print(dictionary1)

# второй многочлен из файла и его обратное преобразование в словарь
path = r'expression2.txt'
with open(path, 'r', encoding='UTF-8') as file2:
    data2 = file2.readline()

dictionary2 = functions.polynomial_to_dictionary(data2)
print(dictionary2)

print()

# суммирование первого и второго словарей
dictionary_sum = functions.sum_dictionaries(dictionary1,dictionary2)
dictionary_sum = dict(sorted(dictionary_sum.items())[::-1])
print(dictionary_sum)

print()

# сумма многочленов из первого и второго словаря и запись его в файл
polynomial_sum = functions.create_polynomial(dictionary_sum)
print(polynomial_sum)

with open('expression_sum.txt', 'w', encoding = 'UTF-8') as data:
    data.write(polynomial_sum)


