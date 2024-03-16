import math;

def tailor_sin(x, n=10):
    result = 0;
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    return result

def tailor_cos(x, n=10):
    result = 0;
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    return result

def tailor_tg(x, n=10):
    sin_x = tailor_sin(x, n);
    cos_x = tailor_cos(x, n);
    return sin_x / cos_x

def tailor_ctg(x, n=10):
    sin_x = tailor_sin(x, n);
    cos_x = tailor_cos(x, n);
    return cos_x / sin_x