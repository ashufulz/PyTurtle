import turtle
import random


# Setting up screen
win = turtle.Screen()
win.title("Name 1300x700")
win.bgcolor('black')
win.setup(width=1300, height=700)
win.tracer(1)           # Screen updates: 0 - Off, 1 - On

t = turtle.Turtle()
t.penup()
t.hideturtle()
t.speed(0)              # 0: Fastest; 5: Medium; 1: Slowest
screen_x = -550
screen_y = 50
box = 100


# Making invisible Box for each character
def BoxMaking():
    t.goto(screen_x, screen_y)
    t.pendown()
    t.color('white')
    t.forward(box)
    t.left(90)
    t.forward(box)
    t.left(90)
    t.forward(box)
    t.left(90)
    t.forward(box)
    t.left(90)
    t.penup()


# -----------------------------------------------
# Set the name here
# -----------------------------------------------
name = 'LOVE'           # Keep it upto MAX 4 characters only, if increased then every line below needs to be modified.
global alpha

alphanumerals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z',
                 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# Colors
def clr():
    win.colormode(255)
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    return r, g, b


# -----------------------------------------------
# Initializing Backbone
# -----------------------------------------------
t.pensize(40)
t.backward(650)
t.left(90)
t.forward(250)


def fullfill():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(250)
    t.backward(250)
    t.penup()
    t.left(90)


def first():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(45)
    t.backward(45)
    t.penup()
    t.left(90)


def mid():
    t.color(clr())
    t.right(90)
    t.forward(102.5)
    t.pendown()
    t.forward(45)
    t.penup()
    t.backward(146.5)
    t.left(90)


def last():
    t.color(clr())
    t.right(90)
    t.forward(205)
    t.pendown()
    t.forward(45)
    t.penup()
    t.backward(250)
    t.left(90)


def firstmid():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(156)
    t.backward(156)
    t.penup()
    t.left(90)


def threefourth():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(203)
    t.backward(203)
    t.penup()
    t.left(90)


def midlast():
    t.color(clr())
    t.right(90)
    t.forward(94)
    t.pendown()
    t.forward(156)
    t.penup()
    t.backward(250)
    t.left(90)


def firstlast():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(45)
    t.penup()
    t.forward(160)
    t.pendown()
    t.forward(45)
    t.penup()
    t.backward(250)
    t.left(90)


def oneright():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(222)
    t.backward(222)
    t.penup()
    t.left(90)


def oneleft():
    t.color(clr())
    t.right(90)
    t.forward(250)
    t.pendown()
    t.backward(222)
    t.penup()
    t.backward(28)
    t.left(90)


def oneboth():
    t.color(clr())
    t.right(90)
    t.forward(28)
    t.pendown()
    t.forward(194)
    t.backward(194)
    t.penup()
    t.backward(28)
    t.left(90)


def nextline():
    t.backward(50)


def space():
    t.right(90)
    t.forward(320)      # actual space between two characters
    t.left(90)
    t.forward(500)      # nextline(backward) * 10


def g404():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(80)
    t.penup()
    t.forward(90)
    t.pendown()
    t.forward(80)
    t.penup()
    t.backward(250)
    t.left(90)


def g304():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(45)
    t.penup()
    t.forward(125)
    t.pendown()
    t.forward(80)
    t.penup()
    t.backward(250)
    t.left(90)


def g302():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(45)
    t.penup()
    t.forward(175)
    t.pendown()
    t.forward(30)
    t.penup()
    t.backward(250)
    t.left(90)


def j203():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(20)
    t.penup()
    t.forward(82.5)
    t.pendown()
    t.forward(45)
    t.penup()
    t.backward(147.5)
    t.left(90)


def j030():
    t.color(clr())
    t.right(90)
    t.forward(25)
    t.pendown()
    t.forward(110)
    t.penup()
    t.backward(135)
    t.left(90)


def j040():
    t.color(clr())
    t.right(90)
    t.forward(45)
    t.pendown()
    t.forward(75)
    t.penup()
    t.backward(120)
    t.left(90)


def kr30030():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(45)
    t.penup()
    t.forward(132)
    t.pendown()
    t.forward(45)
    t.penup()
    t.backward(222)
    t.left(90)


def kr30300():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(45)
    t.penup()
    t.forward(96)
    t.pendown()
    t.forward(45)
    t.penup()
    t.backward(186)
    t.left(90)


def kr330():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(45)
    t.penup()
    t.forward(57.5)
    t.pendown()
    t.forward(45)
    t.penup()
    t.backward(147.5)
    t.left(90)


