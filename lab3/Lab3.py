import math;

def Number1(X, Y):
    # Ваше арифметическое выражение
    result = 25 + Y / 8 + X**2 + 6 * Y * X - 9 * math.log(X)

    # Округляем результат до целых чисел
    rounded_result = round(result)

    return result, rounded_result

def Number2(X, Y):
    result = Y * math.exp(-X) - 4 + math.log10(27 + Y);
    rounded_result = round(result);
    return result, rounded_result;

n = int(input('Введите уранение которое хотите решить: \n1. 25+Y/8+X2+6YX-9*ln(X) \n2. ye-x-4+ lg(27+y)'));
if n==1:
    X_value = int(input('Введите значение Х: '));
    Y_value = int(input('Введите значение У: '));
    exact_result, rounded_result = Number1(X_value, Y_value)

    print(f"Точный результат: {exact_result}")
    print(f"Округленный результат: {rounded_result}")
if n==2:
    X_value = int(input('Введите значение Х: '));
    Y_value = int(input('Введите значение У: '));
    exact_result, rounded_result = Number2(X_value, Y_value)

    print(f"Точный результат: {exact_result}")
    print(f"Округленный результат: {rounded_result}")
