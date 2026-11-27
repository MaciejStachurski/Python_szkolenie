# bloki warunkowe

# kolor = "różowy"

# if kolor == "biały":  # znak == to równość, znak != to "nie równa się"
#     print("kupię")
# elif kolor == "różowy":
#     print("super")
# else:
#     print("nie kupię")
# print("test")

# kolor = "biały"

# cena = 70000
# #kupię w cenie do 65k zielony

# if cena<=65000 and (kolor == "zielony" or kolor == "biały"):  # tutaj jest ważny nawias, bo najpierw jest sprawdzany warunek "and" a potem "or" jak nie ma nawiasu
#     print("kupię")
# else:
#     print("nie kupię")

############################################## INPUTY #############################################################################


# # pobranie od usera
# cena = input("Podaj cenę: ")

# # test = "97fawfaw"
# # print(test.isdigit())

# if cena == "":
#     print("brak ceny")
# # elif cena.isdigit() == False:
#     # alternatywnie
# elif not cena.isdigit():
#     print("niepoprawna liczba")
# else:
#     print(f"cena: {cena}")

# import biblioteki która sprawdza czy cena została podana prawidłowo

# from tkinter import simpledialog

# kurs = simpledialog.askfloat("Kurs", "Podaj kurs", minvalue=0, maxvalue=10000000.0, initialvalue=2)

# if kurs == None:
#         print("nie podano kursu")
#         exit()
# else:
#     tekst_CSV = "03/22/2025 jan KOWalski wypłata PLN: 8359"
#     # Obliczenie wypłaty
#     dwukropek = tekst_CSV.find(":")
#     kasa = round(float(tekst_CSV[dwukropek + 2 :]) / kurs , 2)

#     print(f"Kurs to: {kurs}")
#     print(f"Kasa w euro to: {kasa}")


####################################################### PĘTLE #######################################################################


# cars = ['audi','bmw','skoda','kia']

# for pojazd in cars:
#     if pojazd == "skoda" or "audi":
#         print(f"Samochód: {pojazd} KUPIĘ")
#     else:
#         print(f"Samochód: {pojazd} NIE KUPIĘ")

#alternatywnie:
# for nr in range(len(cars)):
#     if cars[nr] == "skoda":
#         print(f"Samochód: {cars[nr]} KUPIĘ")
#     else:
#         print(f"Samochód: {cars[nr]} NIE KUPIĘ")


# Słownik
# garaz = {
#     "Toyota": "Corolla",
#     "Mazda": "CX-5",
#     "BMW": "M3",
#     "Tesla": "Model S"
# }

# for marka, model in garaz.items():
#     print(f"Marka: {marka} | Model: {model}")

# auta_szczegoly = {
#         "WA12345": {"marka": "Toyota", "rok": 2020, "przebieg": 50000},
#         "KR67890": {"marka": "BMW", "rok": 2018, "przebieg": 120000}
# }

# for rejestracja, kilometry in auta_szczegoly.items():
#     pojazd = rejestracja
#     przebieg = kilometry["przebieg"]
#     print(f"Rejestracja: {pojazd} ma przebieg: {przebieg}")

# alternatywnie:
# import dane1
# from dane1 import auta_szczegoly as kol
# for rejestracja, kilometry in kol.items():
#     pojazd = rejestracja
#     przebieg = kilometry["przebieg"]
#     print(f"Rejestracja: {pojazd} ma przebieg: {przebieg}")


from prettytable import PrettyTable as pt

tabelka = pt(["Pojazd","Rok"])

import dane1
from dane1 import garaz
for marka, opis in garaz.items():
    pojazd = marka
    rok = opis[1][0]
    #print(f"Marka: {pojazd} z rocznika: {rok}")
    tabelka.add_row([pojazd,rok])

csv = tabelka.get_csv_string()

print(csv)

print(tabelka)
