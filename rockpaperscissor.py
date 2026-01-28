import random


class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, player, computer):
        if player == computer:
            return "tie"
        elif (
            (player == "rock" and computer == "scissors")
            or (player == "scissors" and computer == "paper")
            or (player == "paper" and computer == "rock")
        ):
            return "player"
        else:
            return "computer"

    def update_score(self, winner):
        if winner == "player":
            self.player_score += 1
        elif winner == "computer":
            self.computer_score += 1

    def display_score(self):
        print(f"\nScore → You: {self.player_score} | Computer: {self.computer_score}")


def get_player_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("❌ Invalid choice. Try again.")


def play():
    game = RockPaperScissors()
    print("\n🎮 Welcome to Rock, Paper, Scissors!\n")

    while True:
        player_choice = get_player_choice()
        computer_choice = game.get_computer_choice()

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = game.determine_winner(player_choice, computer_choice)
        game.update_score(winner)

        if winner == "tie":
            print("🤝 It's a tie!")
        elif winner == "player":
            print("🎉 You win this round!")
        else:
            print("💻 Computer wins this round!")

        game.display_score()

        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("\n👋 Thanks for playing!")
            break


play()
