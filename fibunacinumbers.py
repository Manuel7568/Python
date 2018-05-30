# fibonacinumbers
n = int(input("Geben Sie eine Zahl ein "))
last = 1
secondlast = 1
lastSave = 0
print(1)
print(1)
for i in range(1, n+1):
    lastSave = last
    last += secondlast
    secondlast = lastSave
    print(last)

print("Fibunacifolge: ",last)
