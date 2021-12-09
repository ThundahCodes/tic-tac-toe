from tkinter import *
import random


def turn(row, column):
    global player

    if ticButtons[row][column]['text'] == "" and winner() is False:
        if player == players[0]:

            ticButtons[row][column]['text'] = player

            if winner() is False:
                player = players[1]
                turns.config(text=(players[1]+ "'s turn"))

            elif winner() is True:
                turns.config(text=(players[0] + " wins"))

            elif winner() == "Tie":
                turns.config(text=("Tie"))

        else:

            ticButtons[row][column]['text'] = player

            if winner() is False:
                player = players[0]
                turns.config(text=(players[0]+ "'s turn"))

            elif winner() is True:
                turns.config(text=(players[1] + " wins"))

            elif winner() == "Tie":
                turns.config(text=("Tie"))

def winner():
    

    for row in range(3):
        if ticButtons[row][0]['text'] == ticButtons[row][1]['text'] == ticButtons[row][2]['text'] != "":
            ticButtons[row][0].config(bg="green")
            ticButtons[row][1].config(bg="green")
            ticButtons[row][2].config(bg="green")
            return True
    
    for column in range(3):
        if ticButtons[0][column]['text'] == ticButtons[1][column]['text'] == ticButtons[2][column]['text'] != "":
            ticButtons[0][column].config(bg="green")
            ticButtons[1][column].config(bg="green")
            ticButtons[2][column].config(bg="green")
            return True

    if ticButtons[0][0]['text'] == ticButtons[1][1]['text'] == ticButtons[2][2]['text'] != "":
        ticButtons[0][0].config(bg="green")
        ticButtons[1][1].config(bg="green")
        ticButtons[2][2].config(bg="green")
        return True

    elif ticButtons[0][2]['text'] == ticButtons[1][1]['text'] == ticButtons[2][0]['text'] != "":
        ticButtons[0][2].config(bg="green")
        ticButtons[1][1].config(bg="green")
        ticButtons[2][0].config(bg="green")    
        return True    

    elif empty_space() is False:
        
        for row in range(3):
            for column in range(3):
                ticButtons[row][column].config(bg="red")
        return "Tie"

    else:
        return False

def empty_space():
    
    spaces = 9

    for row in range(3):
        for column in range(3):
            if ticButtons[row][column]['text'] != "":
                spaces -= 1
    
    if spaces == 0:
        return False
    else:
        return True

def restart():
    
    global player

    player = random.choice(players)

    turns.config(text= player + "'s turn")

    for row in range(3):
        for column in range(3):
            ticButtons[row][column].config(text="", bg="#F0F0F0")

game = Tk()
game.title("Tic-Tac-Toe Game")
players = ["X" , "O"]
player = random.choice(players)
ticButtons = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]

turns = Label(text = player + "'s turn", font=('Arial', 30))
turns.pack(side="top")

reset = Button(text="Reset", font=('Arial', 20), command=restart)
reset.config(bg="red")
reset.pack(side="top")


frame = Frame(game)
frame.pack()

for row in range(3):
    for column in range(3):
        ticButtons[row][column] = Button(frame, text="", font=('Arial', 30), width=4, height=2, command= lambda row = row, column = column: turn(row, column))
        ticButtons[row][column].grid(row=row,column=column)

game.mainloop()