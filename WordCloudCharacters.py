import turtle
import random

girl_adj = [' Adorable ', ' Amazing ', ' Attractive ', ' Alluring ', ' Audacious ', ' Adaptable ', ' Adventurous ',
            ' Affable ', ' Affectionate ', ' Ambitious ', ' Amusing ', ' Awesome ', ' Beautiful ', ' Bold ', ' Brainy ',
            ' Bright ', ' Breathtaking ', ' Blazing ', ' Bubbly ', ' Brazen ', ' Brave ', ' Broad-minded ', ' Calm ',
            ' Caring ', ' Cool ', ' Cheerful ', ' Charming ', ' Confident ', ' Cute ', ' Considerate ', ' Creative ',
            ' Compassionate ', ' Courteous ', ' Clever ', ' Credible ', ' Dear ', ' Daring ', ' Divine ', ' Dauntless ',
            ' Delightful ', ' Dazzling ', ' Dedicated ', ' Delectable ', ' Deserving ', ' Determined ', ' Diligent ',
            ' Dynamic ', ' Enthusiastic ', ' Energetic ', ' Enchanting ', ' Encouraging ', ' Enthralling ',
            ' Elegant  ', ' Excellent ', ' Effective ', ' Extraordinary ', ' Elegant ', ' Exceptional ', ' Emotional ',
            ' Fascinating ', ' Forgiving ', ' Fantastic ', ' Funny ', ' Favorable ', ' Friendly ', ' Fearless ',
            ' Frank ', ' Gorgeous ', ' Gifted ', ' Genius ', ' Glorious ', ' Glowing ', ' Gracious ', ' Great ', ' Grand ',
            ' Genuine ', ' Generous ', ' Gregarious ', ' Happy ', ' Honest ', ' Helpful ', ' Heavenly ', ' Hilarious ',
            ' Humorous ', ' Hearty ', ' Incredible ', ' Inspirational ', ' Inspiring ', ' Impeccable ', ' Ingenious ',
            ' Impressive ', ' Innovative ', ' Insightful ', ' Incandescent ', ' Intense ', ' Intrepid ', ' Impartial ',
            ' Imaginative ', ' Independent ', ' Intuitive ', ' Inventive ', ' Intellectual ', ' Intelligent ',
            ' Jolly ', ' Joyful ', ' Jubilant ', ' Jovial ', ' Joyous ', ' Kindhearted ', ' Knowledgeable ', ' Lively ',
            ' Lovable ', ' Lovely ', ' Luscious ', ' Loyal ', ' Marvelous ', ' Majestic ', ' Motivating ', ' Moral ',
            ' Modest ', ' Magnanimous ', ' Nubile ', ' Natural ', ' Noble ', ' Outstanding ', ' Obliging ',
            ' Optimistic ', ' Open-minded ', ' Positive ', ' Passionate ', ' Patient ', ' Perfect ', ' Progressive ',
            ' Productive ', ' Placid ', ' Phenomenal ', ' Potent ', ' Plucky ', ' Persuasive ', ' Polite ',
            ' Practical ', ' Peppy ', ' Quiet ', ' Ravishing ', ' Radiant ', ' Rightful ', ' Resolute ',
            ' Responsible ', ' Reliable ', ' Reserved ', ' Romantic ', ' Sweet ', ' Strong ', ' Stunning ',
            ' Spirited ', ' Sincere ', ' Special ', ' Smart ', ' Sensible ', ' Sensitive ', ' Sympathetic ',
            ' Sensuous ', ' Thrilling ', ' Tenacious ', ' Talented ', ' Trustworthy ', ' Thoughtful ', ' Unselfish ',
            ' Upbeat ', ' Uplifting ', ' Upstanding ', ' Vivacious ', ' Vigorous ', ' Valiant ', ' Understandable ',
            ' Versatile ', ' Witty ', ' Wise ', ' Wild ', ' Worthy ', ' Wonderful ', ' Welcoming ', ' Warmhearted ',
            ' Willing ', ' Youthful ', ' Zesty ', ' Best ', ' Besty ', ' Bestie ', ' Bestfriend ', ' Deary ', ' Icy ',
            ' Shy ', ' Spicy ', ' Hotty ', ' Hottest ', ' Chick ']

