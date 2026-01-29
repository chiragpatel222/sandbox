import random


class RockPaperScissors:
    def __init__(self):
        self.choices = ["1", "2", "3"]
        self.player_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, player, computer):
        if player == computer:
            return "tie"
        elif (
            (player == "1" and computer == "3")
            or (player == "3" and computer == "2")
            or (player == "2" and computer == "1")
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


def get_choice_name(chosen):
    if chosen == "1":
        return "Rock"
    elif chosen == "2":
        return "Paper"
    elif chosen == "3":
        return "Scissors"


def get_player_choice():
    while True:
        choice = input("Choose your option: ")
        if choice in ["1", "2", "3"]:
            return choice
        print("❌ Invalid choice. Try again.")


def play():
    game = RockPaperScissors()
    print("\n🎮 Welcome to Rock, Paper, Scissors!\n")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    while True:
        player_choice = get_player_choice()
        computer_choice = game.get_computer_choice()

        print(f"\nYou chose: {get_choice_name(player_choice)}")
        print(f"Computer chose: {get_choice_name(computer_choice)}")

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
