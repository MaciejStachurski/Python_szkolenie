import pandas as pd

#odczyt pliku, wybór arkusza
# df = pd.read_excel(r'dane\samochody.xlsx', sheet_name="dane")

# print(df.head().to_string())

# print(df.shape)

# df = pd.read_excel('dane.xlsx', usecols="A,D,K")

df = pd.read_excel(
    r'dane\samochody.xlsx', sheet_name="dane"
    # sep=";",
    # encoding="utf-8-sig"
)

# print(dane.shape)

# print(dane.columns.tolist())
# print(dane.dtypes)

# Pobranie konkretnej kolumny

nazwy = df['Marka'].unique()
# print(nazwy)

# Filtrowanie danych (np. tylko pojazdy droższe niż 50 000):
drogie_pojazdy = df[df['Cena_PLN'] > 50000]
# print(drogie_pojazdy)

kolumny = [ 'Kolor','Cena_PLN', 'Marka']
filtr = ((df["Kolor"] == 'Czerwony') | (df["Kolor"] == 'Biały')) \
         & (df['Cena_PLN'] <= 50000)

marka = df['Marka'].astype("string")
marka = marka.str.lower()
df['Marka_clean'] = marka

# filtr_bmw = df["Marka"].str.contains("bmw")

# print(filtr_bmw)

# filtr2 = (df["Kolor"].isin (['Czerwony','Biały','Różowy']) & (df['Cena_PLN'] <= 100000)) \
#         & (df["Marka"].str.contains("bmw",case=False))

# print(filtr2)

# df_filtr2 = df.loc[filtr,kolumny]
# print(df_filtr2)


# nazwy = (
#     df.loc[filtr,kolumny]
#     .sort_values(
#         ["Cena_PLN"],
#         ascending=[True]
#     )
# )

# print(nazwy)

wynik =df[df.isna().any(axis=1)] # axis=1 - szukanie po wierszach ; axis=0 - szukanie po kolumnach
# print(wynik)

df["Cena brutto"] = df['Cena_PLN'] * 1.23
# print(df)

df['Marka_Model']= (df['Marka'].astype("string")+" "+df['Model'])

# print(df)

df.loc[df["Kolor"].isin (['Czerwony','Biały']), 'Jaki kolor'] = "ładny" 
df.loc[~df["Kolor"].isin (['Czerwony','Biały']), 'Jaki kolor'] = "brzydki" 
# print(df[['Kolor', 'Jaki kolor']].to_string())


liczba = df['Cena_PLN'].count()  #Liczba niepustych cen
suma = df['Cena_PLN'].sum() # Suma cen wszystkich ofert
# print(liczba)
# print(suma)

# liczba_df = df.groupby('Marka_clean') \
#         .size() \
#         .reset_index(name='Liczba ofert')

# print(liczba_df)


# liczba_df = (df.groupby('Marka_clean', as_index=False) \
#     .agg(
#         Liczba_ofert=('Cena_PLN','count'),
#         Suma_cen=('Cena_PLN','sum'),
#         Srednia_cena=('Cena_PLN','mean')
#     ).sort_values('Liczba_ofert', ascending=False)
# )
# # print(liczba_df)

# moja_ramka = pd.DataFrame([{
#     'Marka_clean': 'TOTAL',
#     'Liczba_ofert':liczba_df['Liczba_ofert'].sum(),
#     'Suma_cen':liczba_df['Suma_cen'].sum(),
#     'Srednia_cena':liczba_df['Srednia_cena'].mean()
# }])

# liczba_df = pd.concat([liczba_df,moja_ramka])

# # print(moja_ramka)
# print(liczba_df)


# liczba_df.to_excel(r"dane\raport1.xlsx", index=False, sheet_name="moje_dane")


lokalizacje = df['Lokalizacja'].unique()

for lok in lokalizacje:
    ramka_filtr = df.loc[df['Lokalizacja'] == lok]

    liczba_df = (ramka_filtr.groupby('Marka_clean', as_index=False) \
        .agg(
            Liczba_ofert=('Cena_PLN','count'),
            Suma_cen=('Cena_PLN','sum'),
            Srednia_cena=('Cena_PLN','mean')
        ).sort_values('Liczba_ofert', ascending=False)
    )
    # print(liczba_df)

    moja_ramka = pd.DataFrame([{
        'Marka_clean': 'TOTAL',
        'Liczba_ofert':liczba_df['Liczba_ofert'].sum(),
        'Suma_cen':liczba_df['Suma_cen'].sum(),
        'Srednia_cena':liczba_df['Srednia_cena'].mean()
    }])

    # liczba_df = pd.concat([liczba_df,moja_ramka])

# print(moja_ramka)
# print(liczba_df)


    # liczba_df.to_excel("dane\\" + lok + ".xlsx", index=False, sheet_name="moje_dane")



# policz ile jest pojazdów ładnych i brzydkich


kolory = (liczba_df.groupby('Jaki kolor', as_index=False) \
        .agg(
            Ile = ("Cena_PLN", "count")
        ).sort_values('Ile', ascending=False)
    )

total =df["Cena_PLN"].count()
kolory["udział%"] = (kolory["Ile"] / total) * 100
# policz % w totalu

moja_ramka = pd.DataFrame([{
    "Jaki kolor": "TOTAL",
    "Ile": total,
    "udział %" : 100
}])

wynik = pd.concat([kolory,moja_ramka], ignore_index = True)
print(wynik)

