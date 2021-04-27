"""
Izveidot funkciju, kura atgriež skaitļu kvadrātus, lietotāja norādītā apgabalā.
"""
def kvad(a):
    kvad=pow(a, 2)
    return kvad
cipars=float(input("ievadi skaitli:"))
print (kvad(cipars))