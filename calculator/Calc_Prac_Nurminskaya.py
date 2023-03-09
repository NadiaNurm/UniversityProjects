from math import trunc, pi, sin, cos, tan

def blank(num1):
    return num1

def negative(num1):
    return -num1

def minus(num1,num2):
    return(num1 - num2)

def plus(num1,num2):
    return(num1 + num2)

def mult(num1,num2):
    return(num1 * num2)

def divide(num1,num2):
    return round((num1 / num2),3)

def power(num1, num2):
    return num1 ** num2

dict_symbol = { #словарь, из которого мы берем операцию и с помощью функции ее осуществляем
    ' в степени ' : power,
    ' разделить на ' : divide,
    ' умножить на ' : mult,    
    ' плюс ' : plus,
    ' минус ' : minus,
}

dict_priority = { # расставляем приоритеты операций, чтобы отсортировать их для польской записи
    1: [' в степени '],
    2: [' умножить на ', ' разделить на '],
    3: [' плюс ',' минус ']
}

dict_aux_op = { #словарь дополнительных операций
    'синус ': sin,
    'косинус ': cos,
    'тангенс ': tan,
    'минус ': negative,
}

dict_number =  {
    'ноль'         : 0 ,
    'один'         : 1 ,
    'два'          : 2 ,
    'три'          : 3 ,
    'четыре'       : 4 ,
    'пять'         : 5 ,
    'шесть'        : 6 ,
    'семь'         : 7 ,
    'восемь'       : 8 ,    
    'девять'       : 9 ,
    'десять'       : 10 ,
    'одиннадцать'  : 11 ,
    'двенадцать'   : 12 ,
    'тринадцать'   : 13 ,
    'четырнадцать' : 14 ,
    'пятнадцать'   : 15 ,
    'шестнадцать'  : 16 ,
    'восемнадцать' : 18 ,
    'семнадцать'   : 17 ,
    'девятнадцать' : 19 ,
    'двадцать'     : 20 ,
    'тридцать'     : 30 ,
    'сорок'        : 40 ,
    'пятьдесят'    : 50 ,
    'шестьдесят'   : 60 ,
    'восемьдесят'  : 80 ,
    'семьдесят'    : 70 ,
    'девяносто'    : 90 ,
    'сто'          : 100 , 
    'двести'       : 200 , 
    'триста'       : 300 , 
    'четыреста'    : 400 , 
    'пятьсот'      : 500 , 
    'шестьсот'     : 600 , 
    'семьсот'      : 700 , 
    'восемьсот'    : 800 ,
    'девятьсот'    : 900 , 
    'одна тысяча'  : 1000 , 
    'две тысячи'   : 2000 , 
    'три тысячи'   : 3000 , 
    'четыре тысячи': 4000 , 
    'пять тысяч'   : 5000 , 
    'шесть тысяч'  : 6000 , 
    'восемь тысяч' : 8000 ,
    'семь тысяч'   : 7000 ,
    'девять тысяч' : 9000 , 
}


def getKey(dict, value): # получаем ключ по значению
    return list(dict.keys())[list(dict.values()).index(value)]

def translate_number(result): # переводим целое число, которое мы получили в результате вычислений, обратно в строку
    rangeMax = len(str(result)) + 1
    str_result = str(result)
    new_str_result = ''
    new_number_list = []
    if result == 0:
        return 'ноль'
    if int(str_result[-2:]) <= 19 and int(str_result[-2:]) >= 11: # последние 2 цифры
        new_number_list.insert(0, getKey(dict_number,int(str_result[-2:])))
    else:
        if len(str_result) < 2: # сколько раз итерируем по числу
            rangeMax = 2
        else:
            rangeMax = 3
        for i in range(1, rangeMax):
            if int(str_result[-i]) == 0:
                continue
            new_number = int(str_result[-i]) * (10 ** (i-1)) # переделываем цифру в число с учетом разряда 
            new_number_list.insert(0, getKey(dict_number,new_number))
    for i in range(3, len(str_result) + 1):
        if int(str_result[-i]) == 0:
                continue
        new_number = int(str_result[-i]) * (10 ** (i-1))
        new_number_list.insert(0, getKey(dict_number,new_number))
    new_str_result = ' '.join(new_number_list)
    return new_str_result 

