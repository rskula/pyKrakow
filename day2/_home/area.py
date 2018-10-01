#from math import sqrt

figure = input('Wybierz [t]rojkat lub [k]wadrat: ')
if figure == 'k':
    print(int(input('Podaj dlugosc boku: '))**2)
elif figure == 't':
    a = int(input('Podaj dlugosc podstawy: '))
    h = int(input('Podaj wysokosc: '))
    print(a*h/2)
else:
    exit(1)
