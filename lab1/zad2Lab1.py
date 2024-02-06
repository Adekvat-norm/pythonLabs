n = int(input('Введите число n: '));
prev = 0;
cur = 1;
while (prev < n):
    print(prev, end='');
    prev, cur = cur, prev+cur;
    print();