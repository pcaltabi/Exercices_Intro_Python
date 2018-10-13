#!/usr/bin/python3
'''
EXERCICE 6

'''

i=input('Rayon :')
num=float(i)
while num.is_integer() and num>0:
    result=3.14156 *num
    print(result)
    i=(input('Rayon :'))
    num= float(i)

print("Fin")

'''FIN'''