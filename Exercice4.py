#!/usr/bin/python3
'''
EXERCICE 4

'''

employes = {
    "lausanne": [
        "Julien",
        "Sophie",
        "Victor",
        "Paul",
        "Camille",
        "Prunille"
    ],
    "geneve": [
        "Anthéa",
        "Prunille",
        "Julien",
        "Florence",
        "Sophie",
        "Etienne",
        "Henry"
    ]
} 
 
my_list = []
my_list += [3, 9, 5, 7, 12, 3, 7, 5, 9]
print(my_list)
print(len(my_list))

'''
La virgule sépare les éléments
et permet d'avoir des types d'éléments différents
'''
print(my_list[0],my_list[1])

print(my_list[3:5])
my_list.sort(reverse=True)
print(my_list)
my_list.append(11)
my_list.sort()
print(my_list)

print("Les employé de la société")
0+0.1


'''
template = "Une %s coûte %s CHF."
print( template % ('tomate',liste['tomate'] ) )
print( template % ('carotte',liste['carotte'] ) )

temp = set("Ils ont des chapeaux ronds vive les Bretons")
print (len(temp))

"Julien".strip('Ju')
'''