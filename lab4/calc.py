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
    x = float(input('Введите значение x: '));
    q = int(input('Что хотите выбрать: \n 1. Синус \n 2. Косинус \n 3. Тангенц \n 4. Котангенц'));
    if q==1:
        radianX = math.radians(x);
        sinX = tailor_sin(radianX);
        print(f"Угол в градусах: {x}")
        print(f"Синус угла: {sinX}")
    if q==2:
        radianX = math.radians(x);
        cosX = tailor_cos(radianX);
        print(f"Угол в градусах: {x}")
        print(f"Косинус угла: {cosX}")
    if q==3:
        radianX = math.radians(x);
        tgX = tailor_tg(radianX);
        print(f"Угол в градусах: {x}")
        print(f"Тангенц угла: {tgX}")
    if q==4:
        radianX = math.radians(x);
        ctgX = tailor_ctg(radianX);
        print(f"Угол в градусах: {x}")
        print(f"Котангенц угла: {ctgX}")
