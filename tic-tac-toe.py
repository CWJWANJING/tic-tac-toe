import random
import pdb

 #  O |   | X
 # -----------
 #    | O |
 # -----------
 #    |   |


def makeLine1N3N5():
    line = []
    line.append(" ")
    line.append(" ")
    line.append(" ")
    line.append("|")
    line.append(" ")
    line.append(" ")
    line.append(" ")
    line.append("|")
    line.append(" ")
    line.append(" ")
    line.append(" ")
    return line


def makeLine2N4():
    line = []
    line.append("-----------")
    return line


def makeDict():
    # make a dict which stores the stages components
    line1 = makeLine1N3N5()
    line3 = makeLine1N3N5()
    line5 = makeLine1N3N5()

    line2 = makeLine2N4()
    line4 = makeLine2N4()

    dict = {}
    dict[0] = line1
    dict[1] = line2
    dict[2] = line3
    dict[3] = line4
    dict[4] = line5
    return dict


def printDict(dict):
    for i in range(len(dict)):
        print("".join(dict[i]))
    print("\n→ 1  2  3")
    print("↓ 1  2  3")


def firstMover():
    rand = random.randint(0,1)
    if rand == 0:
        print("X moves first")
        return "X"
    else:
        print("O moves first")
        return "O"


def invalid():
    print("Please enter a valid coordinates")


def drawTheMove(x,y,dict,move):
    if y == 1:
        if x == 1:
            dict[0][1] = move
        elif x == 2:
            dict[0][5] = move
        elif x == 3:
            dict[0][9] = move
        action = str(x)+str(y)
    elif y == 2:
        if x == 1:
            dict[2][1] = move
        elif x == 2:
            dict[2][5] = move
        elif x == 3:
            dict[2][9] = move
        action = str(x)+str(y)
    elif y == 3:
        if x == 1:
            dict[4][1] = move
        elif x == 2:
            dict[4][5] = move
        elif x == 3:
            dict[4][9] = move
        action = str(x)+str(y)
    return dict, action


def switchTurns(move):
    if move == "X":
        return "O"
    else:
        return "X"


def horizontal(dict):
    win = False
    if dict[0][1] == "X" and dict[0][1] == dict[0][5] and dict[0][5] == dict[0][9]:
        print("X wins!")
        win = True
    elif dict[0][1] == "O" and dict[0][1] == dict[0][5] and dict[0][5] == dict[0][9]:
        print("O wins!")
        win = True
    elif dict[2][1] == "X" and dict[2][1] == dict[2][5] and dict[2][5] == dict[2][9]:
        print("X wins!")
        win = True
    elif dict[2][1] == "O" and dict[2][1] == dict[2][5] and dict[2][5] == dict[2][9]:
        print("O wins!")
        win = True
    elif dict[4][1] == "X" and dict[4][1] == dict[4][5] and dict[4][5] == dict[4][9]:
        print("X wins!")
        win = True
    elif dict[4][1] == "O" and dict[4][1] == dict[4][5] and dict[4][5] == dict[4][9]:
        print("O wins!")
        win = True
    return win


def vertical(dict):
    win = False
    if dict[0][1] == "X" and dict[0][1] == dict[2][1] and dict[2][1] == dict[4][1]:
        print("X wins!")
        win = True
    elif dict[0][1] == "O" and dict[0][1] == dict[2][1] and dict[2][1] == dict[4][1]:
        print("O wins!")
        win = True
    elif dict[0][5] == "X" and dict[0][5] == dict[2][5] and dict[2][5] == dict[4][5]:
        print("X wins!")
        win = True
    elif dict[0][5] == "O" and dict[0][5] == dict[2][5] and dict[2][5] == dict[4][5]:
        print("O wins!")
        win = True
    elif dict[0][9] == "X" and dict[0][9] == dict[2][9] and dict[2][9] == dict[4][9]:
        print("X wins!")
        win = True
    elif dict[0][9] == "O" and dict[0][9] == dict[2][9] and dict[2][9] == dict[4][9]:
        print("O wins!")
        win = True
    return win


def cross(dict):
    win = False
    if dict[0][1] == "X" and dict[0][1] == dict[2][5] and dict[2][5] == dict[4][9]:
        print("X wins!")
        win = True
    elif dict[0][1] == "O" and dict[0][1] == dict[2][5] and dict[2][5] == dict[4][9]:
        print("O wins!")
        win = True
    elif dict[0][9] == "X" and dict[0][9] == dict[2][5] and dict[2][5] == dict[4][1]:
        print("X wins!")
        win = True
    elif dict[0][9] == "O" and dict[0][9] == dict[2][5] and dict[2][5] == dict[4][1]:
        print("O wins!")
        win = True
    return win


def checkwin(dict):
    win = False
    if horizontal(dict) or vertical(dict) or cross(dict):
        win = True
    return win


def checkdraw(dict):
    l = []
    l.append(dict[0][1])
    l.append(dict[0][5])
    l.append(dict[0][9])
    l.append(dict[2][1])
    l.append(dict[2][5])
    l.append(dict[2][9])
    l.append(dict[4][1])
    l.append(dict[4][5])
    l.append(dict[4][9])
    draw = True
    for i in l:
        if i == "X" or i == "O":
            draw = draw&True
        else:
            draw = draw&False
    if draw == True:
        print("Draw")
    return draw


def prep():
    dict = makeDict()
    printDict(dict)
    print("Please decide who's X or O")
    print("Then enter the coorninates of the blanks of this form: 11")
    # decides who moves first
    move = firstMover()
    # record the actioned moves
    moveds = []
    return dict, move, moveds


def game(inp, dict, move, moveds):
    win = False
    draw =  False
    x = int(inp[0])
    y = int(inp[1])
    # take the valid move
    dict, action = drawTheMove(x,y,dict,move)
    moveds.append(action)
    printDict(dict)
    # check whether one side wins or not
    win = checkwin(dict)
    if win == False:
        draw = checkdraw(dict)
    if win == False and draw == False:
        # switch the move
        move = switchTurns(move)
        print(f"{move}'s turn:")
    return win, draw, move, moveds


def checkinp(inp):
    inval = False
    # check if inputs are in the range of (1,2,3) or not
    if inp.isdecimal() != True:
        invalid()
        inval = True
    # check if the inputs are numbers
    elif len(inp) != 2 or int(inp[0])<1 or int(inp[0])>3 or int(inp[1])<1 or int(inp[1])>3:
        invalid()
        inval = True
    # check if the move has already been made before
    elif inp in moveds:
        print("This space has been taken, please enter a new one")
        inval = True
    return inval


if __name__ == "__main__":
    # draw initial stage out first
    dict, move, moveds = prep()
    while True:
        # get the input, input should be in coordinates form:
        # labeling start from [1,1]
        inp = input()
        inval = checkinp(inp)
        if inval == False:
            win, draw, move, moveds = game(inp, dict, move, moveds)
            if win:
                break
            # if in the end no win then draw
            if draw:
                break
