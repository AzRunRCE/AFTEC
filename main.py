#!/usr/bin/env python
# coding: utf-8
from tkinter import *

fen = Tk() # Création de la fenêtre
fen.title("HOUR GENERATOR 2000") # Affichage du titre
fen.geometry('300x210') # Déf des dimensions de la fenêtre (400x250)

TextID = Label(fen, text="IDENTIFIANT")
TextID.pack()

saisieID=StringVar()
entreeID=Entry(fen,textvariable=saisieID, width=30)
entreeID.pack(padx=10,pady=10)

TextPWD = Label(fen, text="MOT DE PASSE")
TextPWD.pack()

saisiePWD=StringVar()
entreePWD=Entry(fen,textvariable=saisiePWD, width=30)
entreePWD.pack(padx=10,pady=10)

TextHOURS = Label(fen, text="NOMBRE D'HEURES A GENERER")
TextHOURS.pack()

s = Spinbox(fen, from_=1, to=4)
s.pack(padx=10, pady=10)

def main():
	print ("button ok")

bou=Button(fen , text='Générer' , command=main)
bou.pack()

fen.mainloop()