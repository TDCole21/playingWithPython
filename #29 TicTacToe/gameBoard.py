# This is a script to create the game Rock, Paper, Scissors.
import os, re, time, random

# This function will take a user input string, and compare it to a list of accepted values.
# This has been improved from the function found in RPS to include the original question.
def answerClean(choice, correct, question):
    choice = choice.lower()
    if choice in correct:
        os.system('cls') 
        return choice
    else:
        for i in correct:
            if re.findall("^\s*"+i[0], choice):
                change = input("You entered, "+choice+", did you mean "+i+ "?\n").lower()
                if change.startswith("y"):
                    print("\n")
                    os.system('cls')
                    return i
                else:
                   os.system('cls') 
        os.system('cls') 
        newChoice = input("I'm sorry, I don't understand what " + choice + " means.\n" + question + "\nPlease enter a correct value from the following: " + ', '.join(correct[:-1]) + ", or " + correct[-1] + "\n")
        return (answerClean(newChoice, correct, question))


# This will print out a horizontal line per number of columns
def print_x_line(board_size):
    print(" ---" * board_size)


# This will print out a a vertical line per number of columns plus 1 for the end.
def print_y_line(board_size):
    print("|   " * (board_size+1))


# This will take the board size and print the appropriate number of horizontal and vertical lines
def print_board(x_board_size, y_board_size):
    os.system('cls') 
    for index in range(y_board_size):
        print_x_line(x_board_size)
        print_y_line(x_board_size)
    print_x_line(x_board_size)


# This is the game loop
if __name__ == "__main__":
    question = "Do you want a square board?"
    if answerClean(input(question+"\n"),["yes","no"],question) == "yes":
        board_size = int(input("Great, lets make this a square board.\nWhat is size of game board?\n"))
        print_board(board_size, board_size)
    else:
        x_board_size = int(input("Cool, lets make this a rectangular board.\nHow many columns on the game board?\n"))
        y_board_size = int(input("How many rows on the game board?\n"))
        print_board(x_board_size, y_board_size)