two_adj = [' Smart ', ' Peppy ', ' Quiet ', ' Great ', ' Happy ', ' Jolly ', ' Loyal ', ' Noble ', ' Sweet ', ' Brave ',
           ' Funny ', ' Deary ', ' Spicy ', ' Chick ', ' Grand ']
one_adj = [' Wise ', ' Wild ', ' Hot ', ' Kind ', ' Sexy ', ' Bold ', ' Calm ', ' Cool ', ' Cute ', ' Dear ', ' Icy ',
           ' Shy ', ' Best']
big_adj = [' Adventurous ', ' Broad-minded ', ' Breathtaking ', ' Trustworthy ', ' Open-Minded ', ' Understandable ',
           ' Responsible ', ' Sympathetic ', ' Outstanding ', ' Magnanimous ', ' Compassionate ', ' Enthusiastic ',
           ' Affectionate ', ' Extraordinary ']


# -----------------------------------------------
# Set the name here
# -----------------------------------------------
name = 'A'
global alpha

alphanumerals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z',
                 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# Color Mode
def clr():
    win.colormode(255)
    r = random.randrange(20, 255)           # The characters will be shown on Black background, so omitting the dark colors
    g = random.randrange(20, 255)           # for maximum visibility of the character. If background is chosen white, then
    b = random.randrange(20, 255)           # this can be reversed.
    return r, g, b


# Fonts based on your machine
def fonts():
    fonts = ['Beautiful Lovers Personal Use', 'FORTE', 'Signatra DEMO', 'Pristina', 'French Script MT', 'Gabriola',
             'Rage Italic', 'Mistral', 'Vivaldi', 'Harlow Solid Italic', 'Yellow Rabbit - Personal Use',
             'Margetha', 'Monotype Corsiva', 'Old English Text MT', 'Viner Hand ITC', 'Ink Free']
    return random.choice(fonts)


def gword():
    return random.choice(girl_adj)


# Words with 3-4 letters
def w1():
    return random.choice(one_adj)


# Words with 5-6 letters
def w2():
    return random.choice(two_adj)


# Biggest words
def bw():
    return random.choice(big_adj)


# Setting up screen
win = turtle.Screen()
win.title("Name")
win.bgcolor('black')        # Can be changed to any color
win.setup(width=1300, height=700)
win.tracer(1)               # Screen updates: 0: Off, 1: On

t = turtle.Turtle()         # Initializing the Turtle module
t.speed(0)                  # 0: Fastest, 5: Medium, 1: Slowest
t.hideturtle()
t.penup()


# -----------------------------------------------
# Initializing Backbone
# -----------------------------------------------
t.backward(150)             # Setting the character at center of the screen
t.left(90)
t.forward(250)


# Filling words in full line
def fullfill():
    t.right(90)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.forward(125)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.forward(125)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.backward(250)
    t.left(90)


# Only First word
def first():
    t.right(90)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.left(90)


# Only Middle/Central word
def mid():
    t.right(90)
    t.forward(125)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.backward(125)
    t.left(90)


# Only Last word
def last():
    t.right(90)
    t.forward(250)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.backward(250)
    t.left(90)


def firstlast():
    t.right(90)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.forward(250)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.backward(250)
    t.left(90)


def firstmid():
    t.right(90)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.forward(125)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.backward(125)
    t.left(90)


def midlast():
    t.right(90)
    t.forward(125)
    t.color(clr())
    t.write(random.choice([' Compassionate ', ' Extraordinary ', ' Fantabulous ', ' Jaw-Dropping ']), align="center",
            font=(fonts(), 25))
    t.forward(125)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.backward(250)
    t.left(90)


def firstspacemid():
    t.right(90)
    t.color(clr())
    t.backward(30)
    t.write(" Calm ", align="center", font=(fonts(), 25))
    t.forward(155)
    t.color(clr())
    t.write(" Attractive ", align="center", font=(fonts(), 25))
    t.backward(125)
    t.left(90)


# The topmost tipping point of A and bottom-most tipping point of V
# Here 0 represents blank spaces
def avxy010():
    t.right(90)
    t.forward(138)
    t.color(clr())
    t.write(random.choice([' Dear ', ' Calm ', ' Cool ', ' Bold ', ' Wise ', ' Wild ']), align="center",
            font=(fonts(), 25))
    t.backward(138)
    t.left(90)


