# HRA OBĚŠENEC
import os  # Pro smazání obrazovky, práci se soubory

CELKOVY_POCET_ZIVOTU = 8

# Načte slova ze souboru a vrátí je jako seznam[]
def nacti_slovnik(cesta="slovnik_1000slov.txt"):
    
    seznam = []
    with open(cesta, "r", encoding="utf-8") as f:
        # Jeden řádek = jedna položka v seznamu
        for i in range(1000):  # Dle počtu řádků/slov v souboru
            seznam.append(f.readline().replace("\n", ""))
    
    return seznam

print("Načítám slovník...")
SLOVA_K_HADANI = nacti_slovnik()

zbyvajici_zivoty = CELKOVY_POCET_ZIVOTU
stav = "menu"  # Stavová proměnná - "menu/hra"
skore = -1  # Po skončení hry uloží předchozí skóre (po spuštění programu -1)
hadane_slovo = ""
jiz_hadano = set() # Seznam již hádaných písmenek
napoveda = ""  # Ukládá stav rozkrytí hádaného slova ("Py---n")

def zobraz_menu(skore):
    # Zobrazí hlavní menu, volá se po spuštění programu / ukončení hry (stisknutí klávesy)
    # stav = "menu"
    # obsluhuje vstup od uživatele (vybírá položky zadáním jejich čísel):
    # - 1) Nová hra ... zavolá funkci nova_hra()
    # - 2) Pravidla ... zobrazí pravidla hry a vrátí se k menu
    # - 3) Konec ... ukončí program

    os.system("cls")

    global stav
    stav = "menu"

    nazev_hry = "H R A   O B Ě Š E N E C"
    polozky_menu = "1) Nová hra\n2) Pravidla hry\n3) Konec"
    pravidla = f"""
PRAVIDLA

Hráč se snaží uhodnout tajné slovo (např. "Abeceda"), a to tím způsobem, že postupně zkouší různá písmena abecedy.
Pakliže písmeno ve slově není obsaženo, hráčí se strhne jeden život (bod).
Již na začátku je zobrazena nápověda v podobě "_______", kde počet znaků odpovídá délce hádaného slova
a každé uhodnuté písmenko se vždy objeví na všech odpovídajících pozicích (např. "A_e_e_a").

Hráč začíná s {CELKOVY_POCET_ZIVOTU} životy.
Výhra nastane po rozkrytí celého slova a celkové dosažené skóre je pak rovno počtu zbývajících životů.
"""

    print(f"{nazev_hry}\n{len(nazev_hry) * '='}\n")
    
    # Zobrazí informaci o výsledku minulé hry
    if skore == CELKOVY_POCET_ZIVOTU:
        print("V minulé hře jste získal(a) plný počet bodů!\n")
    elif skore > 0:
        print(f"V minulé hře jste získal(a) {skore} bod/-y/-ů.\n")
    elif skore > -1:
        print("Minule jste prohrál(a).\n")

    print(polozky_menu + "\n")
    volba = input("Vyberte jednu z možností: ").strip()

    if volba == "1":
        nova_hra()
    elif volba == "2":
        os.system("cls")
        print(pravidla + "\n(stiskněte Enter...)")
        input()
        zobraz_menu(skore)
    elif volba == "3":
        pass
    else:
        print("Neexistující položka menu (napište číslo \"1\", \"2\" nebo \"3\" bez uvozovek).")
        input("\n(stiskněte Enter...)")
        zobraz_menu(skore)


def nova_hra():
    # Vybere náhodné slovo z n-tice (souboru) a uloží jej do proměnné hadane_slovo
    # Do proměnné zbyvajici_zivoty uloží hodnotu z CELKOVY_POCET_ZIVOTU
    # Změní stavovou proměnnou stav na "hra"
    # Zavolá funkci zobraz_hru()

    global stav
    stav = "hra"
    global jiz_hadano
    jiz_hadano.clear()

    from random import choice
    global hadane_slovo
    hadane_slovo = choice(SLOVA_K_HADANI)

    global zbyvajici_zivoty
    zbyvajici_zivoty = CELKOVY_POCET_ZIVOTU

    global napoveda
    napoveda = len(hadane_slovo) * "_"

    os.system("cls")
    zobraz_hru(zbyvajici_zivoty, napoveda)


