#!python3
import sys
import os
from random import randint

print(__name__ + ' chargé')
if __name__ == '__main__' :
    print('Exécuté individuellement')

''' NE RIEN FAIRE'''
def do_nothing():
    pass

def hasard(max) :
    return randint(0,int(max))

