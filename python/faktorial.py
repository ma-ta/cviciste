"""
Výpočet faktoriálu
(příklad rekurzivní funkce)
"""


def faktorial(n):
    if n < 0:
        return ("není definován (záporné číslo)")
    elif n == 0:
        return 1
    else:
        return (n * faktorial(n - 1))


print("\n==================")
print("Výpočet faktoriálu".upper())
print("==================\n")

print("n! =", faktorial(int(round(float(input("Zadej číslo n: "))))))
input(("\n(Stiskni Enter...)"))