def zobraz_hru(zbyvajici_zivoty, napoveda):
    # Vypíše herní obrazovku s nápovědou ("----") a počtem životů
    # Zavolá funkci tah()

    print(f"\nZBÝVÁ VÁM {zbyvajici_zivoty} ŽIVOTŮ.\n")
    print(f"\"{napoveda}\"\n")

    tah()


def tah():
    # Vezme vstup (písmeno) od uživatele a vyhodnotí:
    # - zda již hráč písmeno nezkoušel,
    # - zda je v hádaném slově přítomno,
    # Doplní do hádanky ("-a-a") všechny výskyty uhádnutého písmena
    # Případně odečte jeden život
    # Vyhodnotí, zda došlo k výhře nebo prohře a případně zavolá funkci zaver(vysledek)
    # Když hra pokračuje, zavolá funkci zobraz_hru()
    
    while(True):
        hadane_pismeno = input("Hádejte písmeno: ").lower()
        global jiz_hadano
        if len(hadane_pismeno) == 1:
            if hadane_pismeno not in jiz_hadano:
                jiz_hadano.add(hadane_pismeno)
                if hadane_pismeno in hadane_slovo.lower():
                    global napoveda
                    napoveda = aktualizuj_napovedu(hadane_pismeno)
                    break
                else:
                    global zbyvajici_zivoty
                    zbyvajici_zivoty -= 1
                    break
            else:
                print("Toto písmeno jste již hádal(a).")
        else:
            print("Musíte zadat jen jedno písmeno bez uvozovek a stisknout Enter (např. \"a\").")


    if zbyvajici_zivoty > 0:
        if napoveda == hadane_slovo:
            zaver("vyhra")
        else:
            zobraz_hru(zbyvajici_zivoty, napoveda)
    else:
        zaver(False)

# Doplní uhodnuté písmeno na všechna místa nápovědy a vrátí nový řetězec
def aktualizuj_napovedu(hadane_pismeno):

    pocet_vyskytu = (hadane_slovo.lower()).count(hadane_pismeno)
    na_pozicich = []
    relativni_pozice = 0
    nova_napoveda = napoveda
    
    for i in range(pocet_vyskytu):
        na_pozicich.append((hadane_slovo[relativni_pozice:].lower()).index(hadane_pismeno) + relativni_pozice)
        relativni_pozice += (hadane_slovo[relativni_pozice:].lower()).index(hadane_pismeno) + 1

    for i in range(len(na_pozicich)):
        pozice = na_pozicich[i]
        if hadane_slovo[pozice].isupper():
            nova_napoveda = nova_napoveda[:pozice] + hadane_pismeno.upper() + nova_napoveda[pozice + 1:]
        else:
            nova_napoveda = nova_napoveda[:pozice] + hadane_pismeno + nova_napoveda[pozice + 1:]

    return nova_napoveda

def zaver(vysledek):
    # Oznámí výhru či prohru, zbývající životy (skóre), výsledek předchozí hry (proměnná skore)
    # Uloží zbývající životy do proměnné skóre
    # Po stisknutí libovolné klávesy zavolá funkci zobraz_menu()
    global skore

    print(f"\n{20 * '='}\n")
    if vysledek == "vyhra":
        print(f"ZVÍTĚZIL(A) JSTE S KONEČNÝM POČTEM {zbyvajici_zivoty} BODŮ/-U.")
        if skore > -1:
            if zbyvajici_zivoty > skore:
                print(f"Získal(a) jste o {zbyvajici_zivoty - skore} bod/-y/-ů více než v minulé hře.")
            elif zbyvajici_zivoty == skore:
                print("To je se stejným počtem jako v minulé hře.")
            elif zbyvajici_zivoty < skore:
                print(f"Získal(a) jste o {skore - zbyvajici_zivoty} bod/-y/-ů méně než v minulé hře.")
    else:
        print("Tentokrát jste prohrál(a).")
        print(f"Hledané slovo bylo \"{hadane_slovo}\".")

    skore = zbyvajici_zivoty

    input("\n(stiskněte Enter...)")
    zobraz_menu(skore)


zobraz_menu(skore)
