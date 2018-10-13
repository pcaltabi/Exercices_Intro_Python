#!python3
import sys
import MODULE_01

MODULE_01.do_nothing()

entree = input('Entrez un nombre: ')
val=MODULE_01.hasard(int(entree))
print(val)