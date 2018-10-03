## Wydrukuj tablicę
## Postaw kolko lub krzyzyk
## Sprawdz czy gracz wygral
## Nastepny gracz

def tictactoe(game, turn):
    ##Print the board
    print('\n'+game[0] + "|" + game[1] + "|" + game[2])
    print(game[3] + "|" + game[4] + "|" + game[5])
    print(game[6] + "|" + game[7] + "|" + game[8])

    ##Set player's choice
    i = input('\nPodaj indeks \"' + turn + '\": ')
    if not i.isdigit(): exit(1)

    while game[int(i)] != ' ':
        i = input('Indeks zajety, podaj indeks: ')

    #print(game[0:int(i)] + turn + game[int(i)+1:])
    game = game[0:int(i)] + turn + game[int(i)+1:]

    ##Viva Las Vegas
    match = False



    if match: return('\nWygrywa ' + turn + '!')
    elif game.count(' ') == 0:
        return('\nPamietasz \"Gry Wojenne\"?')
    else:

        #Switch player and go again
        if turn == 'o': turn = 'x'
        else: turn ='o'
        tictactoe(game, turn)

##tictactoe(plansza startowa, pierwszy gracz)
print(tictactoe('xoxoxoxo ', 'o'))
