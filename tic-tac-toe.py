import random

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


def firstMover():
    rand = random.randint(0,1)
    if rand == 0:
        print("X moves first.")
    else:
        print("O moves first.")


if __name__ == "__main__":
    while True:
        # draw initial stage out first
        dict = makeDict()
        printDict(dict)
        print("\n→ 1  2  3")
        print("↓ 1  2  3")
        print("Please decide who's X or O")
        print("Then enter the coorninates of the blanks of this form: [1,1]")
        # decides who moves first
        firstMover()

        # get the input, input should be in coordinates form:
        # labeling start from [1,1]
        inp = input()
        x = inp[0]
        y = inp[1]
        if x == 1:
            if y == 1:
                dict[0][2] = "O"
            elif y == 2:
                dict[0][6] = "O"
        else:
            None
