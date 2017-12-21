"""
Hiire algoritm

1 OSA : Suvalise labürindi genereerimine
2 OSA : Labürindi turtlesse lugemine
3 OSA : Hiire algoritm
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
 
        koordinaadid = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(koordinaadid)
        for (xx, yy) in koordinaadid: # valib välja kuhu sein teha
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
aken.title("Labyrindi lahendamine - hiire algoritm")
aken.setup(700, 700)
aken.register_shape("puu.gif", shape = None)

class Labürint(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("puu.gif")
        self.color("black")
        self.penup()
        self.speed(10)
        self.setposition(300, -300)
      
levels = [""]
levels.append(level_1)

turtle.bgpic("joulud.gif")
hiir = turtle.Turtle()
hiir.color('#0C4E15')
hiir.shape("turtle")
hiir.penup()
hiir.speed(500)
hiir.setheading(270)

def koostamine(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            karakter = level[y][x]
            
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
            
            if karakter == "#":
                lab.goto(screen_x, screen_y)
                lab.shape("puu.gif")
                lab.stamp()
                seinad.append((screen_x, screen_y))
            if karakter == "P":
                hiir.goto(screen_x, screen_y)
            if karakter == ".":
                lopp = True
lab = Labürint()
seinad = [(-264,288)]
koostamine(levels[1])

aeg = Turtle(visible=False)  #Aja kuvamine (sekundites)
aeg.color("#0C4E15")
aeg.penup()
aeg.setposition(-288, 305) 
aeg.write("Aeg(s): " + str(0), font = ("Arial",16))

vahemaa = Turtle(visible=False) #Läbitud vahemaa kuvamine (pikslites)
vahemaa.color("#0C4E15")
vahemaa.penup()
vahemaa.setposition(-130, 305)  
vahemaa.write("Tee pikkus(px): " + str(0), font = ("Arial",16))

# 3. osa labürindi lahendamine -hiire algoritm
def uus_suund():
    suunad = {1:90, 2:0, 3:180, 4:270} #1=N=üles, 2=E=paremale,3=W=vasakule, 4=S=alla
    uus_suund = suunad[randint(1,4)]
    return uus_suund

def järgmise_sammu_koordinaadid(järgmine_samm):
    if järgmine_samm == 0: #paremale
        liigu_x = round(hiir.xcor())+24
        liigu_y = round(hiir.ycor())    
    if järgmine_samm == 90: #üles
        liigu_x = round(hiir.xcor())
        liigu_y = round(hiir.ycor()-24)        
    if järgmine_samm == 180: #vasakule
        liigu_x = round(hiir.xcor()-24)
        liigu_y = round(hiir.ycor())   
    if järgmine_samm == 270: #alla
        liigu_x = round(hiir.xcor())
        liigu_y = round(hiir.ycor())+24
    return (liigu_x, liigu_y)

labitud_vahemaa = 0
kulunud_aeg = 0

hiir.pen(pencolor = "#E86B6B", pensize = 22)
hiir.pendown()
hiir.forward(24)

while True:
    vahemaa.undo()
    vahemaa.write("Tee pikkus(px): " + str(labitud_vahemaa), font = ("Arial",16))
    kulunud_aeg = round(time.perf_counter(), 2)
    aeg.undo()
    aeg.write("Aeg(s): " + str(kulunud_aeg), font = ("Arial",16))
    järgmine_samm = uus_suund()
    hiir.setheading(järgmine_samm)
    koordinaadid = järgmise_sammu_koordinaadid(järgmine_samm)
    if (koordinaadid) not in seinad:   
        hiir.goto(koordinaadid)
        labitud_vahemaa += 24
    if (koordinaadid) == (264, -168):
        hiir.goto(koordinaadid)
        hiir.goto(264,-192)
        hiir.setheading(270)
        labitud_vahemaa += 48
        vahemaa.undo()
        vahemaa.write("Tee pikkus(px): " + str(labitud_vahemaa), font = ("Arial",16))
        kulunud_aeg = round(time.perf_counter(), 2)
        aeg.undo()
        aeg.write("Aeg(s): " + str(kulunud_aeg), font = ("Arial",16))
        break

exitonclick()