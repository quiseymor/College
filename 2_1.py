import random

def Ssl(Sn, a):
    return Sn * (1 + a / 100)

def D(Sk, Sn):
    return Sk - Sn

Sn = float(input("Initial amount, $.: "))
a = float(input("Bid, % year: "))
N = int(input("Investment period, yers: "), 10)

print()
print("Initial amount = ", round(Sn, 2), " $.")
print("Bid = ", round(a, 2), "% year")
print("Investment period = ", round(N, 2), " year")
print()

Sprk = Sn * (1 + a / 100)
Sslk = Sn * (1 + a / 100)
prd = Sprk - Sn
sld = Sslk - Sn
Sprd = prd
Ssld = sld

for i in range(1, N + 1):
    print(i, " year\t", round(Sprk, 2), "\t", round(prd, 2), "\t",
          round(Sslk, 2), "\t", round(sld, 2))
    Sprd += prd
    Sprk += prd
    sld = Sslk * (1 + a / 100) - Sslk
    Sslk += sld
    Ssld += sld

print()
print("Total income:\t\t", round(Sprd-prd, 2), "\t\t\t", round(Ssld-sld, 2))
