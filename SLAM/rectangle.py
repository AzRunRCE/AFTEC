#!usr/bin/python3
def writeLine(caract_start,caract_mid,caract_end,many,croix_x,croix_y):
	i = 0;
	print(caract_start,end='')
	while i < many:
		if croix_x == i:
			print("\\",end='')
		elif croix_y == i:
			print("/",end='')
		else:
			print(caract_mid,end='')
		i += 1
	print(caract_end)
def whitespace(num):
	i = 0
	while (i<num):
		print(" ",end='')
		i += 1

def newline(num):
	i = 0
	while (i<num):
		print("")
		i += 1


y = int(input("indiquez y ?:"))
x = int(input("Indiquez x ?:"))
xpos = int(input("Indiquez x pos ?:"))
ypos = int(input("Indiquez y pos ?:"))

caract = input("Indiquez le caractére:")
i = 0
croix_x = 1
croix_y = y -2 
newline(xpos)
whitespace(ypos)
writeLine(caract,'-',caract,y,-1,-1)
while i<x-2:
	whitespace(ypos)
	writeLine(caract,' ',caract,y,croix_x,croix_y)
	croix_y -= 1
	croix_x += 1
	i += 1
whitespace(ypos)
writeLine(caract,'-',caract,y,-1,-1)
newline(xpos)
