# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import functions

# создать файл с многочленом номер 1
dictionary1 = functions.create_dictionary(0, 100)
print(dictionary1)

expression1 = functions.create_polynomial(dictionary1)
print(expression1)

with open('expression1.txt', 'w', encoding = 'UTF-8') as data:
    data.write(expression1)

print()


# создать файл с многочленом номер 2
dictionary2 = functions.create_dictionary(0, 100)
print(dictionary2)

expression2 = functions.create_polynomial(dictionary2)
print(expression2)

with open('expression2.txt', 'w', encoding = 'UTF-8') as data:
    data.write(expression2)