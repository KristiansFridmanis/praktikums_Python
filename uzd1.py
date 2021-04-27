""" 
Uzrakstiet programmu, kas ielasa skaitli (kā float) -
riņķa līnijas rādiusu un izvada uz ekrāna (print) 
riņķa līnijas garumu un laukumu, atbilstoši noformējot atbildi.
Pārbaudiet programmas darbību ar dažādiem ievaddatiem.
"""
import math

r1=float(input("Ievadi riņķa līnijas rādiusu: "))
garums=2*3.14*r1
laukums=3.14*r1*r1
print ("Riņķa līnijas garums ir", garums, "un riņķa laukums ir", laukums)