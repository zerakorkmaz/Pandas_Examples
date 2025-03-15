#Kaggle üzerinden edindiğim video game sales data seti üzerinde çalışacağım.

#Önce datayı temizleyecek ve düzenleyeceğim.

import pandas as pd
import numpy as np

file= "vgsales.csv"
df = pd.read_csv(file)

print(df.head())
missing_values_df = df.isnull()

print("Columns containing missing data:")
print(missing_values_df.sum())

for column in missing_values_df.columns:
    missing_count = missing_values_df[column].sum()
    if missing_count > 0:
        print(f'\nColumn Name: {column}')
        print(f'Missin Data Count: {missing_count}')

# Year sütunu için ortalama ile dolduruyoruz
df["Year"] = df["Year"].fillna(df["Year"].mean()).astype(int)

#Publisher sütunundaki eksikleri de en çok tekrar eden ile doldurmak istedim.
df["Publisher"] = df["Publisher"].fillna(df["Publisher"].mode()[0])

print("\nUpdated Dataframe")
print(df.isnull().sum())

print("\nYear")
print(df["Year"].head())

print("\nPublisher")
print(df["Publisher"].head())

#"group by" kullanarak platforma göre listeleyebiliriz
print(df.groupby(by="Platform").count())

#yine group by kullanarak oyun türüne göre listeleyebiliriz
print(df.groupby(by="Genre").count())

#Şimdi de aynı veri seti üzerinde filter ve select işlemleri yapacağım.

#Önce Genre sütununda Aciton olanları filtreleyelim
print(df[df["Genre"] == "Action"])

#Platformu PS4 olan ve 2025 yılında çıkmış oyunların isim ve ranklarını filtreleyelim:
filtered_df= df[(df["Platform"] == "Wii") & (df["Year"] == 2007)]
print(filtered_df[["Name", "Rank"]])

#loc kullanarak da yapabiliriz
#Spor türünde olan ve çıkış yılı 2005 ile 2010 arasında olan oyunların isim ve global satış miktarlarını yazdırabiliriz.
print(df.loc[(df["Genre"]=="Sports") & (2005<= df["Year"]) & (df["Year"] <=2010),["Name","Global_Sales"]])

#query ve where kullanarak da filtreleme işlemlerini gerçekleştirebiliriz.
using_query = df.query("Genre == 'Action' and Platform == 'PS3'")
print(using_query[["Name","Year"]])

#where kullanırken dropna() kullanmadığımızda koşulları sağlamayan satırların yerıne NaN yazar.
using_where = df.where((df["Genre"] == "Action") & (df["Platform"] == "PS3")).dropna()
print(using_where[["Name","Year"]])

