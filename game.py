import sys
import random
from enum import Enum 
import argparse

def rps(name="PlayerOne"):
    game_count  = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        print("\n******** ROCK PAPER SCISSORS GAME ************ \n")

        playerchoice = input(f"\n {name}, enter....\n 1 for Rock 🪨 , \n 2 for Paper 📄, \n 3 for Scissors ✄ \n\n ")

        if playerchoice not in ["1","2","3"]:
            print(f"{name}, you must enter  1,2 or 3")
            return play_rps()

        player = int(playerchoice)


        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\n {name}, you choose {str(RPS(player)).replace('RPS.', '').title()}.")

        print(
            f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
        )

        def decide_winner(player,computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer ==3:
                player_wins +=1
                return f"🎉🎉🎉{name},you win"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉🎉 {name},you win"
            elif player == 3 and computer == 2:
                player_wins +=1 
                return f"🎉🎉{name}, you win"
            elif player == computer:
                return"🤝It is a draw game"
            else:
                python_wins +=1
                return"🐍Python Wins"
            

        game_results = decide_winner(player,computer)

        print(game_results)


        nonlocal game_count
        game_count += 1


        print(f"\n Game count is {game_count}")
        print(f"\n {name} Wins {player_wins}")
        print(f"\n Python Wins {python_wins}")


        print("\n Play Again?")

        while True:
            playagain = input("\n Y for yes or Q to Quit \n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n Thank you for playing \n")
            if __name__ == "__main__":
                sys.exit(f"Bye 🎉 {name} \n")
            else:
                return
        
    return play_rps



if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n","--name", metavar="name",
        required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)

    rock_paper_scissors()
