# factorial recursive

def fact(n):
    if(n==1):
        return 1
    else:
        return n * fact(n-1)

n = int(input("Geben Sie eine Zahl ein."))


print("Fakultaet von ", n , ": " , fact(n))