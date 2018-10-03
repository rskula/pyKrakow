# Wydrukuj tablicę
# Pobierz indeks o
# Sprawdz czy wygrywa
# Zmien indeks

def tictactoe(game, turn):
    print('\n'+game[0] + "|" + game[1] + "|" + game[2])
    print(game[3] + "|" + game[4] + "|" + game[5])
    print(game[6] + "|" + game[7] + "|" + game[8])

    i = input('\nPodaj indeks \"' + turn + '\": ')
    if not i.isdigit(): exit(1)

    if turn == 'o': turn = 'x'
    else: turn ='o'

    tictactoe(game, turn)
    return(tictactoe)

print('|'+tictactoe('         ', 'o')+'|')
