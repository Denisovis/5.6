def to_list(in_str):
    return [_ for _ in in_str if _ != '\n' and _ != ' ']


def to_str(in_list):
    out_str = ''
    for _ in range(len(in_list)):
        out_str += in_list[_]
        if len(out_str) == 5 or len(out_str) == 11:
            out_str += '\n'
        else:
            out_str += ' '
    return out_str


def check_winner(list_field):
    #Варианты победителя
    winner = [[True, True, True,
               False, False, False,
               False, False, False],
              [False, False, False,
               True, True, True,
               False, False, False],
              [False, False, False,
               False, False, False,
               True, True, True],
              [False, False, True,
               False, False, True,
               False, False, True],
              [False, True, False,
               False, True, False,
               False, True, False],
              [True, False, False,
               True, False, False,
               True, False, False],
              [True, False, False,
               False, True, False,
               False, False, True],
              [False, False, True,
               False, True, False,
               True, False, False,]]

    #Заменяем символы списков на True/False, чтобы сравнивать с победными вариантами
    cache_list = list_field.copy()

    for _ in range(len(list_field)):
        if turnX:
            cache_list[_] = True if cache_list[_] == 'x' else False
        else:
            cache_list[_] = True if cache_list[_] == 'o' else False
    for _ in range(len(winner)):
        cache2_list = cache_list.copy()
        for i in range(len(cache2_list)):
            cache2_list[i] = cache2_list[i] and winner[_][i]
        if cache2_list in winner:
            if turnX:
                print('\nКрестики победили!!!\n')
                return True
            else:
                print('\nНолики победили!!!\n')
                return True
    return False


turnX = True
str_start_field = '''- - -\n- - -\n- - -'''
dict_turn = {'7': 0, '8': 1, '9': 2, '4': 3, '5': 4, '6': 5, '1': 6, '2': 7, '3': 8}
print('Чтобы поставить x/o в клетку, '
      'игрок должен нажать на калькуляторной \n'
      'части клавиатуры соответствующую цифру. '
      'Например "7", чтобы поставить символ в\n'
      'верхний левый угол или "3", чтобы '
      'поставить символ в нижний правый угол.\n'
      'Удачи!!!')

while input('Нажмите Enter, чтобы начать новую игру!') == '':
    str_now_field = str_start_field
    list_now_field = to_list(str_now_field)
    print(str_now_field)
    while not check_winner(to_list(str_now_field)):
        if '-' not in str_now_field:
            print('\nНичья :(\n')
            break
        btn = input('Сейчас ходят %s' % ('крестики ' if turnX else 'нолики '))
        if btn in dict_turn:
            if list_now_field[dict_turn[btn]] == '-':
                list_now_field[dict_turn[btn]] = 'x' if turnX else 'o'
                str_now_field = to_str(list_now_field)
                print(str_now_field)
                if check_winner(list_now_field):
                    break
                turnX = not turnX

