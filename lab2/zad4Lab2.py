a=[];
spisok = [a.append(x) for x in input('Введите элементы в списке: ').split(' ')];
largest = a[0];
smallest = a[0];
largest_index = 0;
smallest_index = 0;
for i, numb in enumerate(a):
    if numb>largest:
        largest=numb;
        largest_index = i;
    if numb<smallest:
        smallest=numb;
        smallest_index = i;
a[largest_index], a[smallest_index] = a[smallest_index], a[largest_index];
print(a);

