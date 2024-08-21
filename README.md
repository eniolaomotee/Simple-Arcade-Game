# A Simple Arcade Game 

Welcome to the Arcade Game - a fun and interactive game experience where you can challenge yourself with two classic games: Rock Paper Scissors and Guess My Number.


## Description
The Arcade Game combines two popular games into a single gaming experience. Players can choose to play either Rock Paper Scissors or Guess My Number, all within a personalized game environment.

The game uses command-line arguments to get the player's name, allowing for a more personalized experience. On Windows, the game can be run using the command py game_lobby.py -n "user name", while on macOS, the command is python3 game_lobby.py -n "user name".


## Features
Rock Paper Scissors: Challenge the computer in a classic game of Rock Paper Scissors.
Guess My Number: Try to guess the computer's randomly generated number.
Personalized Game Experience: The game uses the player's name, which is provided through command-line arguments.
Arcade-style Menu: The game presents the player with a menu of available games and options.

## Installation
To run the Arcade Game, you'll need to have Python 3 installed on your system. You can download the latest version of Python from the official website: https://www.python.org/downloads/
Once you have Python installed, you can clone the repository and run the game:

## Clone the repository:
git clone https://github.com/eniolaomotee/Simple-Arcade-Game/


## Run the game:

Windows: py game_lobby.py -n "user name"
macOS: python3 game_lobby.py -n "user name"



## Usage
Run the game using the appropriate command for your operating system.
Enter your name when prompted.
Choose from the available games (Rock Paper Scissors or Guess My Number) or select 'x' to exit the arcade.
Enjoy playing the selected game!

## Concepts Learned
In the development of this Arcade Game, the following Python concepts were applied:

Command-line Arguments: The game uses the argparse module to accept the player's name as a command-line argument, providing a personalized experience.
Closures: The game makes use of closures to encapsulate the game logic and state within the rps and num functions.
Recursion: The game employs recursion in the play_arcade function to handle invalid user input and restart the game loop.
