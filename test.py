import turtle


# start: shape start position
# sidLen: the lenght of the side of the shape
# sideCount: how many sies for the shape
def drawRegularShape(start, sideLen, sideCount, color):
  t = turtle.Turtle()
  t.speed(10)
  t.penup()
  t.color(color)
  t.goto(start)
  t.pendown()
  turnAngle = 180 - (sideCount-2) * 180 / sideCount
  for i in range(sideCount):
    t.forward(sideLen)
    t.right(turnAngle)

def drawRegularTriangle(start, sideLen, sideCount):
  drawRegularShape(start, sideLen, 3, 'red')
  return 3
  
def drawRegularSquare(start, sideLen, sideCount):
  drawRegularShape(start, sideLen, 4, 'green')
  return 4

drawRegularTriangle((0,0), 100, 3)
drawRegularSquare((-100, -100), 100, 4)
turtle.done()