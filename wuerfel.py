# wuerfel.py
from random import *
numcounts = int(input("Wie viele Durchläufe sollen gestartet werden?"))
anz1 = 0
anz2 = 0
anz3 = 0
anz4 = 0
anz5 = 0
anz6 = 0

for i in range(0,numcounts):
    rnd = randint(1,6)
    if(rnd == 1):
        anz1 += 1
    if(rnd == 2):
        anz2 += 1
    if(rnd == 3):
        anz3 += 1
    if(rnd == 4):
        anz4 += 1
    if(rnd == 5):
        anz5 += 1
    if(rnd == 6):
        anz6 += 1


print("Anzahl der gewürfelten Einser: " , anz1)
print("Anzahl der gewürfelten Zweier: " , anz2)
print("Anzahl der gewürfelten Dreier: " , anz3)
print("Anzahl der gewürfelten Vierer: " , anz4)
print("Anzahl der gewürfelten Fünfer: " , anz5)
print("Anzahl der gewürfelten Sechser: " , anz6)        