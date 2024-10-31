while True:
    try:
        a = input('Введите первое число: ')
        a = int(round(float(a)))
        b = input('Введите первое число: ')
        b = int(round(float(b)))
        break
    except ValueError: print('Неверный ввод, попробуйте еще раз. ')

for i in range(min(a, b)+1, max(a, b)):
    print(i, end=' ')
