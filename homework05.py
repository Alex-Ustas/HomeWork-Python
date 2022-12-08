# Homework 05
from random import randint


# 1. Создайте программу для игры с конфетами человек против человека.
# Условие игры: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# - Добавьте игру против бота
def candy():
    """Игра с конфетами"""
    candies = 117
    limit = 28
    player = randint(1, 2)
    step = 1
    print(f'Всего конфет: \033[1m\033[31m{candies}\033[0m, максимально можно взять {limit}')
    while candies != 0:
        who = 'человек' if player == 1 else 'компьютер'
        print(f'\033[1;33mХод {step}\033[0m. Количество конфет: \033[1m\033[31m{candies}\033[0m. Ход игрока: {who}')
        if player == 1:  # ход человека
            amount = limit + 1
            while amount > limit or amount < 1 or amount > candies:
                amount = int(input('Сколько конфет вы хотите взять? '))
                if amount > limit or amount < 1:
                    print(f'Количество может быть от 1 до {limit}, повторите ввод')
            player = 2
        else:  # ход компьютера
            if candies % (limit + 1) == 0:
                amount = randint(1, limit)
            elif candies > limit:
                amount = candies % (limit + 1)
            else:
                amount = candies
            print(f'Компьютер взял конфет: {amount}')
            player = 1
        step += 1
        candies -= amount
    if player == 2:
        print('Вы выиграли!')
    else:
        print('Выиграл компьютер')


# 2. Создайте программу для игры в ""Крестики-нолики"".(в консоли происходит выбор позиции)
def check_winner(player: str, table: list) -> bool:
    """Проверка выигрыша конкретного игрока"""
    if table[0] == table[3] == table[6] == player or \
            table[1] == table[4] == table[7] == player or \
            table[2] == table[5] == table[8] == player or \
            table[0] == table[1] == table[2] == player or \
            table[3] == table[4] == table[5] == player or \
            table[6] == table[7] == table[8] == player or \
            table[0] == table[4] == table[8] == player or \
            table[2] == table[4] == table[6] == player:
        return True
    return False


def game_over(table: list) -> int:
    """Определение конца партии: -1 - не окончена, 0 - ничья, 1 - выиграл первый игрок, 2 - выиграл второй игрок"""
    if check_winner('x', table):
        return 1
    elif check_winner('o', table):
        return 2
    elif table.count('x') + table.count('o') == 9:
        return 0
    return -1


def check_step(pos: str, table: list) -> bool:
    """Проверка возможности хода"""
    if not pos.isdigit():
        return False
    pos = int(pos)
    if pos not in range(9):
        return False
    elif table[pos] == 'x' or table[pos] == 'o':
        return False
    return True


def mark_pos(item: str) -> str:
    """Выделить позицию в таблице цветом"""
    if item == 'x':
        return '\033[1m\033[31mx\033[0m'
    elif item == 'o':
        return '\033[1m\033[32mo\033[0m'
    else:
        return item


def print_table(table: list):
    """Печать игрового поля"""
    for i in range(len(table)):
        print(mark_pos(table[i]) + ' ', end='')
        if (i + 1) % 3 == 0:
            print()


def minmax(table: list, player: str) -> int:
    """Алгоритм минимакса"""
    if game_over(table) == 1:
        return -10
    elif game_over(table) == 2:
        return 10
    elif game_over(table) == 0:
        return 0

    if player == 'o':  # компьютер
        max_score = -100
        for pos in range(len(table)):
            if table[pos] != 'x' and table[pos] != 'o':
                temp_table = table.copy()
                temp_table[pos] = 'o'
                score = minmax(temp_table, 'x')
                if max_score < score:
                    max_score = score
            pos += 1
        return max_score

    if player == 'x':  # человек
        min_score = 100
        for pos in range(len(table)):
            if table[pos] != 'x' and table[pos] != 'o':
                temp_table = table.copy()
                temp_table[pos] = 'x'
                score = minmax(temp_table, 'o')
                if min_score > score:
                    min_score = score
            pos += 1
        return min_score


def tic_tac_toe():
    """Игра в крестики-нолики"""
    table = [str(i) for i in range(9)]
    print_table(table)
    step = 1
    while game_over(table) < 0:
        player = 'x' if step % 2 == 1 else 'o'
        if player == 'x':  # ход человека
            pos = '-'
            while not check_step(pos, table):
                pos = input(f'\033[1m\033[33mХод {step}\033[0m. Выберите позицию для хода: ')
                if not check_step(pos, table):
                    print('Неверная позиция. Повторите ввод.')
            table[int(pos)] = player
        else:  # ход компьютера
            best_score = -100
            best_pos = -1
            for pos in range(len(table)):
                if table[pos] != 'x' and table[pos] != 'o':
                    temp_table = table.copy()
                    temp_table[pos] = 'o'
                    score = minmax(temp_table, 'x')
                    if best_score < score:
                        best_score = score
                        best_pos = pos
                pos += 1
            print(f'\033[1m\033[33mХод {step}\033[0m. Компьютер сходил на позицию {best_pos}')
            table[best_pos] = player

        print_table(table)
        step += 1
    end = game_over(table)
    if end == 0:
        print('Ничья')
    elif end == 1:
        print('Вы выиграли!')
    else:
        print('Выиграл компьютер!')


print('1 - игра с конфетами, 2 - крестики-нолики')
while True:
    num = int(input('Введите номер игры (1-2, 0 - окончание): '))
    if num == 1:
        candy()
    elif num == 2:
        tic_tac_toe()
    elif num == 0:
        break
    else:
        print('Неверный номер игры')
    print()
