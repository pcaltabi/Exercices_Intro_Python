#!/usr/bin/python3
"""
EXERCICE 13
programmation objet
"""

class Pet:
    def __init__(self, nom=0, age=0, poid=0):
        print('>une instance de Pet créée')
        self.nom = nom 
        self.poid = poid 
        self.age = age
    def __del__(self):
        print('>une instance de Pet détruite')
    def mange(self, quantite=1):
        self.poid += quantite*0.2
        print(self.nom, " a un poid de ", self.poid ," [Kg]")
    def __str__(self):
        return self.nom+', '+str(self.poid)+', '+str(self.age)

p1 = Pet()
p1.nom='Médor'
p1.age = 5
p1.poid = 20

'''print(p1)

 


