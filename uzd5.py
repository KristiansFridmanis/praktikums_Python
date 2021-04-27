"""
Uzrakstiet programmu Python, 
kas pieņem veselu skaitli (n) un 
aprēķina n + nn + nnn vērtību.
"""
def skaitlis(a):
    skaitlis=a+pow(a, 2)+pow(a, 3)
    return skaitlis
print (skaitlis(3))