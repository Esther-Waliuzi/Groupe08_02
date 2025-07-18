# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 07:29:52 2025

@author: congo
"""
note1 = float(input("Première note : "))
note2 = float(input("Deuxième note : "))
note3 = float(input("Troisième note : "))

moyenne = (note1 + note2 + note3) / 3

print(f"Moyenne : {moyenne:.2f}")

print("L'étudiant est reçu." if moyenne >= 10 else "L'étudiant n'est pas reçu.")