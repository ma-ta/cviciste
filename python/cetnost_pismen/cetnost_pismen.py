#
#   Program načte zvolený textový soubor,
#   zjistí počet výskytů obsažených znaků
#   a výsledek exportuje do souboru .CSV.
#
#   © 2020  Martin TÁBOR
#
#   -------------------------------------
# 
#   Potřebné knihovny:
#   - click
#


# KNIHOVNY:
import os, click


# FUNKCE:

# vypisuje informace do konzole
def std_out():
    NADPIS = "Četnost písmen".capitalize()
    print("=" * len(NADPIS))
    print(NADPIS)
    print("=" * len(NADPIS) + "\n")


# načítá textový soubor
def nacti_soubor(cesta):
    with open(cesta, "r", encoding="utf-8") as f:
        pismena = list(f.read().lower())
    
    return pismena


# počítá znaky
def cetnost_pismen():
    pismena = nacti_soubor("text.txt")
    pismena.pop(0)
    pismena.pop()
    pismena = tuple(pismena)
    cetnost = {}

    print("Počet znaků k analýze:", len(pismena), end="\n\n")
    jiz_precteno = set()

    for znak in pismena:
        if znak not in jiz_precteno:
            jiz_precteno.add(znak)
            cetnost[znak] = pismena.count((znak))

    with open("log.txt", "w", encoding="utf-8") as f:
        f.write(str(cetnost).replace(", ", "\n").strip("{}"))

    print(str(cetnost).replace(", ", "\n").strip("{}"))


# VSTUPNÍ BOD PROGRAMU:
if __name__ == "__main__":

    cetnost_pismen()
    input()
