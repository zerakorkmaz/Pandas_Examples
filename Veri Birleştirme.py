#merge kullanarak iki stock data setini birleştireceğim.

import pandas as pd

df1 = pd.read_csv("SP 500 Stock Prices 2014-2017.csv")
df2 =pd.read_csv("GME_stock.csv")

# birleştirebilmek için ikinci data setine symbol sütununu ekliyorum
df2["symbol"] = "GME"

#sütun adları aynı şeyi ifade ediyor ama farklı biçimde yazılmış. Bunları aynı hale getireceğim.
df2_renamed=df2.rename(columns={"open_price": "open","high_price": "high","low_price": "low","close_price": "close","adjclose_price": "adj_close"})

df1["date"]=pd.to_datetime(df1["date"])
df2_renamed["date"]=pd.to_datetime(df2_renamed["date"])

merged_df=pd.merge(df1,df2_renamed,on="date")
print(merged_df)

#Birleştirme işlemini join ile de yapabiliriz.