def avxy030():
    t.right(90)
    t.forward(130)
    t.color(clr())
    t.write(' Majestic ', align="center", font=(fonts(), 25))
    t.backward(130)
    t.left(90)


def avxy050():
    t.right(90)
    t.forward(130)
    t.color(clr())
    t.write(random.choice([' Knowledgeable ', ' Broad-minded ', ' Understandable ', ' Inspirational ']), align="center",
            font=(fonts(), 25))
    t.backward(130)
    t.left(90)


def avxy03030():
    t.right(90)
    t.forward(45)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.forward(160)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.backward(205)
    t.left(90)


def g3022():
    t.right(90)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.forward(150)
    t.color(clr())
    t.write(" Coolest ", align="center", font=(fonts(), 25))
    t.forward(100)
    t.color(clr())
    t.write(" Awesome ", align="center", font=(fonts(), 25))
    t.backward(250)
    t.left(90)


def g0320():
    t.right(90)
    t.forward(125)
    t.color(clr())
    t.write(random.choice([' Compassionate ', ' Extraordinary ', ' Fantabulous ', ' Jaw-Dropping ']), align="center",
            font=(fonts(), 25))
    t.forward(105)
    t.color(clr())
    t.write(random.choice([' Cool ', ' Cute ', ' Best ', ' Wild ', ' Dear ', ' Wise ', ' Bold ']), align="center",
            font=(fonts(), 25))
    t.backward(230)
    t.left(90)


def j2by5():
    t.right(90)
    t.forward(70)
    t.color(clr())
    t.write(" Awestruck ", align="center", font=(fonts(), 25))
    t.backward(70)
    t.left(90)


def kr30300():
    t.right(90)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.forward(160)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.backward(160)
    t.left(90)


def kr30030():
    t.right(90)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.forward(190)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.backward(190)
    t.left(90)


def k50():
    t.right(90)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.forward(120)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.backward(120)
    t.left(90)


def k40():
    t.right(90)
    t.forward(50)
    t.color(clr())
    t.write(random.choice([' Very Gorgeous ', ' Surprisingly Wild ', ' Extremely Hot ', ' Most Handsome ',
                           ' Most Beautiful ', ' Insane Killer ']), align="center", font=(fonts(), 25))
    t.backward(50)
    t.left(90)


def kfirst():
    t.right(90)
    t.color(clr())
    t.write(random.choice([' Jolly ', ' Beauty ', ' Besty ', ' Hotty ', ' Smart ', ' Sweet ', ' Strong ', ' Joyous ',
                           ' Joyful ']), align="center", font=(fonts(), 25))
    t.left(90)


def m404():
    t.right(90)
    t.color(clr())
    t.write(bw(), align="center", font=(fonts(), 25))
    t.forward(230)
    t.color(clr())
    t.write(bw(), align="center", font=(fonts(), 25))
    t.backward(230)
    t.left(90)


def m20402():
    t.right(90)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.forward(100)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.forward(100)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.backward(200)
    t.left(90)


def m30103():
    t.right(90)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.forward(150)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.forward(50)
    t.color(clr())
    t.write(gword(), align="center", font=(fonts(), 25))
    t.backward(200)
    t.left(90)


def nfl():
    t.right(90)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.forward(250)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.backward(250)
    t.left(90)


def n21000000002():
    t.right(90)
    t.color(clr())
    t.write(w1(), align="center", font=(fonts(), 25))
    t.forward(50)
    t.color(clr())
    t.write(w1(), align="center", font=(fonts(), 25))
    t.forward(200)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.backward(250)
    t.left(90)


def n20100000002():
    t.right(90)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.forward(71)
    t.color(clr())
    t.write(w1(), align="center", font=(fonts(), 25))
    t.forward(179)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.backward(250)
    t.left(90)


def n20010000002():
    t.right(90)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.forward(89)
    t.color(clr())
    t.write(w1(), align="center", font=(fonts(), 25))
    t.forward(161)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.backward(250)
    t.left(90)


def n20001000002():
    t.right(90)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.forward(107)
    t.color(clr())
    t.write(w1(), align="center", font=(fonts(), 25))
    t.forward(143)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.backward(250)
    t.left(90)


