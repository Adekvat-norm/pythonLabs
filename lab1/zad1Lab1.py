
try:
    slovo = input('Введите слово: ');
    print('Дано слово: ', slovo);
except ValueError:
    print('Не то');
finally:
    bukva = input('Введите букву: ');
print(bukva, slovo.index(bukva)+1);
  #print(slovo.index('c'))
