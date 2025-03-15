#aynı data set üzerinde satış miktarlarını normalize edelim.

#öncesinde bu işlem için gerekli olmayan sütunları kaldıralım.

import pandas as pd

file= "vgsales.csv"
df = pd.read_csv(file)

df.drop(columns=["Rank","Platform","Year","Genre","Publisher"],inplace=True)
print(df.head().to_string())

#şimdi NA sales,EU sales, JP sales, Other sales ve Global sales sütunlarına normalizasyon yapalım

for column in ["NA_Sales","EU_Sales","JP_Sales","Other_Sales","Global_Sales"]:
    df[column] = df[column]/df[column].max()

print(df.head().to_string())



