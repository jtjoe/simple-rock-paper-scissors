
# Simple Rock Paper Scissors game
import random

menu = "Options: \n   r = Rock\n   p = Paper\n   s = Scissors\n   q = Quit/exit"
print("Welcome to Rock Paper Scissors!" + menu)
player = input('\nPlease enter your choice: ').lower()

def evaluate(player):
    win = "Congrats, you won!"
    lose = "Aww no, you lost!"
    choices = {1:'r', 2:'p', 3:'s'}
    pc = choices[random.randint(1,3)]
    res = f' (Player chose: {player}, PC chose: {pc})'

    if player == pc:
        return "It's a tie! " + res
    if player == 'r':
        if pc == 'p': return lose + res
        if pc == 's': return win + res
    if player == 'p':
        if pc == 'r': return win + res
        if pc == 's': return lose + res
    if player == 's':
        if pc == 'r': return lose + res
        if pc == 'p': return win + res

while player != 'q':
    if player not in ['r','p','s','q']:
        player = input('\nUnknown input, please try again:\n' + menu).lower()
    if player == 'q':
        print("\nThanks for playing!")
        break
    else:
        print(evaluate(player))
    player = input('\nPlay again?:\n' + menu).lower()
print("\nThanks for playing!")
