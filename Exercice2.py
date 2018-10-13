#!/usr/bin/python3
'''
EXERCICE 2
Sachant que Julien Ambord mesure 1.82 mètres et qu'il pèse 72.3
kilogrammes, calculez son BMI (Body Mass Index) et affichez le
résultat dans une phrase contenant le nom de la personne (Le BMI
de M. XXX est YYY).
 Utilisez des variables afin de pouvoir modifier les paramètres facilement.
 Formule : BMI = poids[kg] / (taille[m])2
 Générez l'affichage suivant
(voir pdf)
'''
nom = "Julien Ambord"
hauteur = 1.82
masse = 72.3

adresse_ligne_1 = "Rue du Simplon 3"
adresse_ligne_2 = "1006 Lausanne"
espaces_ligne_adresse ="                                   "
concerne = "Votre nouvelle mission"

print(espaces_ligne_adresse+adresse_ligne_1)
print(espaces_ligne_adresse+adresse_ligne_2)
print("Concerne: "+concerne, end="\n\n" )
print("Monsieur,",end="\n\n" )

