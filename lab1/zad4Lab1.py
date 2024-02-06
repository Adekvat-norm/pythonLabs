try:
    chislo = int(input('Введите двоичное число: '));
except ValueError:
    print('fef');
finally:
    while(chislo>=1):
        numb = chislo%2;
        print();