def translate_decimal_number(number): # переводим дробное число, которое мы получили в результате вычислений, обратно в строку
    suffix = ''
    str_number = ''
    str_list = []
    current_number = number # приходят всегда тысячные
    if (current_number % 10 == 1) and (current_number % 100 != 11): # смотрим, как можно сократить
        suffix = 'тысячная'
    elif current_number % 10 != 0:
        suffix = 'тысячных'
    elif (current_number % 100) // 10 == 1 and (current_number % 1000) // 10 != 11:
        suffix = 'сотая'
    elif (current_number % 100) // 10 != 0:
        suffix = 'сотых'
    elif (current_number % 1000) // 100 == 1:
        suffix = 'десятая'
    elif (current_number % 1000) // 100 != 0:
        suffix = 'десятых'
    while current_number % 10 == 0:
        current_number = trim_number(current_number)
    
    if current_number % 10 == 1 and current_number % 100 != 11: # склонение числительных
        current_number = trim_number(current_number) * 10
        str_list.insert(0,'одна')
    elif current_number % 10 == 2 and current_number % 100 != 12:
        current_number = trim_number(current_number) * 10
        str_list.insert(0,'две')
    if current_number != 0:
        str_list.insert(0,translate_number(current_number))
    str_number = ' '.join(str_list)
    full_str_number = '{} {}'.format(str_number, suffix)
    return full_str_number

def generator(max = 99, printResult = False): # генерируем словарь чисел от 0 до 99
    dict_generator = {} 
    for i in range(0,max + 1):
        new_str_result = translate_number(i)
        dict_generator[new_str_result] = i
    if printResult:  # если надо распечатать словарь
        for key in dict_generator:
            print('{} : {}'.format(key,dict_generator[key]))
    return dict_generator   

def trim_number(number): # отбрасываем последнюю цифру
    return number // 10

def decimal_generator(printResult = False): # генерируем словарь до тысячных
    dict_generator_decimal = {}
    dict_generator = generator(max = 999) 
    for i in range(1,1000): # идем по тысячным, i = 1 => число равно 0,001
        full_str_number = translate_decimal_number(i)
        dict_generator_decimal[full_str_number] = i/1000
    if printResult:  # если надо распечатать словарь
        for key in dict_generator_decimal:
            print('{} : {}'.format(key,dict_generator_decimal[key]))
    return dict_generator_decimal


def check_decimal(number): # проверяем, что число не целое
    dict_generator = decimal_generator()
    if number in dict_generator.keys():
        ready_number = dict_generator[number]
        return ready_number
    return None

def find_aux_op(number): # проверяем, есть ли вспомогательные символы в веденной строке 
    for op in dict_aux_op.keys():
        if number[:len(op)] == op:
            return dict_aux_op[op], number[len(op):]
    return blank,number

def check_number(number): # проверяем, что число целое
    dict_generator = generator()
    if number in dict_generator.keys():
        ready_number = dict_generator[number]
        return ready_number
    return None



def polska(number_list): # используем польскую инверсионную запись, используем уже отсортированный список
    stack = []
    #lst = list(number_list)
    for i in number_list:
        if isinstance(i,int) or isinstance(i,float):
            stack.append(i)
            #lst.remove(i)
        else:
            num1, num2 = stack.pop(), stack.pop() # достаем два предыдущих числа и проводим операцию
            if dict_symbol[i] == divide and num1 == 0:
                return 'Деление на ноль!!!'
            stack.append(dict_symbol[i](num2, num1)) # добавляем выражение
            #lst.remove(i)
    return stack.pop() # езультат всех вычислений