def _004000_():
    t.color(clr())
    t.right(90)
    t.forward(56)
    t.pendown()
    t.forward(110)
    t.penup()
    t.backward(166)
    t.left(90)


def _05000_():
    t.color(clr())
    t.right(90)
    t.forward(28)
    t.pendown()
    t.forward(138)
    t.penup()
    t.backward(166)
    t.left(90)


def left7():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(194)
    t.backward(194)
    t.penup()
    t.left(90)


def left5():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(122)
    t.penup()
    t.backward(122)
    t.left(90)


def left4():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(90)
    t.penup()
    t.backward(90)
    t.left(90)


def right7():
    t.color(clr())
    t.right(90)
    t.forward(56)
    t.pendown()
    t.forward(194)
    t.penup()
    t.backward(250)
    t.left(90)


def mqw404():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(90)
    t.penup()
    t.forward(70)
    t.pendown()
    t.forward(90)
    t.penup()
    t.backward(250)
    t.left(90)


def mqw30103():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(45)
    t.penup()
    t.forward(72.5)
    t.pendown()
    t.forward(15)
    t.penup()
    t.forward(72.5)
    t.pendown()
    t.forward(45)
    t.penup()
    t.backward(250)
    t.left(90)


def last1():
    t.color(clr())
    t.right(90)
    t.forward(235)
    t.pendown()
    t.forward(15)
    t.penup()
    t.backward(250)
    t.left(90)


def avxy03030():
    t.color(clr())
    t.right(90)
    t.forward(28)
    t.pendown()
    t.forward(45)
    t.penup()
    t.forward(104)
    t.pendown()
    t.forward(45)
    t.penup()
    t.backward(222)
    t.left(90)


def avxy050():
    t.color(clr())
    t.right(90)
    t.forward(56)
    t.pendown()
    t.forward(138)
    t.penup()
    t.backward(194)
    t.left(90)


def avxy030():
    t.color(clr())
    t.right(90)
    t.forward(84)
    t.pendown()
    t.forward(82)
    t.penup()
    t.backward(166)
    t.left(90)


def avxy010():
    t.color(clr())
    t.right(90)
    t.forward(112)
    t.pendown()
    t.forward(26)
    t.penup()
    t.backward(138)
    t.left(90)


def midleft():
    t.color(clr())
    t.right(90)
    t.forward(68.33)
    t.pendown()
    t.forward(45)
    t.penup()
    t.backward(113.33)
    t.left(90)


def midleftmost():
    t.color(clr())
    t.right(90)
    t.forward(34.16)
    t.pendown()
    t.forward(45)
    t.penup()
    t.backward(79.16)
    t.left(90)


def midright():
    t.color(clr())
    t.right(90)
    t.forward(136.66)
    t.pendown()
    t.forward(45)
    t.penup()
    t.backward(181.66)
    t.left(90)


def midrightmost():
    t.color(clr())
    t.right(90)
    t.forward(170.82)
    t.pendown()
    t.forward(45)
    t.penup()
    t.backward(215.82)
    t.left(90)


def n403():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(80)
    t.penup()
    t.forward(125)
    t.pendown()
    t.forward(45)
    t.penup()
    t.backward(250)
    t.left(90)


def n503():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(115)
    t.penup()
    t.forward(90)
    t.pendown()
    t.forward(45)
    t.penup()
    t.backward(250)
    t.left(90)


def n304():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(45)
    t.penup()
    t.forward(125)
    t.pendown()
    t.forward(80)
    t.penup()
    t.backward(250)
    t.left(90)


def n305():
    t.color(clr())
    t.right(90)
    t.pendown()
    t.forward(45)
    t.penup()
    t.forward(90)
    t.pendown()
    t.forward(115)
    t.penup()
    t.backward(250)
    t.left(90)


# -----------------------------------------------
# Alphabet Code
# -----------------------------------------------
def A():
    avxy010()
    nextline()
    avxy030()
    nextline()
    avxy050()
    nextline()
    avxy03030()

    nextline()
    firstlast()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()

    space()


def B():
    oneright()
    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    firstlast()
    nextline()
    fullfill()

    nextline()
    oneright()
    nextline()
    fullfill()
    nextline()
    firstlast()
    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    oneright()

    space()


def C():
    oneboth()

    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    firstlast()

    nextline()
    first()
    nextline()
    first()
    nextline()
    first()

    nextline()
    firstlast()

    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    oneboth()

    space()


def D():
    oneright()

    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()

    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    oneright()

    space()


