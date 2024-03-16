import math;
from basic import add, minus, multiply, delen;
from delWithRemains import delRemains;
from trigonTailor import tailor_sin, tailor_cos, tailor_tg, tailor_ctg;

n = int(input('Что хотите выбрать: \n 1. Базовая арифметика \n 2. Деление с остатком \n 3. Тригонометрические функции по ряду Тейлера'));
if n==1:
    a = int(input('Введите значение 1: '));
    b = int(input('Введите значение 2: '));
    q = int(input('Что хотите выбрать: \n 1. Сложение \n 2. Вычитание \n 3. Умножение \n 4. Деление'));
    if q==1:
        print(add(a,b));
    if q==2:
        print(minus(a,b));
    if q==3:
        print(multiply(a,b));
    if q==4:
        print(delen(a,b));
if n==2:
    a = int(input('Введите значение 1: '));
    b = int(input('Введите значение 2: '));
    print(delRemains(a,b));
if n==3:
    x = int(input('Введите значение x: '));
    q = int(input('Что хотите выбрать: \n 1. Синус \n 2. Косинус \n 3. Тангенц \n 4. Котангенц'));
    if q==1:
        print(tailor_sin(math.pi/x));
    if q==2:
        print(tailor_cos(math.pi/x));
    if q==3:
        print(tailor_tg(math.pi/x));
    if q==4:
        print(tailor_ctg(math.pi/x));
