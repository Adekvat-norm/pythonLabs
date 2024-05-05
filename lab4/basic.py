def add(a,b):
    return a+b;
def minus(a,b):
    return a-b;
def multiply(a,b):
    return a*b;
def delen(a,b):
    if b!=0:
        return a/b;
    else:
        raise ValueError('На ноль делить нельзя...');
