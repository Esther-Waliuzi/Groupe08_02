# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 07:24:11 2025

@author: congo
"""

n = int(input("Entrez un nombre entier : "))

if n % 3 == 0 and n % 5 == 0:
    print("Le nombre est divisible par 3 et 5.")
else:
    print("Le nombre n'est pas divisible par 3 et 5 en même temps.")