try:
    chislo = int(input('Введите число: '));
    a = 0;
except ValueError:
    print('fef');
finally:
    while (chislo >0):
        if(chislo%2==1):
            a+=1;
            chislo //=2;
        else:
            chislo //=2;
print(a);