
try:
    slovo = input('Введите слово: ')
    if (slovo == ''):
        print('Это пустое слово...')
    else:
        print('Дано слово: ', slovo)
        bukva = input('Введите букву: ')
        if bukva in slovo:
            index = 0
            for i in slovo:
                if i == bukva:
                    print(bukva, index+1)
                index += 1
except ValueError:
    print('Не то')