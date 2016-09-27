#!/usr/bin/env python3
# coding: utf-8
import string
import os
import socket
hote = "localhost"
port = 15555
user = input("Username:") + ": "
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))
msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    msg_a_envoyer = user + input(">")
    msg_a_envoyer = msg_a_envoyer.encode()
    connexion_avec_serveur.send(msg_a_envoyer)
print("Fermeture de la connexion")
connexion_avec_serveur.close()
