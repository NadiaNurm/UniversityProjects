import random

computer_number = []
player_number = []

def create_number(): # создаем произвольный номер
    global computer_number
    for i in range(4):
        digit = random.randint(0,9) 
        while digit in computer_number: # проверяем, чтобы цифры в числе не повторялись
            digit = random.randint(0,9)
        computer_number.append(digit) # заполняем computer_number 4 рандомными неповторяющимися цифрами

def get_player_number(): # получаем число от игрока
    global player_number
    number_str = input('Введите число: ')
    try:
        number_int = int(number_str)
    except: 
        print('Это не число')
        return
    if len(number_str) != 4:
        print('Число должно быть четырехзначным')
        return
    for i in range(4): # проверяем, что в числе игрока нет повторяющихся цифр
        if number_str[i] in player_number:
            print('Цифры в загаданном числе должны быть без повтора!')
            player_number = []
            return
        player_number.append(int(number_str[i]))

def check(): # находим количество быков и коров
    cows = 0
    bulls = 0
    for i in range(4):
        if player_number[i] == computer_number[i]: # если цифра из числа игрока стоит на том же месте, что и цифра из сгенерированного числа, то это +бык
            bulls += 1
        elif player_number[i] in computer_number: # если цифра из числа игрока есть в сгенерированноом числе, то это +корова
            cows  += 1
    return cows, bulls # возвращаем количество коров и быков


def game():
    global player_number
    create_number()
    cows = 0
    bulls = 0
    while bulls != 4:
        while player_number == []: # пока номер игрока пуст, просим его ввести число
            get_player_number()
        cows, bulls = check()
        print('Коровы: {}. Быки: {}'.format(cows,bulls))
        player_number = [] # если игрок не угадал, обнуляем число
    print('Вы выиграли!')

game()
