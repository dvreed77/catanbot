import settlers.game

def main():

    quit = False
    while not quit:
        user_input = raw_input('(n)ew game -- (q)uit: ').lower()
        if user_input == 'n':
            game_loop()
        elif user_input == 'q':
            quit = True

def game_loop():

    num_players = int(raw_input('how many players (1-4): '))
    num_bots    = int(raw_input('how many players are bots (0-4): '))
    
    game = settlers.game.Game(num_players, num_bots)

    print ' '.join([p.name for p in game.players])

    game_over = False
    while not game_over:
        quit_response = raw_input('(q) to quit: ')
        if quit_response == 'q':
            game_over = True

if __name__ == "__main__":
    main()