while True:
    try:
        a = input('Введите число а: ')
        if a == '': break
        a = int(a)
        b = int(input('Введите число b: '))
        print(f'Сумма a+b = {a+b}')
    except ValueError: print("Неверный ввод. Попробуйте еще раз.")
