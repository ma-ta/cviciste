DELKA_POLE = 20
SYMBOL_HRACE = "x"
SYMBOL_POCITACE = "o"
SYMBOL_VOLNO = "-"

NADPIS = "1D PIŠKVORKY"
SLOVNI_INFO = {
    "uvod":
f"""{"=" * len(NADPIS)}
{NADPIS}
{"=" * len(NADPIS)}

Vítejte! Cílem hry je obsadit tři vedle sebe umístěná políčka.
Herní pole obsahuje celkem {DELKA_POLE} volných pozic, o něž soupeříte s počítačem.
Pakliže nezbyde žádné volné políčko, aniž někdo vyhrál, nastává remíza.""",
    "vyhra": "*** Vyhrál(a) jste ! ***".upper(),
    "prohra": "--- Prohrál(a) jste ---",
    "remiza": "=== Výsledek je REMÍZA ===",
    "obsazeno": "Toto políčko je obsazeno!",
    "mimo": f"Zadejte číslo od 1 do {DELKA_POLE}!",
    "zadani_policka": f"Číslo políčka pro Váš tah (1-{DELKA_POLE}): "
    }

def smazat_obrazovku():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def vyhodnot(pole):
    """
    Podle stavu herního pole vrátí:
     řetězec "x", když vyhraje hráč,
     řetězec "o", když vyhraje počítač,
     řetězec "!", když dojde k remíze nebo
     řetězec "-", když je možné ještě pokračovat ve hře
    """

    if SYMBOL_HRACE*3 in pole:
        return "x"
    if SYMBOL_POCITACE*3 in pole:
        return "o"
    if SYMBOL_VOLNO not in pole:
        return "!"
    
    return "-"


def tah(pole, cislo_policka, symbol):
    """
    Vrátí herní pole s daným symbolem umístěným na danou pozici.
    """

    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]


def tah_hrace(pole):
    """
    Zeptá se hráče, kam chce hrát, a vrátí herní pole s jeho zaznamenaným
    tahem.
    """
    
    while True:
        cislo_policka = int(input(SLOVNI_INFO["zadani_policka"])) - 1
        if cislo_policka >= 0 and cislo_policka <= DELKA_POLE-1:
            if pole[cislo_policka] == SYMBOL_VOLNO:
                return tah(pole, cislo_policka, SYMBOL_HRACE)
            else:
                print(SLOVNI_INFO["obsazeno"])
        else:
            print(SLOVNI_INFO["mimo"])


def tah_pocitace(pole):
    """
    Vrátí herní pole se zaznamenaným tahem počítače
    """
    
    from random import randrange

    while True:
        cislo_policka = randrange(0, DELKA_POLE)
        if pole[cislo_policka] == SYMBOL_VOLNO:
            return tah(pole, cislo_policka, SYMBOL_POCITACE)

def vypis_pole(pole):
    vypis = f"""
{((DELKA_POLE+4-12)//2)*"-"} HERNÍ POLE {((DELKA_POLE+4-12)//2)*"-"}
| {pole} |
{(DELKA_POLE+4) * "-"}"""
    
    return vypis


def piskvorky1d():
    """
    Hraje 1D piškvorky.
    """
    smazat_obrazovku()
    print(SLOVNI_INFO["uvod"])

    pole = DELKA_POLE * SYMBOL_VOLNO
    print(vypis_pole(pole))

    while vyhodnot(pole) == "-":
        pole = tah_hrace(pole)
        if vyhodnot(pole) == "-":
            pole = tah_pocitace(pole)
        smazat_obrazovku()
        print(SLOVNI_INFO["uvod"])
        print(vypis_pole(pole))
    
    if vyhodnot(pole) == SYMBOL_HRACE:
        print(SLOVNI_INFO["vyhra"])
    elif vyhodnot(pole) == SYMBOL_POCITACE:
        print(SLOVNI_INFO["prohra"])
    elif vyhodnot(pole) == "!":
        print(SLOVNI_INFO["remiza"])


if __name__ == "__main__":
     piskvorky1d()
     input()
