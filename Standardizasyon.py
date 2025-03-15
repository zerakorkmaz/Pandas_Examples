#bunu yapabilmek için biraz araştırma yapmam gerekti. Kafama oturmadı tam.
#Z-score standartizasyonunu kullanacağım.SP 500 Stock Prices 2014-2017 isimli data set üzerinde çalışacağım.

import pandas as pd

df = pd.read_csv("SP 500 Stock Prices 2014-2017.csv")
print(df.head())

columns_to_standardize = ["open", "high", "low", "close", "volume"]

for column in columns_to_standardize:
    mean = df[column].mean()
    std = df[column].std()
    df[column] = (df[column] - mean) / std

df.to_csv("SP_500_Stock_Prices_Standardized.csv", index=False)
print(df.head())
