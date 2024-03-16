def delRemains(a,b):
    if b!=0:
        answer = a//b;
        remains = a%b;
        return answer, remains
    else:
        raise ValueError('На ноль делить нельзя...')