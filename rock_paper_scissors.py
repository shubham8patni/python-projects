import random

def is_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True

def play():
    player = input("Enter your choice! 'r' for rock, 'p' for paper, 's' for scissors \n")
    computer = random.choice(['r', 'p', 's'])

    if player == computer:
        return "It's a Tie!"
    
    if is_win(player, computer):
        return "You win!"
    
    return "You lost!"

print(play())