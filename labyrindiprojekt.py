"""
Põhi programm
See programm kasutab tkinterit. Ja laseb kasutajal valida eelistatud algoritmi.
Samuti on võimalik saada informatsiooni mõlema algoritmi kohta siit samast.
"""

from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
import tkinter as tk
from subprocess import call

raam = Tk()
raam.title("Labürindi lahendamise programm")
raam.geometry("940x500")
raam.configure(background="#A6D4FD")
raam.option_add("*font", ('Century Gothic', 12))


def sulge_aken():
    raam.destroy()

silt = ttk.Label(raam, text="Vali alt endale meelepärane algoritm, millega tahad näha labürindi lahenduskäiku.")
silt.place(x=147, y=80)
nupp1 = Button(raam, text= "HIIRE ALGORITM",width=20, height=2, padx= 5, pady= 5, command = lambda: call(["python", "labyrint.py"]))
nupp1.place(x= 60, y = 300)

nupp2 = Button(raam, text= "SEINAJÄRGIJA ALGORITM",width=20, height=2, padx= 5, pady= 5, command = lambda: call(["python", "labyrint2.py"]))
nupp2.place(x= 350, y = 300)

nupp3 = Button(raam, text= "Sulge",width=5, height=1, padx= 2, pady= 2, command = sulge_aken)
nupp3.place(x= 860, y = 450)

nupp4 = Button(raam, text= "PROOVIN ISE!",width=20, height=2, padx= 5, pady= 5, command = lambda: call(["python", "labyrint3.py"]))
nupp4.place(x= 640, y = 300)

"""
esimese pildi ja pildi peale vajutamise koodid
"""
image = Image.open("hiir.png")
photo = ImageTk.PhotoImage(image)
#label1 = Label(raam, image=photo).place(x=75, y = 130)

def vajutus():
    global muutuja
    if not muutuja:
        siltt.place(x=120, y=30)
        muutuja = True
    else:
        siltt.place_forget()
        muutuja=False

nuppp = tk.Button(raam, image=photo, command = lambda: vajutus())
nuppp.place(x=75, y = 135)
siltt = tk.Label(raam, text="Hiire algoritm \n Üks lihtsamaid algoritme, mida saab väljapääsu leidmiseks kasutada.\n Põhimõte on liikuda otse seinani ja siis pöörata suvalisse suunda.\n Teisisõnu uidatakse keerdkäikudes kuni leitakse väljapääs.\n Selle algoritmi nõrkuseks on see, et sageli kulub palju aega labürindist välja pääsemiseks.")
muutuja = False

"""
teise pildi ja pildi peale vajutamise koodid
"""
image2 = Image.open("sein.png")
photo2 = ImageTk.PhotoImage(image2)

def vajutus2():
    global muutuja2
    if not muutuja2:
        siltt2.place(x=120, y=30)
        muutuja2 = True
    else:
        siltt2.place_forget()
        muutuja2=False

nuppp2 = tk.Button(raam, image=photo2, command = lambda: vajutus2())
nuppp2.place(x=366, y = 135)
siltt2 = tk.Label(raam, text="Seinajärgija algoritm \n Teine võimalus kuidas algoritmi läbida. Esmalt tuleb valida parem või vasak käsi ja \n hoida see käsi pidevas kontaktis labürindi seinaga väljapääsu leidmiseni. \n Meie oleme valinud antud juhul parema käe. \n Selline algoritm ei tööta, kui algus- ja lõpp-punkt pole omavahel seinapidi ühendatud. ")
muutuja2 = False
"""
kolmanda pildi ja pildi peale vajutamise koodid
"""
image3 = Image.open("ise.png")
photo3 = ImageTk.PhotoImage(image3)
Label(raam, image=photo3).place(x = 655, y = 140)


raam.mainloop()
