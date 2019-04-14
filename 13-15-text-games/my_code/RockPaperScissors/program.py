

def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------------------')
    print('     ROCK, PAPER, SCISSORS GAME')
    print('--------------------------------------')
    print()


def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)


def build_the_three_rolls():
    pass


def get_players_name():

    Player = input('Enter your name to play: ')
    print(f"Hello {Player}, let's play Rock, Paper, Scissors!")


def game_loop(player1, player2, rolls):
    count = 1
    while count < 3:
        p2_roll = None # TODO: get random roll
        p1_roll = None # TODO: have player choose a roll

        outcome = p1_roll.can_defeat(p2_roll)

        # display throws
        # display winner for this round

        count += 1

    # Compute who won


if __name__ == '__main__':
    main()


