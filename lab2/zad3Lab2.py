a=[];
spisok = [a.append(x) for x in input('Введите элементы в списке: ')];
index=0;
while(a):
    bukva = a[index];
    if(a.count(bukva)>=2):
        print(a[index], a.count(bukva));
        while bukva in a:
            a.remove(bukva);
    else:
        a.remove(bukva);