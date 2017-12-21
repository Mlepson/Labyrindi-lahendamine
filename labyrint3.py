"""
Kasutaja proov

1 OSA : Suvalise labürindi genereerimine
2 OSA : Labürindi turtlesse lugemine
3 OSA : Kasutaja käikude kontroll
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
labitud_vahemaa = 0
aken = turtle.Screen()
aken.bgcolor("white")
aken.title("Labyrindi lahendamine - Kasutaja katse")
aken.setup(700, 700)
aken.register_shape("lumememm.gif", shape = None)
aken.register_shape("mouse_parem.gif", shape = None)
aken.register_shape("mouse_vasak.gif", shape = None)
turtle.bgpic("sarav.gif")


#3 OSA- Mängija kontrollimine
class Labürint(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("lumememm.gif")
        self.color("black")
        self.penup()
        self.speed(50)

class Kasutaja(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("mouse_parem.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.setheading(270)
    def go_up(self):
        global labitud_vahemaa
        x = self.xcor()
        y = self.ycor()+24
        if (x,y) not in seinad:   
            self.goto(x,y)
            labitud_vahemaa +=24
    def go_down(self):
        global labitud_vahemaa
        x = self.xcor()
        y = self.ycor()-24
        if (x,y) not in seinad:   
            self.goto(x,y)
            labitud_vahemaa +=24
    def go_left(self):
        global labitud_vahemaa
        x = self.xcor()-24
        y = self.ycor()
        self.shape("mouse_vasak.gif")
        if (x,y) not in seinad:   
            self.goto(x,y)
            labitud_vahemaa +=24
    def go_right(self):
        global labitud_vahemaa
        x = self.xcor()+24
        y = self.ycor()
        self.shape("mouse_parem.gif")
        if (x,y) not in seinad:   
            self.goto(x,y)
            labitud_vahemaa +=24
        
kasutaja = Kasutaja()
levels = [""]
levels.append(level_1)

def koostamine(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            karakter = level[y][x]
            
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            if karakter == "#":
                lab.goto(screen_x, screen_y)
                lab.stamp()
                seinad.append((screen_x, screen_y))
            if karakter == "P":
                kasutaja.goto(screen_x, screen_y)
            if karakter == ".":
                lopp = True
lab = Labürint()
seinad = [(-264,288)]
koostamine(levels[1])

aeg = Turtle(visible=False)
aeg.color("black")
aeg.penup()
aeg.setposition(-288, 305)  
aeg.write("Aeg(s): " + str(0), font=("Arial", 16))

vahemaa = Turtle(visible=False)
vahemaa.color("black")
vahemaa.penup()
vahemaa.setposition(-130, 305) 
vahemaa.write("Tee pikkus(px): " + str(0), font=("Arial", 16))

 # 3. osa labürindi lahendamine - parem käsi vastu seina algoritm
turtle.listen()
turtle.onkey(kasutaja.go_left, "Left")
turtle.onkey(kasutaja.go_right, "Right")
turtle.onkey(kasutaja.go_up, "Up")
turtle.onkey(kasutaja.go_down, "Down")

aken.tracer(0)

while True:
    vahemaa.undo()
    vahemaa.write("Tee pikkus(px): " + str(labitud_vahemaa), font=("Arial", 16))
    kulunud_aeg = round(time.perf_counter(),2)
    aeg.undo()
    aeg.write("Aeg(s): " + str(kulunud_aeg), font=("Arial", 16))
    aken.update()
    if round(kasutaja.xcor()) == 264  and round(kasutaja.ycor()) == -192:
        vahemaa.undo()
        vahemaa.write("Tee pikkus(px): " + str(labitud_vahemaa), font=("Arial", 16))
        kulunud_aeg = round(time.perf_counter(),2)
        aeg.undo()
        aeg.write("Aeg(s): " + str(kulunud_aeg), font=("Arial", 16))
        break
exitonclick()