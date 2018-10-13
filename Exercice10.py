#!python3
import os
import sys

nom_fichier = 'ma_config.txt'
path_local = os.getcwd()
complet = os.path.join(path_local,nom_fichier)

if  not os.path.isfile(complet) :
    print("le fichier n'existe pas")
    fd = open(nom_fichier, mode = 'x')
    fd.write('Hello World')
    fd.close()