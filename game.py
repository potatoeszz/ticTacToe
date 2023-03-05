import turtle

MARGIN = 50
BOARDWIDTH = 600
DIMENSION = 3
CELLSIZE = BOARDWIDTH / DIMENSION
DELTA = CELLSIZE / 10

# 2D list to store the game data
data = []
for i in range(DIMENSION):
    temp = []
    for i in range(DIMENSION):
        temp.append(0)
    data.append(temp)

cur_player = 'x' #current player

def checkAnyWin(ln):
    if sum(ln) == DIMENSION:
        return 'x'
    elif sum(ln) == -DIMENSION:
        return 'o'
    return ''

# check who is the winner
def checkWin():
    #check all cols
    for i in range(DIMENSION):
        ln = data[i]
        w = checkAnyWin(ln)
        if w != '':
            return w

    #check all rows
    for i in range(DIMENSION):
        ln = []
        for j in range(DIMENSION):
            ln.append(data[j][i])
        w = checkAnyWin(ln)
        if w != '':
            return w


    #check diagonal 1
    ln = []
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if i == j:
                ln.append(data[j][i])
    w = checkAnyWin(ln)
    if w != '':
        return w


    #check diagonal 2
    ln = []
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if i + j == DIMENSION - 1:
                ln.append(data[j][i])
    w = checkAnyWin(ln)
    if w != '':
        return w

    #till this point, no one win
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if data[i][j] == 0:
                return '' #unsettled

    #till this point, no win, no set up
    return '-' #tie

    return '' #unsettled

def drawXPiece(x, y):
    t = turtle.Turtle()
    t.speed(0)
    t.color('blue')
    t.width(DELTA)
    t.hideturtle
    
    #diagonal
    t.penup()
    t.goto(x - CELLSIZE / 2 + DELTA,y - CELLSIZE / 2 + DELTA)
    t.pendown()
    t.goto(x + CELLSIZE / 2 - DELTA, y + CELLSIZE / 2 - DELTA)
    
    #diagonal line
    t.penup()
    t.goto(x + CELLSIZE / 2 - DELTA, y - CELLSIZE / 2 + DELTA)
    t.pendown()
    t.goto(x - CELLSIZE / 2 + DELTA, y + CELLSIZE / 2 - DELTA)
    pass

def drawOPiece(x, y,):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color('red')
    t.width(5)
    t.penup()
    t.goto(x,y - CELLSIZE / 2 + DELTA)
    t.pendown()
    t.circle(CELLSIZE / 2 - DELTA )
    pass

def drawOPiece2(x,y):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color('red')
    t.width(DELTA)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot(CELLSIZE - DELTA * 2)
    t.color('white')
    t.dot(CELLSIZE - DELTA * 4)

def drawLine(x1, y1, x2, y2):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

def drawBoard():
    turtle.setup(BOARDWIDTH + MARGIN * 2, BOARDWIDTH + MARGIN * 2)
    startX = -BOARDWIDTH / 2
    startY = -BOARDWIDTH / 2

    # draw horizonatl lines
    for i in range(DIMENSION + 1):
        x1 = startX
        y1 = startY + i * BOARDWIDTH / DIMENSION
        x2 = startX + BOARDWIDTH
        y2 = startY + i * BOARDWIDTH / DIMENSION
        drawLine(x1, y1, x2, y2)
    
    # draw verticle lines
    for i in range(DIMENSION + 1):
        x1 = startX + i * BOARDWIDTH / DIMENSION
        y1 = startY
        x2 = startX + i * BOARDWIDTH / DIMENSION
        y2 = startY + BOARDWIDTH
        drawLine(x1, y1, x2, y2)

#drop x piece in the middle of the cell
def dropXPiece(col, row):
    x = -BOARDWIDTH / 2 + col * CELLSIZE + CELLSIZE / 2
    y = -BOARDWIDTH / 2 + row * CELLSIZE + CELLSIZE / 2
    drawXPiece(x,y)
    data[col][row] = 1

def dropOPiece(col, row):
    x = -BOARDWIDTH / 2 + col * CELLSIZE + CELLSIZE / 2
    y = -BOARDWIDTH / 2 + row * CELLSIZE + CELLSIZE / 2
    drawOPiece2(x,y)
    data[col][row] = -1

def xy2ColRow(x, y):
    startX = -BOARDWIDTH / 2
    startY = -BOARDWIDTH / 2
    col = int((x - startX) / CELLSIZE)
    row = int((y - startY) / CELLSIZE)
    #col = int((x + BOARDWIDTH / 2) / CELLSIZE)
    #row = int((y + BOARDWIDTH / 2) / CELLSIZE)
    return col, row

#how to write something on the screen using turtle

def declareWinner(w):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(-BOARDWIDTH / 2, -BOARDWIDTH / 2 - 50)
    #statement = w + ' wins!'
    t.pendown()
    if w == 'x':
        t.color('blue')
    elif w == 'o':
        t.color('red')
    else: #tie
        t.color('black')
        #statement = 'Tie!'
    if w == '-':
        t.write('tie!', font = ('Comic Sans MS', 30, 'normal'))
    elif w != '-':
        t.write(w + ' wins!', font = ('Comic Sans MS', 30, 'normal'))


def handleClick(x, y):
    # if click is outside the board, ignore it
    if x < -BOARDWIDTH / 2 or x > BOARDWIDTH / 2 or y < -BOARDWIDTH / 2 or y > BOARDWIDTH / 2:
        return
    global cur_player
    col, row = xy2ColRow(x, y)
    
    # if piece already exists, ignore it
    if data[col][row] != 0:
        return
   
    if cur_player == 'x':
        dropXPiece(col, row)
        cur_player = 'o'
    else:
        dropOPiece(col, row)
        cur_player = 'x'
    
    w = checkWin()
    if w == '': 
        return
    declareWinner(w)
    answer = turtle.textinput('Play again?', 'Do you want to play again? (y/n)')
    if answer == 'y':
        reset()

def reset():
    global data
    data = [[0 for i in range(DIMENSION)] for j in range(DIMENSION)]
    turtle.clearscreen()
    drawBoard()
    playGame()




def playGame():
    sn = turtle.Screen()
    sn.onclick(handleClick)

# main logic
drawBoard()
playGame()

turtle.done()

#if you see this, allison is an uwu girl