#!/usr/bin/python3
'''
EXERCICE 3

'''

liste = {'carotte' : 2, 'tomate' : 1.5}


print('Result for %s: %.3f' % ('TEST 1', 10 / 3))

template = "Une %s coûte %s CHF."


print( template % ('tomate',liste['tomate'] ) )
print( template % ('carotte',liste['carotte'] ) )

temp = set("Ils ont des chapeaux ronds vive les Bretons")
print (len(temp))

"Julien".strip('Ju')