def E():
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    first()

    nextline()
    firstmid()
    nextline()
    firstmid()
    nextline()
    firstmid()

    nextline()
    first()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    space()


def F():
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    first()

    nextline()
    firstmid()
    nextline()
    firstmid()
    nextline()
    firstmid()

    nextline()
    first()
    nextline()
    first()
    nextline()
    first()
    nextline()
    first()

    space()


def G():
    oneboth()
    nextline()
    fullfill()
    nextline()
    g404()

    nextline()
    g302()
    nextline()
    first()

    nextline()
    g304()
    nextline()
    firstlast()

    nextline()
    firstlast()
    nextline()
    g404()

    nextline()
    fullfill()
    nextline()
    oneboth()

    space()


def H():
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()

    space()


def I():
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    mid()
    nextline()
    mid()
    nextline()
    mid()
    nextline()
    mid()
    nextline()
    mid()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    space()


def J():
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    mid()
    nextline()
    mid()
    nextline()
    mid()
    nextline()
    mid()

    nextline()
    j203()
    nextline()
    firstmid()
    nextline()
    j030()
    nextline()
    j040()

    space()


def K():
    firstlast()

    nextline()
    kr30030()
    nextline()
    kr30300()

    nextline()
    firstmid()
    nextline()
    left5()
    nextline()
    left4()

    nextline()
    left5()
    nextline()
    firstmid()

    nextline()
    kr30300()
    nextline()
    kr30030()
    nextline()
    firstlast()

    space()


def L():
    first()
    nextline()
    first()
    nextline()
    first()
    nextline()
    first()
    nextline()
    first()
    nextline()
    first()
    nextline()
    first()
    nextline()
    first()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    space()


def M():
    firstlast()
    nextline()
    mqw404()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    mqw30103()

    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()

    space()


def N():
    firstlast()

    nextline()
    n403()
    nextline()
    n403()
    nextline()
    n503()
    nextline()
    n503()

    nextline()
    mqw30103()

    nextline()
    n305()
    nextline()
    n305()
    nextline()
    n304()
    nextline()
    n304()

    nextline()
    firstlast()

    space()


def O():
    avxy050()
    nextline()
    oneboth()
    nextline()
    fullfill()

    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()

    nextline()
    fullfill()
    nextline()
    oneboth()
    nextline()
    avxy050()

    space()


def P():
    oneright()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    firstlast()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    oneright()

    nextline()
    first()
    nextline()
    first()
    nextline()
    first()
    nextline()
    first()

    space()


def Q():
    oneboth()

    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()

    nextline()
    mqw30103()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    oneboth()
    nextline()
    last1()

    space()


def R():
    # oneright()
    firstmid()
    nextline()
    threefourth()
    nextline()
    fullfill()

    nextline()
    firstlast()

    nextline()
    fullfill()
    nextline()
    threefourth()
    nextline()
    firstmid()

    nextline()
    kr330()
    nextline()
    kr30300()
    nextline()
    kr30030()
    nextline()
    firstlast()

    space()


def S():
    oneleft()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    first()

    nextline()
    oneright()
    nextline()
    fullfill()
    nextline()
    oneleft()

    nextline()
    last()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    oneright()

    space()


def T():
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    mid()
    nextline()
    mid()
    nextline()
    mid()
    nextline()
    mid()
    nextline()
    mid()
    nextline()
    mid()
    nextline()
    mid()
    nextline()
    mid()

    space()


def U():
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()

    nextline()
    mqw404()
    nextline()
    oneboth()
    nextline()
    avxy050()

    space()


def V():
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()

    nextline()
    avxy03030()
    nextline()
    avxy050()
    nextline()
    avxy030()
    nextline()
    avxy010()

    space()


def W():
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()

    nextline()
    mqw30103()

    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    mqw404()
    nextline()
    firstlast()

    space()


def X():
    firstlast()
    nextline()
    avxy03030()
    nextline()
    avxy050()

    nextline()
    avxy030()

    nextline()
    avxy050()
    nextline()
    avxy03030()
    nextline()
    firstlast()

    space()


def Y():
    firstlast()

    nextline()
    avxy03030()
    nextline()
    avxy050()

    nextline()
    avxy030()
    nextline()
    mid()
    nextline()
    mid()
    nextline()
    mid()

    space()


def Z():
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    midrightmost()
    nextline()
    midright()
    nextline()
    mid()
    nextline()
    midleft()
    nextline()
    midleftmost()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    space()


def zero():
    oneboth()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    oneboth()

    space()


