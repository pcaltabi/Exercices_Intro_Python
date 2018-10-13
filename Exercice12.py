#!/usr/bin/python3
"""
EXERCICE 12
gestion des exceptions
"""


try:
    #open('path_to_file')
    #print(d['birthdate'])
    print(10 / 0)
except FloatingPointError as e:
    print('FloatingPointError')
    print(e)
except OverflowError as e:
    print('OverflowError')
    print(e)
except ArithmeticError as e:
    print('ArithmeticError')
    print(e)    
except Exception as e:
    print('Exception')
    print(e)

