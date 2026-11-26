# print ("Cześć. Hello")
import cowsay

# cowsay.cow("Cześć")
# cowsay.dragon("Cześćććć")
# print(cowsay.char_names)
# cowsay.ghostbusters("Cześćććć")

"""
Komentarz
abc abc 
"""
# print("tekst" , "inny tekst")
# print("tekst" + "inny tekst") #konkatenacja tekstów czyli "&"
# print("*" * 60)

# zmienne
# x=757
# y=1141
# z=x*y
# print(z)


# deklaracja
# definicja zmiennej
# abc = None # można zdefiniować zmienną bez żadnej wartości
# print("*" * 60)  # oddzielenie kolejnych kompilacji kodu
# # wartość = 1
# # print(wartość)
# u, t, s = "hi", "test", 183  # zdefiniowanie kilku zmiennych na raz
# print(u, t, s)
# p = 10
# k = 1.57  # float - liczba z cyframi po przecinku
# r = 0.3  # 30%
# w = True #bool

# y = '13.419'
# z = float(y) + p
# wynik = round(z,2)
# print(wynik)
# print(f"Wynik działania to: {wynik} po dodaniu liczb: {y} i {p}") # inny sposób wyświetlania tekstu
# kasa = 1411.125151
# print(f"Wynik działania to: {wynik} po dodaniu liczb: {y} i {p} wydam: {kasa:,.2f}") # ',.2f' zaokrągla liczbę do drugiego miejsca po przecinku i wstawia separatory, przecinek do oddzielenia miejsc tysięcznych, kropkę do cyfr po przecinku
# ładna_liczba = f"{kasa:_.2f}".replace("_"," ") # zamienienie separatora z "_" na " "
# print(f"Liczba: {ładna_liczba}")
# s=2**4
# # print(s)

# # print(len(str(ładna_liczba))) # zlicza liczbę znaków zmiennej
# # print(u,t,s, sep="+") # określenie separatora do wyświetlania tekstu

# # b = "Hello, World!"
# # print(b[2:5]) # wyciągnięcie znaków ze zmiennej, lewy przedział jest domknięty, ale drugi otwarty
# # txt = "Hello World" [::-1] # Czytanie na odwrót
# # print(txt)
# # imie = "maciek"

# # # stringi są niezmiennne, dlatego trzeba przygotować kopię zmiennej / nadpisać zmienną
# # poprawione_imie = imie.upper() # nowa zmienna która bierze inną zmienną i powiększa litery
# # print (poprawione_imie)

# # imie = imie.title()


# # #łańcuch wywołań - zmienia pierwszą literę na dużą a potem zamienia "c" na "ć"
# # imie = imie.title(). \
# #     replace("c","ć").replace("ć","k")
# # # Spacja z ukośnikiem " \" daje możliwość łamania wierszy komend, żeby nie było długiej komendy w jednej linijce
# # print(imie)


# #################################################CWICZENIE##########################################################

# tekst_CSV = "03/22/2025 jan KOWalski wypłata PLN: 8359"

# # dzien = tekst_CSV.find()

# #dzien
# # print(tekst_CSV[0:2])

# # miesiac
# # print(tekst_CSV[3:5])

# #rok
# # print(tekst_CSV[6:10])

# # poprawnione imię
# # imie = tekst_CSV[11:14]
# # poprawione_imie = imie.title()
# # # print(poprawione_imie)

# # #poprawnione nazwisko
# # nazwisko = tekst_CSV[15:23]
# # poprawione_nazwisko = nazwisko.lower().title()
# # # print(poprawione_nazwisko)

# # # Obliczenie wypłaty
# # dwukropek = tekst_CSV.find(":")
# # kasa = round(float(tekst_CSV[dwukropek + 4 :]) / 4.33 , 2)
# # # print(kasa)

# # print(f" Imię: {poprawione_imie}\n Nazwisko: {poprawione_nazwisko}\n Kasa w euro: {kasa}")

# from datetime import datetime, date, timedelta

# # 1. Pobranie aktualnego czasu
# teraz = datetime.now()
# print(f"Teraz jest: {teraz}")
# print(teraz)

# # 2. Tworzenie konkretnej daty
# urodziny = date(1995,10,25)
# print(f"Urodziny: {urodziny}")

# # 3. Arytmetyka dat (timedelta)
# # Co będzie za 100 dni?
# przyszlosc = teraz + timedelta(days=100)
# print(f"Za 100 dni będzie: {przyszlosc.date()}")
       
# # Obiekt -> Tekst
# ladna_data = teraz.strftime("%d.%m.%Y") # strftime - bierze stringa i formatuje na format czasowy
# print(f"Format europejski: {ladna_data}")
  

# data = tekst_CSV[0:10]
# data_prawidlowa = datetime.strptime(data, "%m/%d/%Y").date() #strptime - "p" to parse czyli przetwarza
# print(f"{data_prawidlowa}")