def n20000100002():
    t.right(90)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.forward(125)
    t.color(clr())
    t.write(w1(), align="center", font=(fonts(), 25))
    t.forward(125)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.backward(250)
    t.left(90)


def n20000010002():
    t.right(90)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.forward(143)
    t.color(clr())
    t.write(w1(), align="center", font=(fonts(), 25))
    t.forward(107)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.backward(250)
    t.left(90)


def n20000001002():
    t.right(90)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.forward(161)
    t.color(clr())
    t.write(w1(), align="center", font=(fonts(), 25))
    t.forward(89)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.backward(250)
    t.left(90)


def n20000000102():
    t.right(90)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.forward(179)
    t.color(clr())
    t.write(w1(), align="center", font=(fonts(), 25))
    t.forward(71)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.backward(250)
    t.left(90)


def n20000000012():
    t.right(90)
    t.color(clr())
    t.write(w2(), align="center", font=(fonts(), 25))
    t.forward(200)
    t.color(clr())
    t.write(w1(), align="center", font=(fonts(), 25))
    t.forward(50)
    t.color(clr())
    t.write(w1(), align="center", font=(fonts(), 25))
    t.backward(250)
    t.left(90)


def z0001():
    t.right(90)
    t.forward(205)
    t.color(clr())
    t.write(w1(), align="center", font=(fonts(), 25))
    t.backward(205)
    t.left(90)


def z0010():
    t.right(90)
    t.forward(165)
    t.color(clr())
    t.write(w1(), align="center", font=(fonts(), 25))
    t.backward(165)
    t.left(90)


def z0100():
    t.right(90)
    t.forward(85)
    t.color(clr())
    t.write(w1(), align="center", font=(fonts(), 25))
    t.backward(85)
    t.left(90)


def z1000():
    t.right(90)
    t.forward(45)
    t.color(clr())
    t.write(w1(), align="center", font=(fonts(), 25))
    t.backward(45)
    t.left(90)


def nextline():
    t.backward(40)


def space():
    t.right(90)
    t.forward(400)  # Actual space between characters
    t.left(90)
    t.forward(480)  # nextline(backward) * 12


# -----------------------------------------------
# Alphabet Code
# -----------------------------------------------
# Alphabets M, W and Q are NOT completed since I was tired writing this whole program.

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


def B():
    firstmid()
    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    fullfill()

    nextline()
    firstmid()
    nextline()
    fullfill()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    firstmid()

    space()


def C():
    midlast()

    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    firstlast()
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
    firstlast()

    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    midlast()

    space()


def D():
    firstmid()

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
    firstlast()
    nextline()
    firstlast()

    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    firstmid()

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
    nextline()
    first()

    space()


def G():
    g0320()

    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    firstlast()
    nextline()
    firstlast()

    nextline()
    first()
    nextline()
    first()
    nextline()
    g3022()

    nextline()
    firstlast()
    nextline()
    firstlast()

    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    g0320()

    space()


def H():
    i = 1
    while i <= 5:
        firstlast()
        nextline()
        i += 1

    i = 1
    while i <= 3:
        fullfill()
        nextline()
        i += 1

    i = 1
    while i <= 5:
        firstlast()
        nextline()
        i += 1

    space()


def I():
    i = 1
    while i <= 3:
        fullfill()
        nextline()
        i += 1

    i = 1
    while i <= 7:
        mid()
        nextline()
        i += 1

    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    space()


def J():
    i = 1
    while i <= 3:
        fullfill()
        nextline()
        i += 1

    i = 1
    while i <= 7:
        mid()
        nextline()
        i += 1

    firstspacemid()
    nextline()
    firstmid()
    nextline()
    j2by5()

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
    k50()
    nextline()

    k40()
    nextline()
    kfirst()
    nextline()
    k40()
    nextline()

    k50()
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
    i = 1
    while i <= 10:
        first()
        nextline()
        i += 1

    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    space()


def M():
    pass


def N():
    nfl()

    nextline()
    n21000000002()
    nextline()
    n20100000002()
    nextline()
    n20010000002()
    nextline()
    n20001000002()

    nextline()
    n20000100002()

    nextline()
    n20000010002()
    nextline()
    n20000001002()
    nextline()
    n20000000102()
    nextline()
    n20000000012()

    nextline()
    nfl()

    space()


def O():
    avxy050()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    m404()

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
    m404()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    avxy050()

    space()


