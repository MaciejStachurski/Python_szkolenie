# plik = open(r"dane\moje_dane.txt", "rt") # rt - read text, jakby to były obrazy, a nie pliki textowe, to wtedy "rb"
# zaw = plik.read()
# plik.close()

# # alternatywnie

# with open(r"dane\moje_dane.txt", "rt") as plik:  # z tą konstrukcją nie rzeba pisać plik.close bo samo "with" zapewnia, że to się samo zamknie po poniższej komendzie (po skończeniu bloku)
#     zaw = plik.read()

# print(zaw)


# #zapis

# with open(r"dane\moje_dane.txt", "a") as plik:
#     plik.write("\nabc dtyujmko gsgsegse")

# import dane z pliku "dane.csv"

from prettytable import PrettyTable as pt
import time

ile = 0
MAX_WIERSZY = 3000000
suma_cen = 0
ile_total = 0

pojazdy = {}
ceny = {}

czas_start = time.time()


with open(r"dane\dane_2_mln.csv", encoding="utf-8") as plik:
    for wiersz in plik:
        if ile == 0:
            ile += 1
            continue
        else:
            # print(wiersz.strip())
            ile += 1
            if ile == MAX_WIERSZY:
                break

            # właściwe działania
            lista = wiersz.split(";")
            pojazd = lista[1]
            cena = float(lista[2])

            suma_cen += cena
            ile_total += 1

            # uzupełnianie słownika
            # lokalizacje
            lokalizacja = lista[7]
            if lokalizacja not in pojazdy:
                pojazdy[lokalizacja] = {}

            if pojazd not in pojazdy[lokalizacja]:
                pojazdy[lokalizacja][pojazd] = [0,0]

            cena_obl = pojazdy[lokalizacja][pojazd][0] + cena
            liczba_obl = pojazdy[lokalizacja][pojazd][1] + 1
            pojazdy[lokalizacja][pojazd] = [cena_obl, liczba_obl]

# print(f"Pojazdów jest: {ile_total} suma cen to: {suma_cen}")
# print(pojazdy)


for lokalizacja, x in pojazdy.items():

    tabelka = pt(["Marka","Cena","Ilość","Srednia cena"])
    
    for pojazd, y in x.items():   
        ceny = f"{y[0]:,.0f}"
        ile = y[1]
        srednia = round(y[0] / y[1] , 1)
        tabelka.add_row([pojazd,ceny,ile, srednia])

    with open ("dane\\" + lokalizacja + ".txt","w",encoding="utf-8", newline="") as plik:
        plik.write(tabelka.get_string())
        plik.write("\n\n")
        plik.write(tabelka.get_csv_string(delimiter=";"))

czas_koniec = time.time()

ile_trwalo_czasu = f"{czas_koniec - czas_start:.2f} s"
print(f"Czas: {ile_trwalo_czasu}")

# dodaj do pliku koncowego dodatkowego info: średnia cena pojazdu