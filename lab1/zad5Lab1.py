numb1 = float(input('Введите первое число: '));
numb2 = float(input('Введите второе число: '));

proc = input('Введите операцию: ');
if (proc == '+'):
    print(numb1+numb2);
try:
    if (proc == '/'):
        print(numb1/numb2);
except ZeroDivisionError:
    print('На ноль делить нельзя');
if (proc == '-'):
    print(numb1-numb2);
if (proc == '*'):
    print(numb1*numb2);