def one():
    avxy030()
    nextline()
    _004000_()
    nextline()
    _05000_()

    nextline()
    avxy030()
    nextline()
    avxy030()
    nextline()
    avxy030()
    nextline()
    avxy030()
    nextline()
    avxy030()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    space()


def two():
    oneboth()
    nextline()
    fullfill()
    nextline()
    firstlast()
    nextline()

    midrightmost()
    nextline()
    midright()
    nextline()
    mid()
    nextline()
    midleft()
    nextline()
    midleftmost()
    nextline()

    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    space()


def three():
    oneboth()
    nextline()
    fullfill()
    nextline()
    firstlast()
    nextline()

    midrightmost()
    nextline()
    midright()
    nextline()
    mid()
    nextline()
    midright()
    nextline()
    midrightmost()
    nextline()

    firstlast()
    nextline()
    fullfill()
    nextline()
    oneboth()

    space()


def four():
    midrightmost()
    nextline()
    midright()
    nextline()
    mid()
    nextline()
    midleft()
    nextline()
    midleftmost()
    nextline()

    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()

    last()
    nextline()
    last()
    nextline()
    last()

    space()


def five():
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()

    first()
    nextline()

    left7()
    nextline()
    oneright()
    nextline()
    fullfill()
    nextline()

    last()
    nextline()

    fullfill()
    nextline()
    oneright()
    nextline()
    left7()

    space()


def six():
    avxy050()
    nextline()
    oneboth()
    nextline()
    firstlast()
    nextline()
    first()
    nextline()

    left7()
    nextline()
    oneright()
    nextline()
    fullfill()
    nextline()
    firstlast()
    nextline()

    fullfill()
    nextline()
    oneboth()
    nextline()
    avxy050()

    space()


def seven():
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()

    last()
    nextline()
    last()
    nextline()

    midrightmost()
    nextline()
    midright()
    nextline()
    mid()
    nextline()
    midleft()
    nextline()
    midleftmost()
    nextline()
    first()

    space()


def eight():
    avxy050()
    nextline()
    oneboth()
    nextline()
    fullfill()
    nextline()
    firstlast()
    nextline()

    fullfill()
    nextline()
    oneboth()
    nextline()
    fullfill()
    nextline()

    firstlast()
    nextline()
    fullfill()
    nextline()
    oneboth()
    nextline()
    avxy050()

    space()


def nine():
    avxy050()
    nextline()
    oneboth()
    nextline()
    fullfill()
    nextline()
    firstlast()
    nextline()

    fullfill()
    nextline()
    oneleft()
    nextline()
    right7()
    nextline()
    last()
    nextline()

    firstlast()
    nextline()
    oneboth()
    nextline()
    avxy050()

    space()


# -----------------------------------------------
# Main Function Caller
# -----------------------------------------------
def AlphaIterator():
    for i in range(len(alphanumerals)):
        if alphanumerals[i] == alpha:
            if alpha == 'A':
                A()
            elif alpha == 'B':
                B()
            elif alpha == 'C':
                C()
            elif alpha == 'D':
                D()
            elif alpha == 'E':
                E()
            elif alpha == 'F':
                F()
            elif alpha == 'G':
                G()
            elif alpha == 'H':
                H()
            elif alpha == 'I':
                I()
            elif alpha == 'J':
                J()
            elif alpha == 'K':
                K()
            elif alpha == 'L':
                L()
            elif alpha == 'M':
                M()
            elif alpha == 'N':
                N()
            elif alpha == 'O':
                O()
            elif alpha == 'P':
                P()
            elif alpha == 'Q':
                Q()
            elif alpha == 'R':
                R()
            elif alpha == 'S':
                S()
            elif alpha == 'T':
                T()
            elif alpha == 'U':
                U()
            elif alpha == 'V':
                V()
            elif alpha == 'W':
                W()
            elif alpha == 'X':
                X()
            elif alpha == 'Y':
                Y()
            elif alpha == 'Z':
                Z()
            elif alpha == '1':
                one()
            elif alpha == '2':
                two()
            elif alpha == '3':
                three()
            elif alpha == '4':
                four()
            elif alpha == '5':
                five()
            elif alpha == '6':
                six()
            elif alpha == '7':
                seven()
            elif alpha == '8':
                eight()
            elif alpha == '9':
                nine()
            elif alpha == '0':
                zero()


# Displays each character of the 'name'
for i in range(len(name)):
    alpha = name[i]
    AlphaIterator()

# Main Loop
while True:
    win.update()
