# Homework 02
from random import randint
from random import random


# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def task1():
    rnd_lst = [randint(1, 10) for i in range(randint(5, 10))]
    print('Список случайных чисел:', rnd_lst)
    summ = [rnd_lst[i] for i in range(len(rnd_lst)) if i % 2 == 1]
    print('Список нечетных чисел из начального списка:', summ)
    print('Сумма чисел на нечетных позициях:', sum(summ))


# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и
# последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
def task2():
    rnd_lst = [randint(1, 5) for i in range(randint(4, 7))]
    print('Список случайных чисел:', rnd_lst)
    len_lst = len(rnd_lst)
    mult_lst = [rnd_lst[i] * rnd_lst[-i - 1] for i in range(len_lst // 2)]
    if len_lst % 2 == 1:
        mult_lst.append(rnd_lst[len_lst // 2] ** 2)
    print('Список произведения пар чисел:', mult_lst)


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 (максимальное значение у числа 1.2 , минимальное у 10.01)
def task3():
    rnd_lst = [round(random(), randint(1, 3)) for i in range(5)]
    # rnd_lst = [1.1, 1.2, 3.1, 5.03, 10.01]
    print('Список случайных чисел:', rnd_lst)
    fract_lst = [str(num).split('.')[1] for num in rnd_lst]
    max_dec = max([len(num) for num in fract_lst])
    fract_lst = [int(int(num) * pow(10, max_dec - len(num))) for num in fract_lst]
    print('Список дробных частей:', fract_lst)
    print(f'max - min = {round((max(fract_lst) - min(fract_lst)) / pow(10, max_dec), max_dec)}')


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def binary(num, bin_list):
    if num < 2:
        return '1' + bin_list
    else:
        return binary(num // 2, str(num % 2) + bin_list)


def task4():
    for i in range(5):
        num = randint(1, 100)
        print(f'{num} -> {binary(num, "")}')


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. (Дополнительное)
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]
def fib(num):
    if num in [1, 2]:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


def negafib(num):
    if num == 1:
        return 1
    elif num == 2:
        return -1
    else:
        return negafib(num - 2) - negafib(num - 1)


def task5():
    num = int(input('Введите число: '))
    lst = [0]
    for i in range(1, num + 1):
        lst.append(fib(i))
        lst.insert(0, negafib(i))
    print(lst)


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
