# This is a script to create the game Rock, Paper, Scissors.
import os, re, time, random

# the wins dictionary will give values for when the key will win
wins = {
    "rock":["scissors","lizard"],
    "paper":["rock","spock"],
    "scissors":["paper","lizard"],
    "lizard":["paper","spock"],
    "spock":["rock","scissors"]
}

# the losses dictionary will give values for when the key will win
losses = {
    "rock":["paper","spock"],
    "paper":["scissors","lizard"],
    "scissors":["rock","spock"],
    "lizard":["rock","scissors"],
    "spock":["paper","lizard"]
}

# the history dictionary will give values for each time a human player has selected an option
history = {
    "rock":1,
    "paper":1,
    "scissors":1,
    "lizard":1,
    "spock":1
}

# this scores dictionary will give values for how many times each player has won when against each other
PvPScores = {
    "player1":0,
    "player2":0,
}

# this scores dictionary will give values for how many times the player has beaten the computer
PvEScores = {
    "player1":0,
    "computer":0,
}

# the winner functions compares the two player objects to declare the winner
def winner(user1, user2):
    print("It's " + user1.name + "'s " + user1.choice + " against " + user2.name + "'s " + user2.choice + "! Who will win???\n")
    if user1.choice == user2.choice:
        timer(1)
        print("Draw...")
    elif user2.choice in wins[user1.choice]:
        timer(3)
        print(user1.name + " wins with " + user1.choice + "!!!")
        scoring(user1,user2)
    else:
        timer(3)
        print(user2.name + " wins with " + user2.choice + "!!!")
        scoring(user2,user2)

# the function finds the correct socring dictionary to alter
def scoring(winner, user2):
    if winner == user2:
        if user2.name == "Computer":
            PvEScores["computer"] += 1
        else:
            PvPScores["player2"] += 1
    else:
        if user2.name == "Computer":
            PvEScores["player1"] += 1
        else:
            PvPScores["player1"] += 1

# a function to allow for pauses in the output
def timer(seconds):
    while seconds >= 0:
        time.sleep(1)
        seconds -= 1

# creates the player as an object
class Player:
    def __init__(self, playerNumber, name, choice): 
        self.playerNumber = playerNumber
        self.name = name
        self.choice = choice

    @classmethod
    def from_input(cls, playerNumber):
        return cls(
            playerNumber,
            input("Player" + str(playerNumber) + " please, enter your name:\n"),
            input('\nNow please chose from: ' + ', '.join(list(wins.keys())[:-1]) + ", or " + list(wins.keys())[-1] + ":\n"),
        )

# this function will take a user input string, and compare it to a list of accepted values
def answerClean(choice, correct):
    choice = choice.lower()
    if choice in correct:
        return choice
    else:
        for i in correct:
            if re.findall("^\s*"+i[0], choice):
                change = input("You entered, "+choice+", did you mean "+i+ "?\n").lower()
                if change.startswith("y"):
                    print("\n")
                    return i
                else:
                   os.system('cls') 
        os.system('cls') 
        newChoice = input("I'm sorry, I don't understand what " + choice + " means.\nPlease enter a correct value from the following: " + ', '.join(correct[:-1]) + ", or " + correct[-1] + "\n")
        return (answerClean(newChoice, correct))

# setting up the game
def gameSetUp():
    os.system('cls')
    print("Hello, and welcome to this game of Rock, Paper, Scissors+ \n")
    numberOfPlayers = input("Do you want to play against a friend or a Computer?\n")
    print("\n")
    if answerClean(numberOfPlayers, ["friend", "computer"]) == "friend":
        PvP(2)
    else:
        PvE(1)

# input for player vs player
def PvP(numberOfPlayers):
    for i in range(numberOfPlayers):
        globals()["user%s" % str(i+1)] = Player.from_input(i+1)
        globals()["user%s" % str(i+1)].choice = answerClean(globals()["user%s" % str(i+1)].choice, list(wins.keys()))
        os.system('cls')
        history[globals()["user%s" % str(i+1)].choice] += 1

# input for player vs AI
def PvE(numberOfPlayers):
    global user1, user2
    user1 = Player.from_input(numberOfPlayers)
    user1.choice = answerClean(user1.choice, list(wins.keys()))
    AI=[]
    for i in list(losses.keys()):
        AI.extend(losses[i]*history[i])
    user2 = Player(2, "Computer", random.choice(AI))
    history[user1.choice] += 1
    os.system('cls')

# show scoreboard
def scoreboard(user2):
    print("\nCURRENT SCORES:")
    if user2.name == "Computer":
        print(PvEScores)
    else:
        print(PvPScores)

# main gameplay loop
def gameplay():
    gameSetUp()
    winner(user1, user2)
    scoreboard(user2)
    playAgain = input("\nDo you want to play again?\n")
    playAgain = answerClean(playAgain, ["yes", "no"])
    if playAgain == "no":
        print("\nThank you for playing")
        return False
    else:
        return True