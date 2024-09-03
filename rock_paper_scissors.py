import random


def game():
    user = (input("Enter your choice of either 'Rock', 'Paper' or 'Scissors': "))
    # to make a random choice
    computer = random.choice(["Rock", "Paper", "Scissors"])

    if user == computer:
        return "We have a TIE"

    def has_won(player, opponent):
        if (player == "Rock" and opponent == "Scissors") or (player == "Paper" and opponent == "Rock") or (
                player == "Scissors" and opponent == "Paper"):
            return True

    if has_won(user, computer):
        return "You Win!"

    return "You Lose!"


print(game())
