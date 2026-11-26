
####################################################LISTY###########################################################

# owoce = ["jabłko", "banan", "wiśnia", "banan"]
# #dozwolone duplikaty

# print(owoce[1])
# print(owoce[1:])
# owoce.sort() # nie trzeba tego definiować jako nową zmienną , wystarczy sama komenda, żeby posortować
# print(owoce) # lista została już posortowana, wystarczy ją wyświetlić

# owoce.append("truskawka")
# owoce.pop(2) # usunięcie trzeciego wyrazu w liście (indeksowanie jest od zera)

# owoce.append(["append1", "append2"]) # lista w liście (zagnieżdzona)
# owoce.extend(["extend1" , "extend2"]) # lista płaska, elementy dodane na tym samym poziomie

# print(owoce)


# owoce = [
#     ["jabłko", "banan", "wiśnia", "banan"],
#     ["a", "b", "c", "d","e"],
# # ]
# # el = owoce[1][3]  #[]wiersz     [w][k] kolumna
# # print(el)
# # print(owoce[1])

# # owoce[0][2] = "kiwi"
# # count = len(owoce[1])
# # print(count)

# tekst_CSV = "03/22/2025 jan KOWalski wypłata PLN: 8359"
# moja_lista = tekst_CSV.split()
# print(moja_lista)
# moja_lista.append(moja_lista[1] + " " + moja_lista[2])
# moja_lista.pop(1)
# moja_lista.pop(1)

# #alternatywnie
# # del moja_lista[1:2]

# print(moja_lista)

# #skoryguj znaki w imieniu i nazwisku
# moja_lista[4] = moja_lista[4].title() # Trzeba najpierw zdefiniować konkretną zmienną, którą korygujemy a potem 
# print(moja_lista)

# #################################################TUPLE############################################################

# print("*" * 100)

# owoce = ("jabłko", "banan", "wiśnia", "banan")
# # owoce[0]="truskawka" # TUPLE (KROTKA) to nie lista, tylko tak jak wcześniej - tekst
# print(owoce)

# a,b,c,d = owoce # przypisujemy kolejno zmiennym wartości z krotek
# print(b) # wynikiem w tym przypadku będzie "banan"

# #################################################ZESTAWY,ZBIORY####################################################

# owoce = {"jabłko", "banan", "wiśnia", "banan"} # dla zestawów/zbiorów (setów) nie ma zdefiniowanych duplikatów
# print(owoce) # wynikiem będzie set 3-elementowy w sposób NIEUPORZĄDKOWANY (losowa kolejność elementów)

# lista = list(owoce)
# lista.append("truskawka")
# zbiór = set(lista)
# print(zbiór)

############################################SŁOWNIKI (DICTionaries)###################################################

dict = {
    "brand": "Ford",
    "model": "Mondeo",
    "year": 1980,
    (1,3): "krotki",
    "wlasciwosci": ["skora","klima"]
}

dict["model"] = "Fiesta" # to dodaje wartość do klucza model
dict["year"] = 2000 # to podmienia wartość klucza year (można tylko zmieniać liczby ale nie teksty?)
print(dict)

x=dict["model"]
print(x)
print(dict["wlasciwosci"][1]) #wypisanie drugiego elementu listy z klucza wlasciwosci

a = dict.items() # wyświetla dict jako krotki
print(a)         # wyświetla dict jako krotki
