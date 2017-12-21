"""
Seinajärgija algoritm

1 OSA : Suvalise labürindi genereerimine
2 OSA : Labürindi turtlesse lugemine
3 OSA : Seinajärgija algoritm
"""

#impordime vajalikud vahendid
from random import shuffle
from random import randrange
from turtle import *
import turtle
from random import randint
import time

#1 OSA labyrindi koostamine
def labyrindi_koostamine(laius, kõrgus):
    lopp_tulemus = []
    vertikaalne = []
    horisontaalne = []
    for element in range(kõrgus):
        lopp_tulemus.append([0] * laius + [1])
    lopp_tulemus += [[1] * (laius + 1)]
    
    for element2 in range(kõrgus):
        vertikaalne.append(["#  "] * laius + ['#']) 
    vertikaalne += [[]]
    
    for element3 in range(kõrgus + 1):
        horisontaalne.append(["###"] * laius + ['#'])
 
    def seinad(x, y): # hakkame seinu paika seadma
        lopp_tulemus[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d: # valib välja kuhu sein teha
            if lopp_tulemus[yy][xx]: #Kui on 0 siis jätkab järgmiste if-idega, kui on sein siis võtab uued argumendid
                continue
            if xx == x:
                horisontaalne[max(y, yy)][x] = "#  " # paneb kordinaatidele seina
            if yy == y:
                vertikaalne[y][max(x, xx)] = "   " #jätab tühimiku
                
            seinad(xx, yy)
        
    seinad(randrange(laius), randrange(kõrgus)) #randrange() tagastab suvaliselt valitud elemendi antud osast
 
    s = ""
    for (a, b) in zip(horisontaalne, vertikaalne):  #zip võtab mõlemast listist elemente järjest ( Algul võtab mõlemast listist esimese elemendi, hiljem mõlemast teise jne)
        s += ''.join(a + ['\n'] + b + ['\n']) #join abil ja reavahetuse märgi abil paneme listi elemendid üksteise alla järjest 
    return s # tagastame saadud labyrindi
 
if __name__ == '__main__': # põhi klass millega labyrindi joonistame
    labyrint = labyrindi_koostamine(8, 10)
    
fail = open("lab.txt", "w") # loome uue faili
fail.write(labyrint)
fail.close()
fail = open("lab.txt", encoding = "UTF-8")
level_1 = []
for rida in fail:
    level_1.append(rida.strip("\n"))
fail.close # labyrint on listi loetud

level_1[0] = '#P#######################'
level_1[20] = '####################### #'
# 2 OSA
#Loeme nüüd labyrindi turtlesse
aken = turtle.Screen()
aken.bgcolor("white")
aken.title("Labyrindi lahendamine - Seinajärgija algoritm")
aken.setup(700, 700)
aken.register_shape("kuul.gif", shape = None)

class Labürint(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("kuul.gif")
        self.color("black")
        self.penup()
        self.speed(50)
        self.setposition(300, -300)
      
levels = [""]
levels.append(level_1)

turtle.bgpic("taust.gif")
käsi = turtle.Turtle()
käsi.color("#C1E4FC")
käsi.shape("turtle")
käsi.penup()
käsi.speed(10)
käsi.setheading(270)

def koostamine(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            karakter = level[y][x]
            
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            if karakter == "#":
                lab.goto(screen_x, screen_y)
                lab.shape("kuul.gif")
                lab.stamp()
                seinad.append((screen_x, screen_y))
            if karakter == "P":
                käsi.goto(screen_x, screen_y)
            if karakter == ".":
                lopp = True
lab = Labürint()
seinad = [(-264,288), (264,-192)]

koostamine(levels[1])

aeg = Turtle(visible=False) #Aja kuvamine
aeg.color("#C1E4FC")
aeg.penup()
aeg.setposition(-288, 305)  
aeg.write("Aeg(s): " + str(0), font=("Ariel", 16))

vahemaa = Turtle(visible=False)  # Vahemaa kuvamine
vahemaa.color("#C1E4FC")
vahemaa.penup()
vahemaa.setposition(-130, 305)  
vahemaa.write("Tee pikkus(px): " + str(0), font=("Ariel", 16))


# 3. osa labürindi lahendamine - Seinajärgija algoritm
labitud_vahemaa = 0
kulunud_aeg = 0

def p_diagonaal(x, y, suund):
    if suund == 270:
        return (x-24,y-24)
    if suund == 90:
        return (x+24, y+24)
    if suund == 0:
        return (x+24,y-24)
    if suund == 180:
        return (x-24, y+24)

def ees(x, y, suund):
    if suund == 270:
        return (x,y-24)
    if suund == 90:
        return (x, y+24) 
    if suund == 0:
        return (x+24, y) 
    if suund == 180:
        return (x-24, y)
    
def tipp(x, y, suund, seinad):
    global labitud_vahemaa
    if suund == 0:
        if (x, y-24) in seinad and (x+24, y) not in seinad and (x+24, y-24) not in seinad and (x+24, y-48) not in seinad and (x, y-48) not in seinad:
            käsi.forward(24)
            käsi.right(90)
            käsi.forward(48)
            käsi.right(90)
            käsi.forward(24)
            labitud_vahemaa += 96
    if suund == 90:
        if (x+24, y) in seinad and (x, y+24) not in seinad and (x+24, y+24) not in seinad and (x+48, y+24) not in seinad and (x+48, y) not in seinad:
            käsi.forward(24)
            käsi.right(90)
            käsi.forward(48)
            käsi.right(90)
            käsi.forward(24)
            labitud_vahemaa += 96
    if suund == 180:
        if (x, y+24) in seinad and (x-24, y) not in seinad and (x-24, y+24) not in seinad and (x-24, y+48) not in seinad and (x, y+48) not in seinad:
            käsi.forward(24)
            käsi.right(90)
            käsi.forward(48)
            käsi.right(90)
            käsi.forward(24)
            labitud_vahemaa += 96
    if suund == 270:
         if (x-24, y) in seinad and (x, y-24) not in seinad and (x-24, y-24) not in seinad and (x-48, y-24) not in seinad and (x-48, y) not in seinad:
            käsi.forward(24)
            käsi.right(90)
            käsi.forward(48)
            käsi.right(90)
            käsi.forward(24)
            labitud_vahemaa += 96
            
def sisenurk(x, y, suund, seinad):
    if suund == 0:
        if (x, y-24) in seinad and (x+24, y-24) in seinad and (x+24, y) in seinad:
            käsi.left(90)
    if suund == 90:
        if (x+24, y) in seinad and (x+24, y+24) in seinad and (x, y+24) in seinad:
            käsi.left(90)
    if suund == 180:
        if (x, y+24) in seinad and (x-24, y+24) in seinad and (x-24, y) in seinad:    
            käsi.left(90)
    if suund == 270:
        if (x-24, y) in seinad and (x-24, y-24) in seinad and (x, y-24) in seinad:
            käsi.left(90)

def välisnurk(x, y, suund, seinad):
    global labitud_vahemaa
    if suund == 0:
        if (x, y-24) in seinad and (x, y-48) in seinad and (x+24, y) not in seinad and (x+24, y-24) not in seinad and (x+24, y-48) not in seinad:
            käsi.forward(24)
            käsi.right(90)
            käsi.forward(48)
            labitud_vahemaa += 72
    if suund == 90:
        if (x+24, y) in seinad and (x+48,y) in seinad and (x, y+24) not in seinad and (x+24, y+24) not in seinad and (x+48, y+24) not in seinad:
            käsi.forward(24)
            käsi.right(90)
            käsi.forward(48)
            labitud_vahemaa += 72
    if suund == 180:
        if (x, y+24) in seinad and (x, y+48) in seinad and (x-24, y) not in seinad and (x-24, y+24) not in seinad and (x-24, y+48) not in seinad:
            käsi.forward(24)
            käsi.right(90)
            käsi.forward(48)
            labitud_vahemaa += 72
    if suund == 270:
         if (x-24, y) in seinad and (x-48, y) in seinad and (x, y-24) not in seinad and (x-24, y-24) not in seinad and (x-48, y-24) not in seinad:
            käsi.forward(24)
            käsi.right(90)
            käsi.forward(48)
            labitud_vahemaa += 72

käsi.pen(pencolor = "#C1E4FC", pensize = 23)
käsi.pendown() 
x = -264
y = 264
käsi.goto(x,y)
käsi.color('#06064D')
käsi.pen(pencolor = "#C1E4FC", pensize = 23)
while True:
    vahemaa.undo()
    vahemaa.write("Tee pikkus(px): " + str(labitud_vahemaa), font=("Ariel", 16))
    kulunud_aeg = round(time.perf_counter(), 2)
    aeg.undo()
    aeg.write("Aeg(s): " + str(kulunud_aeg), font=("Ariel", 16))
    if ees(round(käsi.xcor()), round(käsi.ycor()), round(käsi.heading())) == (264, -168):
        käsi.goto(ees(round(käsi.xcor()), round(käsi.ycor()), round(käsi.heading())))
        käsi.goto(264,-192)
        käsi.setheading(270)
        labitud_vahemaa += 48
        vahemaa.undo()
        vahemaa.write("Tee pikkus(px): " + str(labitud_vahemaa), font=("Ariel", 16))
        kulunud_aeg = round(time.perf_counter(), 2)
        aeg.undo()
        aeg.write("Aeg(s): " + str(kulunud_aeg), font=("Ariel", 16))
        break
    if p_diagonaal(round(käsi.xcor()), round(käsi.ycor()), round(käsi.heading())) in seinad and ees(round(käsi.xcor()), round(käsi.ycor()), round(käsi.heading())) not in seinad:
        käsi.goto(ees(round(käsi.xcor()), round(käsi.ycor()), round(käsi.heading())))
        labitud_vahemaa += 24
    else:
        tipp(round(käsi.xcor()), round(käsi.ycor()), round(käsi.heading()), seinad)
        sisenurk(round(käsi.xcor()), round(käsi.ycor()), round(käsi.heading()), seinad)
        välisnurk(round(käsi.xcor()), round(käsi.ycor()), round(käsi.heading()), seinad)

exitonclick()