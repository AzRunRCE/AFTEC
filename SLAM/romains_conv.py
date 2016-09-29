#/* ************************************************************************* */
#/*                                                                    	      */
#/*                                            ______ _______ ______   _____  */
#/*  romains_conv.py                    /\    |  ____|__   __|  ____| / ____| */
#/*                                    /  \   | |__     | |  | |__   | |      */
#/*  By: quentin.martinez@aftec.org   / /\ \  |  __|    | |  |  __|  | |      */
#/*                            	     / ____ \ | |       | |  | |____ | |____  */
#/*  Created: 2015/28/09 11:44:22   /_/    \_\|_|       |_|  |______| \_____| */
#/*                                                                    	      */
#/* ************************************************************************* */
#! usr/bin/env python3
# -+- coding: utf-8 -*-

tab = [["I","IV","V", "IX","X","XL","L","XC","C","CD","D","CM","M"],[1,4,5,9,10,40,50,90,100,400,500,900,1000]] #Tableau de correspondance
nb_arabe = int(input("Entrez un nombre arabe:"))
i = 12 #Assignation de i a 12 (nbr d'elements dans le tableau 2 dimension)
while i >= 0: #Boucle parcous j'usqua la fin du tableau
	while nb_arabe-tab[1][i] >= 0: #Conditions de décrémentation de nombre arabe utilisateur
		print(tab[0][i], end='') #Affichage de la correspondance
		nb_arabe-= tab[1][i] #Décrémentation du nombre arabe utilisateur
	i-=1 #Décrémentation de i
