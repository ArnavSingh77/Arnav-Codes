print("Welcome to the Rock, Paper, Scissors game!")

while True:
    print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
    player_choice = input().lower()
    if player_choice in ['r', 'p', 's']:
        import random
        computer_choice = random.choice(['r', 'p', 's'])
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif player_choice == 'r' and computer_choice == 's':
            result = "You win! Rock beats Scissors."
        elif player_choice == 'p' and computer_choice == 'r':
            result = "You win! Paper beats Rock."
        elif player_choice == 's' and computer_choice == 'p':
            result = "You win! Scissors beat Paper."
        else:
            result = "You lose! Better luck next time."
        print(f"You chose {player_choice} and the computer chose {computer_choice}. {result}")
    elif player_choice == 'q':
        print("Thanks for playing. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# This code takes the player's input and randomly generates a move for the computer. It then determines the winner and prints the result. The game continues until the player enters "q" to quit.
