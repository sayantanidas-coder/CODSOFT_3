import random

def get_user_choice():                                      #Giving the choice of Rock, paper, scissors
    while True:
        print("\nChoose one: rock, paper, or scissors")
        choice = input("Your choice: ").capitalize()        #Capitalizing the options written by the user
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid input! Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):                       #Determining the winner of each rounds
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):                 #Displaying the final result 
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("=== Welcome to Rock-Paper-Scissors Game ===")

    while True:
        print(f"\n--- Round {round_number} ---")            #Giving the round number at each game rounds, it's written as (--- Round 1 ---)
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Score => You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != "yes":
            break
        round_number += 1

    print("\n=== Game Over ===")
    print(f"Final Score => You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Computer wins the game. Better luck next time!")
    else:
        print("It's a draw! Thanks for playing.")

if __name__ == "__main__": #main function of the whole program 
    play_game()


