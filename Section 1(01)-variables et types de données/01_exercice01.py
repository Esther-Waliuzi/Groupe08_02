# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 15:34:57 2025

@author: congo
"""
# Demande d'informations à l'utilisateur
prenom = input("Entrez votre prénom : ")
age = int(input("Entrez votre âge : "))
ville = input("Entrez votre ville : ")
metier = input("Entrez votre métier : ")

# Approximation des jours vécus
jours_vecus = age * 365

# Affichage formaté
print("\n== PROFIL UTILISATEUR ==")
print(f"Prénom : {prenom}")
print(f"Age : {age} ans ({jours_vecus} jours vécus environ)")
print(f"Ville : {ville}")
print(f"Métier : {metier}")








