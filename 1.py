number = int(input('Введите число: '))
clas = int(input('Введите целевую систему счисления (2 или 8): '))
while (clas != 2) and (clas != 8):
    print('Данная система счисления не поддерживается. Повторите попытку')
    clas = int(input('Введите целевую систему счисления (2 или 8): '))
if clas == 2:
    print('Вывод: ', number, ' -> ', bin(number)[2:])
else:
    print('Вывод: ', number, ' -> ', oct(number)[2:])


