## Wydrukuj tablicę
## Postaw kolko lub krzyzyk
## Sprawdz czy gracz wygral
## Nastepny gracz

def tictactoe(game, turn):
    ##Print the board
    def printboard():
        print('\n' + game[0] + "|" + game[1] + "|" + game[2])
        print(game[3] + "|" + game[4] + "|" + game[5])
        print(game[6] + "|" + game[7] + "|" + game[8] + '\n')

    printboard()

    ##Set player's choice
    i = False
    while not i or not i.isdigit() or int(i) > 8 or game[int(i)] != ' ' : i = input('Podaj nowy indeks \"' + turn + '\": ')

    game = game[0:int(i)] + turn + game[int(i) + 1:]

    ##Viva Las Vegas
    match = False
    if game[0] == game[1] == game[2] == turn: match = True
    if game[3] == game[4] == game[5] == turn: match = True
    if game[6] == game[7] == game[8] == turn: match = True
    if game[0] == game[3] == game[6] == turn: match = True
    if game[1] == game[4] == game[7] == turn: match = True
    if game[2] == game[5] == game[8] == turn: match = True
    if game[0] == game[4] == game[8] == turn: match = True
    if game[2] == game[4] == game[6] == turn: match = True

    if match:
        printboard()
        return ('Wygrywa ' + turn + '!')
    elif game.count(' ') == 0:
        printboard()
        return 'Pamietasz \"Gry Wojenne\"?'
    else:

        # Switch player and go again
        if turn == 'o':
            turn = 'x'
        else:
            turn = 'o'
        return (tictactoe(game, turn))


##tictactoe(plansza startowa, pierwszy gracz)
print(tictactoe('         ', 'o'))
