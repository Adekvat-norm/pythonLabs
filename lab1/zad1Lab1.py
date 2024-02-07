
try:
    slovo = input('Введите слово: ')
    if (slovo == ''):
        print('Это пустое слово...')
    else:
        print('Дано слово: ', slovo)
        bukva = input('Введите букву: ')
        if bukva in slovo:
            print('Индексы буквы "{}" в слове "{}":'.format(bukva, slovo))
            index = 0
            for char in slovo:
                if char == bukva:
                    print(index)
                index += 1
        else:
            print('Буква "{}" не найдена в слове "{}"'.format(bukva, slovo))
except ValueError:
    print('Не то')