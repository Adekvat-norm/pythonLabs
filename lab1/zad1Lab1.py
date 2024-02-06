
try:
    slovo = input('Введите слово: ');
    print('Дано слово: ', slovo);
    bukva = input('Введите букву: ');
    print(bukva, slovo.index(bukva)+1);
except ValueError:
    print('Не то');
  #print(slovo.index('c'))
