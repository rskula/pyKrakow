foo = False
while not foo or len(foo) < 8: foo = input('Podaj haslo: ')


bar = False
while True:
    if len(str(bar)) >= 8:
        break
    else:
        bar = input('Podaj drugie haslo: ')