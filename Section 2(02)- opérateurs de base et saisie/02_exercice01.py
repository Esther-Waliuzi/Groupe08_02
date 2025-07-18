# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 07:22:03 2025

@author: congo
"""
# Demander deux nombres
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

#affichage des résultats
print(f"Somme : {a + b}")
print(f"Différence : {a - b}")
print(f"Produit : {a * b}")
print(f"Quotient : {a / b if b != 0 else 'Division par zéro'}")
print(f"Division entière : {a // b if b != 0 else 'Division par zéro'}")
print(f"Reste : {a % b if b != 0 else 'Division par zéro'}")