def find_operations(expression_list): # разбиваем входящую строку на список из чисел и операций
    new_expression_list = []
    is_ready = True
    for expression_bit in expression_list:
        found = False
        for symbol in dict_symbol.keys():
            if expression_bit in dict_symbol.keys():
                continue
            number_list = expression_bit.split(symbol)
            if len(number_list) > 1:
                is_ready = False
                amount = len(number_list) # смотрим, сколько символов найдено 
                for i in range(amount-1):
                    number_list.insert((i*2)+1, symbol) # вставляем обратно эти символы
                new_expression_list.extend(number_list)
                found = True
                break
        if not found:
            new_expression_list.append(expression_bit)
    
    return is_ready,new_expression_list # на выходе получаем состояние разбиения строки и список строк

def get_priority(operation): # получаем номер операции по приоритету
    for priority in dict_priority.keys():
        if operation in dict_priority[priority]:
            return priority

def sort_for_polska(number_list): # разбиваем опирации по приоритетам
    stack = []
    output = [] # выходной отсортированный лист
    for number in number_list:
        if isinstance(number,int) or isinstance(number,float):
            output.append(number)
        else:
            if len(stack) == 0: # если стек пустой, то добавляем операцию
                stack.append(number)
            else:
                priority1 = get_priority(number)
                priority2 = get_priority(stack[-1])
                if ((priority1 > priority2) and (len(stack) > 0)) or (priority1==priority2 and stack[-1] in [' минус ', ' разделить на ']):
                    output.append(stack.pop()) # достаем последний элемент из списка стак и добавляем в оутпут
                    #priority1 = get_priority(number)
                    #priority2 = get_priority(stack[-1])
                stack.append(number)
    output.extend(reversed(stack))
    return output


def calc(expression):
    is_ready = False
    expresion_list = [expression] # делаем из строки список
    while not is_ready:
        is_ready,expresion_list = find_operations(expresion_list)
    if '' in expresion_list:
        print('Неправлино записано выражение')
        return
    # блок транскрипции чисел
    ready_number_list = []
    numbers_wrong = False
    for number in expresion_list:
        aux_op, number = find_aux_op(number) # ищем особую операцию
        if number in dict_symbol:
            ready_number_list.append(number)
            continue
        if number == 'пи':
            ready_number_list.append(aux_op(pi))
            continue
        ready_number = check_number(number)
        if (ready_number is not None): 
            ready_number_list.append(aux_op(ready_number))
            continue
        elif len(number.split(' и ')) == 2 and not('' in number.split(' и ')): # если число не целое
            int_number = check_number(number.split(' и ')[0])
            dec_number = check_decimal(number.split(' и ')[1])
            if (int_number is not None) and (dec_number is not None): # складываем целую часть и дробную
                ready_number_list.append(aux_op(int_number + dec_number))
            else:
                print('Неправильно записано число: {}'.format(number))
                numbers_wrong = True
        else:
           print('Неправильно записано число: {}'.format(number))
           numbers_wrong = True
    if numbers_wrong: # выходим только здесь, чтобы увидеть все неправильные числа
        return
    #вычисление
    ready_number_list = sort_for_polska(ready_number_list)
    result = polska(ready_number_list)
    #приведение результата в текстовый вид
    new_str_result = ''
    if result == 'Деление на ноль!!!':
        print(result)
        return
    if result<0:
        new_str_result = 'минус '
        result = -result
    if result>9999.0:
        new_str_result += str(result)
    elif isinstance(result,int) or (result % 1 == 0.0):
        new_str_result += translate_number(int(result))
    else:
        int_result = translate_number(trunc(result))
        dec_result = translate_decimal_number(int(result % 1 * 1000))
        new_str_result += ' и '.join([int_result,dec_result])
    print('{} равно {}'.format(expression, new_str_result))

#calc('четыре плюс один плюс восемь')
#calc('четыре плюс один')
#calc('четыре умножить на два')
#calc('четыре разделить на ноль')
#calc('четыре разделить на минус два')
#calc('четыре минус минус два')
#calc('девяносто девять в степени два')
#calc('минус девяносто девять в степени два')
#calc('синус пять')
#calc('пять минус два в степени четыре умножить на два и восемь сотых')
#calc('пять минус ')
#calc('пять минус корова')


