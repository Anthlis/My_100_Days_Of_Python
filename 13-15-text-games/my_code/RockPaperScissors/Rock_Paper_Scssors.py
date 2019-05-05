import random

number_matches = int(input("How many matches would you like to play? "))

class Player:
    def __init__(self, name):
        self.name = name
        self.move = None
    def set_move(self, move):
        self.move = move
        
class Game:
    win_moves = {
        "paper : rock", "scissors : paper", "rock : scissors"}
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        
    def get_match_winner(self):
        if self.player1.move == self.player2.move:
            return None
        if Game.win_moves[self.player1.move] == self.player2.move:
            return self.player1
        else:
            return self.player2
        
human = Player("Human")
computer = Player("Computer")

for i in range(number_matches):
    computer.set_move(random.choice(["scissors", "rock", "paper"]))
    human.set_move(input("What is your move? rock, paper or scissors ?"))
    print(computer.name, "played ", computer.move)
    print(human.name, "played ", human.move)
    game = Game(human, computer)
    winner = game.get_match_winner()
    if not winner:
        print("It's a tie!")
    else:
        print(winner.name, "has won the match")
    
    