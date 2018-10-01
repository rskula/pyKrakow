TPS = input("Podaj liczbe: ")

if not TPS.isdigit():
    print('Liczbe, mowie.')
else:
    if int(TPS) % 3 == 0: print ('3')
    if int(TPS) % 5 == 0: print ('5')
    if int(TPS) % 7 == 0: print ('7')
