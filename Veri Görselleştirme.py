import pandas as pd
import matplotlib.pyplot as plt


file = "vgsales.csv"
df = pd.read_csv(file)

#eksik bilgileri tamamlayalım yine
df["Year"] = df["Year"].fillna(df["Year"].mean()).astype(int)
df["Publisher"] = df["Publisher"].fillna(df["Publisher"].mode()[0])

#görselleştirmeye hazırız.Histogramını oluşturalım.
plt.figure(figsize=(12, 6))
plt.hist(df["Global_Sales"].dropna(), bins=25, color='#4682B4', edgecolor='white', alpha=0.85)
plt.xlabel("Global Sales (Million Units)", fontsize=14, fontweight='bold', color='#333333')
plt.ylabel("Frequency", fontsize=14, fontweight='bold', color='#333333')
plt.title("Global Video Game Sales", fontsize=16, fontweight='bold', color='#222222')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

#Yıllara göre satış miktarlarını anlayabileceğimiz bir dağılım grafiği yapmak istiyorum.
plt.figure(figsize=(10, 6))
plt.scatter(df["Year"].dropna(), df["Global_Sales"].dropna(), alpha=0.5, color='red')
plt.xlabel("Yıl")
plt.ylabel("Global Sales (Milyon)")
plt.title("Yıllara Göre Oyun Satışları")
plt.show()

#En çok oyun çıkaran 10 yayıncıyı seçip bunların çıkardıkları oyun sayısına göre dilim grafiği hazırlayalım.
top_publishers = df["Publisher"].value_counts().nlargest(10)

plt.figure(figsize=(10, 6))
plt.pie(top_publishers, labels=top_publishers.index, autopct='%1.1f%%',
        colors=plt.cm.Paired.colors, startangle=140, wedgeprops={'edgecolor': 'white'})

plt.title("Top 10 Publishers by Number of Games Released", fontsize=14, fontweight='bold')
plt.show()




