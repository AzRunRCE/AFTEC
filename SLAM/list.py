class Voiture:
    def __init__(self):
        Marque =""
        Annee = ""
        Modele = ""
    def getLabel(self):
        print(self.Marque + " " + self.Modele)

audi = Voiture()
audi.Marque = "Audi"
audi.Modele = "A3"
audi.Annee = "2000"
x = Voiture()
x.Marque = "Mercedes"
x.Modele = "CLS"
x.nextAnnee = "2000"
ListVoiture = [audi,x]
i = 0
while i < 2:
    ListVoiture[i].getLabel()
    i = i +1
import send

send.sendmsg("coucu")
