import random
import pdb
import sys
import socket
 #    1   2   3
 # a  O |   | X
 #   -----------
 # b    | O |
 #   -----------
 # c    |   |


def makeLineindexes():
    line = []
    line.append(" ")
    line.append(" ")
    line.append(" ")
    line.append("1")
    line.append(" ")
    line.append(" ")
    line.append(" ")
    line.append("2")
    line.append(" ")
    line.append(" ")
    line.append(" ")
    line.append("3")
    return line


def makeLine1():
    line = []
    line.append("a")
    line.append(" ")
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


def makeLine3():
    line = []
    line.append("b")
    line.append(" ")
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


def makeLine5():
    line = []
    line.append("c")
    line.append(" ")
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
    line.append("  -----------")
    return line


def makeDict():
    # make a dict which stores the stages components
    line0 = makeLineindexes()
    line1 = makeLine1()
    line3 = makeLine3()
    line5 = makeLine5()

    line2 = makeLine2N4()
    line4 = makeLine2N4()

    dict = {}
    dict[0] = line0
    dict[1] = line1
    dict[2] = line2
    dict[3] = line3
    dict[4] = line4
    dict[5] = line5
    return dict


def printDict(dict):
    for i in range(len(dict)):
        print("".join(dict[i]))


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
    if y == "a":
        if x == 1:
            dict[1][3] = move
        elif x == 2:
            dict[1][7] = move
        elif x == 3:
            dict[1][11] = move
        action = str(x)+str(y)
    elif y == "b":
        if x == 1:
            dict[3][3] = move
        elif x == 2:
            dict[3][7] = move
        elif x == 3:
            dict[3][11] = move
        action = str(x)+str(y)
    elif y == "c":
        if x == 1:
            dict[5][3] = move
        elif x == 2:
            dict[5][7] = move
        elif x == 3:
            dict[5][11] = move
        action = str(x)+str(y)
    return dict, action


def switchTurns(move):
    if move == "X":
        return "O"
    else:
        return "X"


def horizontal(dict):
    win = False
    if dict[1][3] == "X" and dict[1][3] == dict[1][7] and dict[1][7] == dict[1][11]:
        print("X wins!")
        win = True
    elif dict[1][3] == "O" and dict[1][3] == dict[1][7] and dict[1][7] == dict[1][11]:
        print("O wins!")
        win = True
    elif dict[3][3] == "X" and dict[3][3] == dict[3][7] and dict[3][7] == dict[3][11]:
        print("X wins!")
        win = True
    elif dict[3][3] == "O" and dict[3][3] == dict[3][7] and dict[3][7] == dict[3][11]:
        print("O wins!")
        win = True
    elif dict[5][3] == "X" and dict[5][3] == dict[5][7] and dict[5][7] == dict[5][11]:
        print("X wins!")
        win = True
    elif dict[5][3] == "O" and dict[5][3] == dict[5][7] and dict[5][7] == dict[5][11]:
        print("O wins!")
        win = True
    return win


def vertical(dict):
    win = False
    if dict[1][3] == "X" and dict[1][3] == dict[3][3] and dict[3][3] == dict[5][3]:
        print("X wins!")
        win = True
    elif dict[1][3] == "O" and dict[1][3] == dict[3][3] and dict[3][3] == dict[5][3]:
        print("O wins!")
        win = True
    elif dict[1][7] == "X" and dict[1][7] == dict[3][7] and dict[3][7] == dict[5][7]:
        print("X wins!")
        win = True
    elif dict[1][7] == "O" and dict[1][7] == dict[3][7] and dict[3][7] == dict[5][7]:
        print("O wins!")
        win = True
    elif dict[1][11] == "X" and dict[1][11] == dict[3][11] and dict[3][11] == dict[5][11]:
        print("X wins!")
        win = True
    elif dict[1][11] == "O" and dict[1][11] == dict[3][11] and dict[3][11] == dict[5][11]:
        print("O wins!")
        win = True
    return win


def cross(dict):
    win = False
    if dict[1][3] == "X" and dict[1][3] == dict[3][7] and dict[3][7] == dict[5][11]:
        print("X wins!")
        win = True
    elif dict[1][3] == "O" and dict[1][3] == dict[3][7] and dict[3][7] == dict[5][11]:
        print("O wins!")
        win = True
    elif dict[1][11] == "X" and dict[1][11] == dict[3][7] and dict[3][7] == dict[5][3]:
        print("X wins!")
        win = True
    elif dict[1][11] == "O" and dict[1][11] == dict[3][7] and dict[3][7] == dict[5][3]:
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
    l.append(dict[1][3])
    l.append(dict[1][7])
    l.append(dict[1][11])
    l.append(dict[3][3])
    l.append(dict[3][7])
    l.append(dict[3][11])
    l.append(dict[5][3])
    l.append(dict[5][7])
    l.append(dict[5][11])
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
    # record the actioned moves
    moveds = []
    return dict, moveds


def game(inp, dict, move, moveds):
    win = False
    draw =  False
    y = inp[0]
    x = int(inp[1])
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


def is_invalid(inp):
    """ Returns True if input invalid, False otherwise"""
    if inp[0].lower() not in ["a", "b", "c"]:
        return True, "First co-ordinate must be a, b or c"
    if len(inp) != 2:
        return True, "You must enter two co-ords"
    if int(inp[1]) not in [1, 2, 3]:
        return True, "Second co-ord has to be number"
    if inp in moveds:
        return True, "This space has been taken, please enter a new one"
    return False, ""

def get_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip != "127.0.0.1" and ip != "::1":
        return ip
    print("Couldn't auto-detect IP, please enter (type ifconfig in terminal)")
    ip = input("> ").strip()
    return ip

if __name__ == "__main__":
    port = 5546
    dict, moveds = prep()
    print("X moves first")
    move = None
    whoami = None
    conn = None
    try:
        # create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # if Server
        if sys.argv[1] == "server":
            ip = "0.0.0.0"
            try:
                s.bind((ip, port))
            except socket.error as e:
                print(str(e))
            s.listen(1)
            print("Server started, waiting for connections")
            # set up accept conn
            conn, addr = s.accept()
            conn.setblocking(True)
            print("Connected to:", addr)
            move = "X"
            whoami = "X"
        # else
        else:
            # ask for IP
            ip = sys.argv[1]
            # connect
            s.setblocking(True)
            s.connect((ip,port))
            move = "X"
            whoami = "O"
            conn = s
        # loop
        while True:
            # if our_turn
            if move == whoami:
                # get input
                inp = input()
                inval, reason = is_invalid(inp)
                if not inval:
                    win, draw, move, moveds = game(inp, dict, move, moveds)
                else:
                    print(reason)
                    continue
                # send to server
                conn.send(str.encode(inp))
            # else
            else:
                # Receive
                print("Waiting for the opponent")
                inp = conn.recv(2048).decode()
                win, draw, move, moveds = game(inp, dict, move, moveds)
            # check win
            if win:
                break
            # if in the end no win then draw
            if draw:
                break
    except Exception as e:
        print(e)
    finally:
        s.close()
