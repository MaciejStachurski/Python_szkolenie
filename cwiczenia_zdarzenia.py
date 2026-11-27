from dane.dane_v2 import zdarzenia
from prettytable import PrettyTable as pt
from tkinter import simpledialog

# data = []
# lotnisko = []
# type = []



#1


wybor = simpledialog.askstring(
    "Format raportu",
    "W jakim formacie zapisać wynik? Wpisz: csv lub json"
)

if wybor is None:
    print("Anulowano przez użytkowanika. Koniec programu.")
    exit()

wybor = wybor.strip().lower()

if wybor != "csv" and wybor != "json":
    print(f"Błędny format: '{wybor}'")
    exit()

ile_zdarzen = 0
ile_minor = 0
ile_serious = 0
po_lotnisku = {}
po_typie = {}

for data,lotnisko,typ,powaga,samolot in zdarzenia:
    ile_zdarzen += 1
    if powaga == "serious":
        ile_serious += 1
    else:
        ile_minor += 1
    if lotnisko not in po_lotnisku:
        po_lotnisku[lotnisko] = [0,0]

    po_lotnisku[lotnisko][0] += 1
    if powaga == "serious":
        po_lotnisku[lotnisko][1] += 1

    if typ not in po_typie:
        po_typie[typ] = 0
    po_typie[typ] += 1

# print(po_lotnisku)
# print(data)
# print(ile_zdarzen)


 # WYŚWIETLANIE TABELI

tabela_lotniska = pt(["Lotnisko","Razem","Minor","Serious","Ryzyko (%)"])
lotniska_do_json = {}

for lotnisko, dane in po_lotnisku.items():
    razem = dane[0]
    serious = dane[1]
    minor = razem - serious
    ryzyko = round((serious/razem)*100,1)

    tabela_lotniska.add_row([lotnisko,razem,minor,serious,f"{ryzyko}%"])

print("\n=== ANALIZA PO LOTNISKU (ICAO) ===")
print(tabela_lotniska)

tabela_typy = pt(["Typ zdarzenia", "Liczba"])

for typ,liczba in po_typie.items():
    tabela_typy.add_row([typ,liczba])

print("\n=== ANALIZA PO TYPIE ZDARZENIA ===")
print(tabela_typy)

# Zapis do pliku

if wybor == "csv":
    sciezka = r"dane\raport_lotniczy"
    with open(sciezka, "w", enconding="utf-8", newline="") as plik:
        plik.write(tabela_lotniska.get_csv_string(delimiter=";"))
        plik.write("\n")
        plik.write(tabela_typy.get_csv_string(delimiter=";"))
    print(f"\nZapisano raport CSV do pliku: {sciezka}")

elif wybor == "json":
    sciezka = r"dane\raport_lotniczy.json"
    with open(sciezka, "w", enconding="utf-8") as plik:
        plik.write(tabela_lotniska.get_csv_string(delimiter=";"))
        plik.write(tabela_typy.get_csv_string(delimiter=";"))
    print(f"\nZapisano raport json do pliku: {sciezka}")
    