#!/usr/bin/python3
"""
EXERCICE 8
pour vérifier que cela fonctionne il faut aller dans la console
type Exercice2.py | Exercice8.py
"""
import sys

while True:
     line = sys.stdin.readline()
     if not line :
        break
     print(str(len(line))+' '+line)
