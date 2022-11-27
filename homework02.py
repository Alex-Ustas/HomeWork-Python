# Homework 02
import math
import random
import time


# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
def task1():
    print('Задание 1')
    num = input('Введите вещественное число: ')
    summa = 0
    digits = '0123456789'
    for i in range(len(num)):
        if num[i] in digits:
            summa += int(num[i])
    print('Сумма цифр:', summa)


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def task2():
    print('Задание 2')
    num = int(input('Введите число N: '))
    mult_lst = [math.factorial(n) for n in range(1, num + 1)]
    print(mult_lst)


# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
#
# Пример:
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]
def task3():
    print('Задание 3')
    num = 0
    while num <= 0:
        num = int(input('Введите число N для расчета последовательности (1+1/n)^n: '))
        if num <= 0:
            print('Число N должно быть положительным!')

    sequence = list()
    for i in range(1, num + 1):
        sequence.append((1 + 1 / i) ** i)
    print(sequence)


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке
# одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# Пример:
# -2 -1 0 1 2 Позиции: 0,1 -> 2
def task4():
    print('Задание 4')
    elements = list()
    with open('file.txt', 'r') as f:
        num = f.readline()
        while num:
            elements.append(int(num.replace('\n', '')))
            num = f.readline()
    print('Список элементов из файла:', elements)
    pos_lst = input('Введите позиции элементов через запятую: ')
    pos_lst = list(map(int, pos_lst.split(',')))
    mult = 1
    for i in pos_lst:
        if i < len(elements):
            mult *= elements[i]
    print('Произведение элементов:', mult)


# 5. Реализуйте алгоритм перемешивания списка.
def task5():
    print('Задание 5')
    in_lst = [i for i in range(10)]
    print('Исходный список из 10 элементов:\t\t\t', in_lst)

    shuffle = in_lst.copy()
    random.shuffle(shuffle)
    print('Перемешанный список методом shuffle:\t\t', shuffle)

    out_lst = list()
    check = [0 for i in range(len(in_lst))]  # 0 - элемент еще не вставляли, 1 - уже использовали
    for i in range(len(in_lst)):
        position = random.randint(0, len(in_lst) - 1)
        while check[position] == 1:
            position = random.randint(0, len(in_lst) - 1)
        out_lst.append(in_lst[position])
        check[position] = 1
    print('Перемешанный список случайным образом:\t\t', out_lst)

    # Алгоритм Лемера от текущего времени
    # x(i) = a * x(i-1) mod m
    cur_time = time.time()
    a = int(float(cur_time) * 100 % 100)
    a = 2 if a < 2 else a
    m = int(float(cur_time) * 10000 % 100)
    m = 11 if m < 2 else m
    xi = int(float(cur_time) * 1000000 % 100)
    xi = 11 if xi == 0 else xi
    print(f'Time = {cur_time}, a = {a}, m = {m}, xi = {xi}')
    lehmer = list()
    check = [0 for i in range(len(in_lst))]  # 0 - элемент еще не вставляли, 1 - уже использовали
    for i in range(len(in_lst)):
        position = xi % len(in_lst)
        while check[position] == 1:
            position += 1
            position = position if position < len(in_lst) else 0
        lehmer.append(in_lst[position])
        check[position] = 1
        xi = (a * xi) % m
    print('Перемешанный список по алгоритму Лемера:\t', lehmer)


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
