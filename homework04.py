# Homework 04
from random import randint
import sympy


# 1. Вычислить число Пи c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415
def calc_pi(d: int) -> str:
    s = float(0.0)
    for i in range(0, 1000000, 2):
        if (i // 2) % 2 == 0:
            s += 4 / (i + 1)
        else:
            s -= 4 / (i + 1)
    return str(s)[:d]


def calc_pi2(d: int) -> (float, int):
    s = 3.0
    i = 1
    sgn = 1
    while str(s)[:d] != '3.14159265358979323846264338327950288419716939937510'[:d]:
        s += sgn / (i * (i + 1) * (2 * i + 1))
        sgn *= -1
        i += 1
    return s, i


def task1():
    """Вычисление числа pi с заданной точностью"""
    d = len(input('Введите точность числа pi: '))
    print('Число pi с заданной точностью:', calc_pi(d))
    result, it = calc_pi2(d)
    print(f'Число pi с заданной точностью (второй вариант): {str(result)[:d]}, количество итераций: {it}')


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример:
# * 6 -> [2,3]
# * 144 -> [2,3]
def task2():
    """Список простых множителей числа N"""
    n = int(input('Введите число N: '))
    nums = list()
    multiplier = 2
    while n >= multiplier:
        while n % multiplier == 0:
            n /= multiplier
            nums.append(multiplier)
        multiplier += 1
    nums = list(set(nums))
    nums.sort()
    print('Список простых множителей числа N:', nums)


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
def task3():
    """Список неповторяющихся элементов"""
    in_lst = input('Введите список элементов через пробел: ')
    in_lst = list(map(int, in_lst.split()))
    in_lst.sort()
    out_lst = list(set(in_lst))
    out_lst.sort()
    print('Исходная последовательность чисел:\t', in_lst)
    print('Список элементов без повторений:\t', out_lst)


# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.(записать в строку)
# Пример:
# k=2 => 2*x**2 + 4*x + 5 или x**2 + 5 или 10*x**2
# k=3 => 2*x**3 + 4*x**2 + 4*x + 5
def task4():
    """Запись многочлена степени k в файл"""
    k = int(input('Введите степень многочлена: '))
    polynom = [f'{str(randint(0, 100))}*x**{i}' for i in range(k + 1)]
    polynom_str = str(sympy.simplify(' + '.join(polynom[::-1])))
    print(polynom_str)
    with open('polynom.txt', 'w') as f:
        f.write(polynom_str)


# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример:
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9
def get_polynom(file_num: int) -> str:
    """Взять многочлен из файла"""
    with open(f'file{file_num}.txt', 'r') as f:
        polynom = f.readline()
    return polynom


def task5():
    """Сумма двух многочленов"""
    polynom1 = sympy.simplify(get_polynom(1))
    polynom2 = sympy.simplify(get_polynom(2))
    print('\t\t' + str(polynom1) + '\n\t\t' + str(polynom2))
    x = sympy.Symbol('x')
    polynom = str(sympy.simplify(polynom1 + polynom2))
    print('Сумма = ' + polynom)
    with open('file3.txt', 'w') as f:
        f.write(polynom)


while True:
    num = int(input('Введите номер задания (1-5, 0 - окончание): '))
    if num == 1:
        task1()
    elif num == 2:
        task2()
    elif num == 3:
        task3()
    elif num == 4:
        task4()
    elif num == 5:
        task5()
    elif num == 0:
        break
    else:
        print('Неверный номер задания')
    print()
