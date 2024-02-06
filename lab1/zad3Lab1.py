fact = int(input('Введите число n: '));
factorial = 1;
print('Введённое число: ', fact);
while(fact!=0):
    factorial *= fact;
    fact -= 1;

print(factorial)


