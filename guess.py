
import random
import sys
import argparse

def num(name="PlayerOne"):
    game_count = 0
    player_win = 0

    def play_guess():
        nonlocal name
        print("\n********GUESS THE NUMBER BETWEEN 1-3 ************ \n")
        playerchoice = input(f" {name},you choose  ")
        computerchoice = random.choice("123")
        print(f"I was thinking of the number {computerchoice}")
        

        if playerchoice not in ["1","2","3"]:
            print(f"{name}, Please choose a number between 1, 2 and 3")
            return play_guess()
        
        player = int(playerchoice)
        computer = int(computerchoice)


        def winner(player,computer):
            nonlocal player_win
            if player == computer:
                player_win += 1
                return f"{name}, You got the Number right"
            else:
                return f"{name}, You didn't get the number"
        

        game = winner(player,computer)
        print(game)

        nonlocal game_count
        game_count += 1

        print(f"Game count : {game_count}")
        print(f" {name}'s win : {player_win}")

        winning = (player_win / game_count) * 100

        print(f"Your winning percentage : {winning:.2f}% \n")  

        print(f"Play again, {name}? \n")

        while True:
            play_again = input("\n Y for Yes or \n Q for Quit\n")
            if play_again.lower() not in ["y","q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_guess()
        else:
            print("\nThanks for playing")
            if __name__ == "__main__":
                sys.exit(f"bye {name} !!!!")
            else:
                return
            

    return play_guess


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n","--name", metavar="name",
        required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()

    guess_number = num(args.name)

    guess_number()