# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 07:30:13 2025

@author: congo
"""

usd = float(input("Montant en USD : "))

eur= usd*0.93
cfa= usd*610
gbp= usd*0.79

print(f"{usd} USD = {eur:.2f} EUR")
print(f"{usd} USD = {cfa:.2f} CFA")
print(f"{usd} USD = {gbp:.2f} GBP")
