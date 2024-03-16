a = [];
spisok = [a.append(x) for x in input('Введите элементы списка: ').split(' ')];
n = int(input('Какое действие вы хотите сделать?\n 1.Сложение\n 2.Произведение '));
index = 0;
if (n==1):
    summ=0;
    while(index<=len(a)-1):
        summ += int(a[index]);
        index+=1;
        print(summ);
if(n==2):
    umnj=1;
    while(index<=len(a)-1):
        umnj *= int(a[index]);
        index+=1;
        print(umnj);
        
