#!python3
import os
import sys
import glob

path_local = os.getcwd()
fichiers = glob.glob('*.*')

def size_comp(x):
    return x[0]

tableau = []
for f in fichiers :
    complet = os.path.join(path_local,f)
    tableau.append([os.stat(complet).st_size, f])

tableau.sort(key=size_comp)
for f in tableau :
    print(f[1], "\t=>", f[0])


