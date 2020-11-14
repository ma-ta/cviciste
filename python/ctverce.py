import turtle

print("================")
print("KRESLENÍ ČTVERCŮ")
print("================\n")

pocet = int(input("Kolik čtverců mám nakreslit? "))
strana = int(input("Délka strany? "))
otoceni_st = int(input("Pootočení ve stupních: "))
zelva = input("Zobrazit želvu (\"1\" ano | \"0\" ne)? ")
if zelva not in ("0", "1"):
    zelva = False
else:
    zelva = bool(int(zelva))

if zelva:
    turtle.shape("turtle")

for i in range(pocet):
    for j in range(4):
        turtle.forward(strana)
        turtle.left(90)

    turtle.left(otoceni_st)

input("(\nEnter pro ukončení...)")