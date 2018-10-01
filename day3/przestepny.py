YEAR = input('Podaj rok: ')

if ( int(YEAR) % 4 == 0 and int(YEAR) % 100 != 0 ) or ( int(YEAR) % 4 == 0):
    exit(0)
else:
    exit(1)