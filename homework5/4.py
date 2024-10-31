summa = 0
while True:
    try:
        number = input('Введите число или "stop" или "exit" для выхода: ')
        if (number == 'exit') or (number == 'stop'):
            print('Сумма чисел: ', summa)
            break
        number1 = 0
        number1 = float(number)
    except ValueError: print('Неверный ввод, попробуйте еще раз. ')
    summa += number1
