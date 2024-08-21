import sys
from guess import num
from game import rps
import argparse

def play_arcade(name="PlayerOne"):
    welcome_back = False

    while True:
        if welcome_back:
            print(f"\n {name} Welcome back to the Arcade Menu")

        playerchoice = input(f"Please Choose a game: \n 1 = Rock Paper Scissors \n 2 = Guess my Number \n or Press 'x' to exit or switch the Arcade   ")

        if playerchoice not in ["1","2","x"]:
            print("Please select an Option")
            return play_arcade()
    

        welcome_back = True
        if playerchoice == "1":
            rock_paper_scissors = rps()
            rock_paper_scissors()
        elif playerchoice == "2":
            guess = num()
            guess()
        else:
            print("\n See you next time! \n")
            sys.exit(f"\n Bye {name} !! \n")

parser = argparse.ArgumentParser(
    description="Provides a personalized game Experience"
)

parser.add_argument(
    "-n","--name",metavar="name",
    required=True, help="The name of the Person playing the game"
)

args = parser.parse_args()

print(f"\n {args.name}, welcome to the Arcade")

play_arcade(args.name)
