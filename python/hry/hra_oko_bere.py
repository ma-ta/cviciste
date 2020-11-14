####################
### Hra OKO BERE ###
####################

from random import randrange

print("========")
print("OKO BERE")
print("========\n")
print("Vítejte! ", end="")

# Globální proměnné
body = 0
tah_min = 2
tah_max = 10
max_bodu = 21
pokracovat = True

print("V tahu se losují čísla od {} do {}, \
avšak smíte získat maximálně {} bodů!"\
      .format(tah_min, tah_max, max_bodu))
print("Hodně štěstí!")

# Cyklus hry
while (pokracovat is True) and (body < max_bodu):

    print("\nAktuální stav bodů:", body)
        
    # Cyklus pokračovat vs. konec hry
    while True:
        vstup = input("Přejete si pokračovat?\nano(a) | ne(n): ")
        if (vstup == "ano") or (vstup == "a") or (vstup == "") or (vstup == "1"):
            body += randrange(tah_min, tah_max+1)
            break
        elif (vstup == "ne") or (vstup == "n") or (vstup == "0"):
            pokracovat = False
            break
        else:
            print("\nOdpovídejte pouze \"ano\"/\"a\" nebo \"ne\"/\"n\"!")

# Vyhodnocení hry
if body < max_bodu:
    print("\n=== DOSÁHLI JSTE", body, "BODŮ. ===")
    print("Do plného počtu chybí", max_bodu-body, "b.")
elif body == max_bodu:
    print("\n*** VYHRÁLI JSTE! MÁTE PŘESNĚ ", max_bodu, " BODŮ! ***", sep="")
else:
    print("\n--- PROHRÁLI JSTE! ", body, " BODŮ JE PŘÍLIŠ! ---", sep="")

print()
input("(Stiskni Enter...)")