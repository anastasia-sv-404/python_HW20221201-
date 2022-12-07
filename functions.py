from random import randint as rnd

def create_dictionary(min_value, max_value): # создать словарь степень:эначение коэффициента перех х
    degree = int(input('Введите степень многочлена: '))
    glossary = {}
    for i in range(degree, -1, -1):
        glossary[i] = rnd(min_value, max_value)
    return glossary

def create_polynomial(glossary): # сформировать многочлен с коэффициентами типа int от 0 и выше
    polynomial = ''
    for key in glossary.keys():
        if key !=0:
            if key == 1:
                if glossary.get(key) == 1:
                    polynomial += f'+ x '
                elif glossary.get(key) == 0:
                    polynomial += f''
                else:
                    polynomial += f'+ {glossary.get(key)}*x '
            else:
                if glossary.get(key) == 1:
                    polynomial += f'+ x**{key} '
                elif glossary.get(key) == 0:
                    polynomial += f''
                else:
                    polynomial += f'+ {glossary.get(key)}*x**{key} '
        else:
            if glossary.get(key) == 0:
                polynomial += f''
            else:
                polynomial += f'+ {glossary.get(key)} '

    polynomial += '= 0'
    polynomial = polynomial[2:]
    return polynomial


def polynomial_to_dictionary(data): # обратное преобразование многочлена в словарь
    data = data.replace(' = 0', '').replace('+', '')
    list1 = data.split()
    list2 = []
    glossary = {}
    for i in list1:
        if not 'x' in i:
            list2.append([0, int(i)])
        elif i.startswith('x'):
            if i == 'x':
                list2.append([1, 1])
            else:
                y = ('1' + i).split('x**')
                list2.append([int(y[1]), int(y[0])])
        elif i.endswith('x'):
            y = (i + '1').split('*x')
            list2.append([int(y[1]), int(y[0])])
        else:
            y = i.split('*x**')
            list2.append([int(y[1]), int(y[0])])
    for item in list2:
        glossary[item[0]] = item[1]
    return glossary


def sum_dictionaries(glossary1, glossary2): # сложение словарей
    glossary_sum = {}
    glossary_sum.update(glossary1)
    glossary_sum.update(glossary2)
    for i in glossary_sum.keys():
        if glossary1.get(i) and glossary2.get(i):
            glossary_sum[i] = glossary1.get(i) + glossary2.get(i)
        elif glossary1.get(i):
            glossary_sum[i] = glossary1.get(i)
        else:
            glossary_sum[i] = glossary2.get(i)
    return glossary_sum
