# bloki warunkowe

kolor = "różowy"

if kolor == "biały":  # znak == to równość, znak != to "nie równa się"
    print("kupię")
elif kolor == "różowy":
    print("super")
else:
    print("nie kupię")
print("test")

kolor = "biały"

cena = 70000
#kupię w cenie do 65k zielony

if cena<=65000 and (kolor == "zielony" or kolor == "biały"):  # tutaj jest ważny nawias, bo najpierw jest sprawdzany warunek "and" a potem "or" jak nie ma nawiasu
    print("kupię")
else:
    print("nie kupię")