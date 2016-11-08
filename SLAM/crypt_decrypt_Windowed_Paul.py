#!/usr/bin/env python
# coding: utf-8
from tkinter import *

fen = Tk() # Création de la fenêtre
fen.title("Cryptage / Décryptage") # Affichage du titre
fen.geometry('400x200') # Déf des dimensions de la fenêtre (400x250)

l = LabelFrame(fen, text="Cryptage", padx=2, pady=2)
l.pack(fill="both", expand="yes")

l2 = LabelFrame(fen, text="Decryptage", padx=2, pady=2)
l2.pack(fill="both", expand="yes")

def encrypt():
    message = saisieCryptage.get()
    message_crypted = ""
    for letter in message:
        inputnb =ord(letter)
        x = inputnb // 16
        y = inputnb % 16
        output = ((5*x-y)% 16)* 16 + y
        message_crypted +=chr(output)
    saisieDecryptage.set(message_crypted)

def decrypt():
    message = saisieDecryptage.get()
    message_crypted = ""
    for letter in message:
        inputnb =ord(letter)
        x = inputnb // 16
        y = inputnb % 16
        output = (13*(x + y) % 16) * 16 + y
        message_crypted +=chr( output)
    saisieCryptage.set(message_crypted)
#**********CRYPTAGE**********#
#labelCryptage = Label(l, text="Crypter", width=25, height=1, fg='black')
#labelCryptage.pack(padx=5,pady=5)

saisieCryptage=StringVar()
entreeCryptage=Entry(l,textvariable=saisieCryptage, width=30)
entreeCryptage.pack(padx=10,pady=10)

bou=Button(l , text='Crypter' , command=encrypt)
bou.pack()
#**********DECRYPTAGE**********#
#labelDecryptage = Label(l2, text="Decrypter", width=25, height=1, fg='black')
#labelDecryptage.pack(padx=5,pady=5)

saisieDecryptage=StringVar()
entreeDecryptage=Entry(l2,textvariable=saisieDecryptage, width=30)
entreeDecryptage.pack(padx=10,pady=10)

bou1=Button(l2 , text='Decrypter' , command=decrypt)
bou1.pack()
#*******************************#
fen.mainloop()