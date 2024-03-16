a=[];
spisok = [a.append(x) for x in input('Введите элементы списка: ').split(' ')];
a.sort();
print(a[-1]);