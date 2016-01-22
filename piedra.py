#!/urs/bin/env python
# -*-coding:utf-8-*-
import time
from time import sleep
import random
import Tkinter, tkSimpleDialog
import Tkinter, tkMessageBox

root = Tkinter.Tk()
root.withdraw()

depo = ["piedra","papel","tijera","lagarto","spock"]
while True:
	x = tkSimpleDialog.askstring("Platzi", "Que elijes? piedra, papel, tijera, lagarto, spock: ")
	if x not in depo:
		break
		print("No hagas Trampa!!!")
		continue
	pc = random.choice(depo)
	sleep(0.5)
	tkMessageBox.showinfo("Platzi",("Computadora elijio {}.").format(pc))
	if x == pc:
		tkMessageBox.showinfo("Platzi", ("Empate.").format(sus))
#opciones
	elif x == "papel" and pc == "tijera":
		sleep(0.5)
		tkMessageBox.showinfo("Platzi", ("Perdiste. {} Cortan {}").format(pc,x))	
	elif x == "piedra" and pc == "papel":
		sleep(0.5)
		tkMessageBox.showinfo("Platzi", ("Perdiste. {} Tapa {}").format(pc,x))
	elif x == "lagarto" and pc == "piedra":
		sleep(0.5)
		tkMessageBox.showinfo("Platzi", ("Perdiste. {} Aplasta {}").format(pc,x))
	elif x == "spock" and pc == "lagarto":
		sleep(0.5)
		tkMessageBox.showinfo("Platzi", ("Perdiste. {} Envenena {}").format(pc,x))
	elif x == "tijera" and pc == "spock":
		sleep(0.5)
		tkMessageBox.showinfo("Platzi", ("Perdiste. {} Rompe {}").format(pc,x))
	elif x == "lagarto" and pc == "tijera":
		sleep(0.5)
		tkMessageBox.showinfo("Platzi", ("Perdiste. {} Decapitan {}").format(pc,x))
	elif x == "papel" and pc == "lagarto":
		sleep(0.5)	
		tkMessageBox.showinfo("Platzi", ("Perdiste. {} Devora {}").format(pc,x))
	elif x == "spock" and pc == "papel":
		sleep(0.5)
		tkMessageBox.showinfo("Platzi", ("Perdiste. {} Desautoriza {}").format(pc,x))
	elif x == "piedra" and pc == "spock":
		sleep(0.5)
		tkMessageBox.showinfo("Platzi", ("Perdiste. {} Vaporiza {}").format(pc,x))
	elif x == "tijera" and pc == "piedra":
		sleep(0.5)
		tkMessageBox.showinfo("Platzi", ("Perdiste. {} Aplasta {}").format(pc,x))
	else:
		sleep(0.5)
		tkMessageBox.showinfo("Platzi",("Ganaste. {} Gana {}").format(pc,x))
input()
