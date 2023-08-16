import ascii_art
import random

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

ascii_art_list = [ascii_art.rock, ascii_art.paper, ascii_art.scissors]

results_matrix = [["It's a draw", "You lost...", "You win!"],
                  ["You win!", "It's a draw", "You lost..."], 
                  ["You lost...", "You win!", "It's a draw"]]

if user_input < 0 or user_input > 2:
    print("Invalid option. GAME OVER")
else:
    print(ascii_art_list[user_input])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(ascii_art_list[computer_choice])
    print(results_matrix[user_input][computer_choice])
