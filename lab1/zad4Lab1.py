try:
    chislo = int(input('Введите двоичное число: '));
    a = 0;
except ValueError:
    print('fef');
finally:
    while (chislo >1):
        if(chislo%2==1):
            a+=1;
        else:
            break;
print(a);