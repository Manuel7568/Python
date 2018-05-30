# fibonacinumbers
n = int(input("Geben Sie eine Zahl ein "))
last = 1
secondlast = 0
lastSave = 0

print(1, end=" ")
for i in range(1, n):
    lastSave = last
    last += secondlast
    secondlast = lastSave
    print(last, end=" ")

print(" ")
print("Fibunacifolge: ",last)