def P():
    firstmid()
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
    fullfill()
    nextline()
    fullfill()
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


def Q():
    pass


def R():
    firstmid()
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
    fullfill()
    nextline()
    fullfill()
    nextline()
    firstmid()

    nextline()
    firstmid()
    nextline()
    kr30300()
    nextline()
    kr30030()
    nextline()
    firstlast()

    space()


def S():
    fullfill()
    nextline()
    fullfill()
    nextline()
    firstmid()

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

    nextline()
    last()
    nextline()
    last()

    nextline()
    midlast()
    nextline()
    fullfill()
    nextline()
    fullfill()

    space()


def T():
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    i = 1
    while i <= 10:
        nextline()
        mid()
        i += 1

    space()


def U():
    firstlast()

    i = 1
    while i <= 9:
        nextline()
        firstlast()
        i += 1

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    avxy03030()

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
    firstlast()

    nextline()
    avxy03030()
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
    pass


def X():
    firstlast()
    nextline()
    firstlast()
    nextline()

    avxy03030()
    nextline()
    avxy03030()
    nextline()
    avxy050()
    nextline()
    avxy030()

    nextline()
    avxy010()

    nextline()
    avxy030()
    nextline()
    avxy050()
    nextline()
    avxy03030()
    nextline()
    avxy03030()

    nextline()
    firstlast()
    nextline()
    firstlast()

    space()


def Y():
    firstlast()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()

    avxy03030()
    nextline()
    avxy03030()
    nextline()
    avxy050()
    nextline()
    avxy030()

    nextline()
    avxy010()

    nextline()
    avxy010()
    nextline()
    avxy010()
    nextline()
    avxy010()
    nextline()
    avxy010()
    nextline()
    avxy010()

    space()


def Z():
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    last()
    nextline()
    z0001()
    nextline()
    z0010()
    nextline()
    mid()
    nextline()
    z0100()
    nextline()
    z1000()
    nextline()
    first()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    space()


def zero():
    avxy050()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    m404()

    nextline()
    firstlast()
    nextline()
    firstlast()

    nextline()
    fullfill()

    nextline()
    firstlast()
    nextline()
    firstlast()

    nextline()
    m404()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    avxy050()

    space()


def one():
    mid()
    nextline()
    mid()
    nextline()
    firstmid()

    i = 1
    while i <= 7:
        nextline()
        mid()
        i += 1

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    space()


def two():
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    firstlast()
    nextline()
    z0001()
    nextline()
    z0010()
    nextline()
    mid()
    nextline()
    z0100()
    nextline()
    z1000()
    nextline()
    first()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    space()


def three():
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    firstlast()
    nextline()
    z0001()
    nextline()
    z0010()

    nextline()
    mid()

    nextline()
    z0010()
    nextline()
    z0001()
    nextline()
    firstlast()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    space()


def four():
    last()
    nextline()
    z0001()
    nextline()
    z0010()
    nextline()
    mid()
    nextline()
    z0100()
    nextline()
    z1000()
    nextline()
    firstlast()

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
    firstlast()
    nextline()
    first()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    last()
    nextline()
    firstlast()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    space()


def six():
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    firstlast()
    nextline()
    first()

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
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    space()


def seven():
    fullfill()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    firstlast()

    nextline()
    last()
    nextline()
    z0001()
    nextline()
    z0010()

    nextline()
    mid()
    nextline()
    mid()
    nextline()
    mid()

    nextline()
    z0100()
    nextline()
    z1000()
    nextline()
    first()

    space()


def eight():
    avxy03030()
    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    fullfill()

    nextline()
    mid()

    nextline()
    fullfill()
    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    avxy03030()

    space()


def nine():
    avxy03030()
    nextline()
    fullfill()
    nextline()
    fullfill()

    nextline()
    firstlast()
    nextline()
    firstlast()
    nextline()
    midlast()

    nextline()
    last()
    nextline()
    last()
    nextline()
    last()
    nextline()
    firstlast()

    nextline()
    fullfill()
    nextline()
    fullfill()
    nextline()
    avxy03030()

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
            elif alpha == '0':
                zero()
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


# Displays each character of the 'name'
for i in range(len(name)):
    alpha = name[i]
    AlphaIterator()

# Main Loop
while True:
    win.update()
