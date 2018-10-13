#!/usr/bin/python3
"""
EXERCICE 13
programmation objet
"""

class Pet:
    def __init__(self, nom='', age=0, poid=0):
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

class Chien(Pet):

    def __init__(self, nom='', age=0, poid=0):
        super().__init__(nom, age, poid)
        print('>une instance de Chien créée')
        self.son = "Aboye"
    def __del__(self):
        print('>une instance de Chien détruite')

class Chat(Pet):

    def __init__(self, son=0):
        super().__init__(nom, age, poid)
        print('>une instance de Chat créée')
        self.son = "Miaule"
    def __del__(self):
        print('>une instance de Chat détruite')
    
class Poisson(Pet):
    pass

c1=Chien()
c1.age=2
c1.poid=4
c1.nom="Médor"
print(c1.son)
