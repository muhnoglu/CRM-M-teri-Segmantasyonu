import pyodbc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# SQL Server veritabanına bağlanma
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost,1433;'  # Docker konteyneri üzerinden bağlanma
    'DATABASE=CRM_System;'  # Veri Tabanı
    'UID=muhammedhanoglu;'  
    'PWD=bjk691903.'  
)

# Veritabanından veri çekme sorguları
query = "SELECT * FROM Customers"
query2 = "SELECT * FROM Interactions"
query3 = "SELECT * FROM Sales"
query4 = '''
    SELECT 
        c.CustomerID, 
        c.Name, 
        SUM(s.Amount) AS TotalSpent
    FROM 
        Customers c
    LEFT JOIN 
        Sales s ON c.CustomerID = s.CustomerID
    GROUP BY 
        c.CustomerID, c.Name
    ORDER BY 
        TotalSpent DESC
'''
query5 = '''
    SELECT 
        c.CustomerID, 
        c.Name, 
        COUNT(i.InteractionID) AS InteractionCount
    FROM 
        Customers c
    LEFT JOIN 
        Interactions i ON c.CustomerID = i.CustomerID
    GROUP BY 
        c.CustomerID, c.Name
    ORDER BY 
        InteractionCount DESC
'''

# Veriyi dataframe olarak almak
df = pd.read_sql(query, conn)
df1 = pd.read_sql(query2, conn)
df2 = pd.read_sql(query3, conn)
df3 = pd.read_sql(query4, conn)
df4 = pd.read_sql(query5, conn)



# Veri Ön İşleme Fonksiyonu
def dataset(dataframe, head=True):
    print("-----------------------------------------------SHAPE-----------------------------")
    print(dataframe.shape)
    print("-----------------------------------------------İNFO------------------------------")
    print(dataframe.info())
    print("-----------------------------------------------İSNULL----------------------------")
    print(dataframe.isnull().sum().sort_values(ascending=False))
    print("-----------------------------------------------NUNİQUE---------------------------")
    print(dataframe.nunique())
    print("-----------------------------------------------DESCİRBE--------------------------")
    print(dataframe.describe())
    if head:
       print("-------------------------------------------HEAD------------------------------")
       print(dataframe.head())
       print("-------------------------------------------TAİL------------------------------")
       print(dataframe.tail())

# Dataset Analizi
dataset(df, head=True)
dataset(df1, head=True)
dataset(df2, head=True)
dataset(df3, head=True)
dataset(df4, head=True)

# Veri Görselleştirme

# 1. Satış Tutarlarının Dağılımı
plt.figure(figsize=(10, 6))
sns.histplot(df2['Amount'], bins=20, kde=True)
plt.title('Satış Tutarlarının Dağılımı')
plt.xlabel('Satış Tutarı')
plt.ylabel('Frekans')
plt.show()

# 2. En Yüksek Harcama Yapan Müşteriler
top_customers = df3.head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x='TotalSpent', y='Name', data=top_customers, palette='Blues_d')
plt.title('En Yüksek Harcama Yapan Müşteriler')
plt.xlabel('Toplam Harcama Tutarı')
plt.ylabel('Müşteri Adı')
plt.show()

# 3. Müşteri Etkileşim Sayısı
top_interactions = df4.head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x='InteractionCount', y='Name', data=top_interactions, palette='Greens_d')
plt.title('En Fazla Etkileşimde Bulunan Müşteriler')
plt.xlabel('Etkileşim Sayısı')
plt.ylabel('Müşteri Adı')
plt.show()

# 4. Eksik Verilerle İlgili Analiz
def missing_data(df):
    missing = df.isnull().sum().sort_values(ascending=False)
    missing_percent = (missing / len(df)) * 100
    missing_data_df = pd.DataFrame({'Missing Values': missing, 'Percentage': missing_percent})
    missing_data_df = missing_data_df[missing_data_df['Missing Values'] > 0]
    return missing_data_df

# Müşteri Veri Setinde Eksik Veriler
print("Eksik Veriler (Customers Tablosu):")
print(missing_data(df))

# Etkileşim Veri Setinde Eksik Veriler
print("Eksik Veriler (Interactions Tablosu):")
print(missing_data(df1))

# 5. Aykırı Değer Analizi (Satış Verisi)
plt.figure(figsize=(10, 6))
sns.boxplot(x=df2['Amount'])
plt.title('Satış Tutarlarındaki Aykırı Değerler')
plt.xlabel('Satış Tutarı')
plt.show()



# 7. Müşterilerin Şehir Bazında Dağılımı
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='City', palette='Set1')
plt.title('Müşterilerin Şehir Bazında Dağılımı')
plt.xlabel('Şehir')
plt.ylabel('Müşteri Sayısı')
plt.xticks(rotation=90)
plt.show()



# 7. Satış Tutarı ve Müşteri Etkileşim Sayısı Arasındaki Korelasyon
merged_df = pd.merge(df3, df4, on='CustomerID')
plt.figure(figsize=(10, 6))
sns.scatterplot(data=merged_df, x='TotalSpent', y='InteractionCount', hue='TotalSpent', palette='viridis')
plt.title('Satış Tutarı ve Müşteri Etkileşim Sayısı Korelasyonu')
plt.xlabel('Toplam Harcama')
plt.ylabel('Etkileşim Sayısı')
plt.show()

# 8. Korelasyon Matrisi (Sayısal Veriler)
plt.figure(figsize=(10, 6))
corr_matrix = df2[['Amount']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
plt.title('Satış Tutarı Korelasyon Matrisi')
plt.show()


# 7. Müşteri Harcama ve Etkileşim Korelasyonu
merged_df = pd.merge(df3, df4, on='CustomerID')
plt.figure(figsize=(10, 6))
sns.scatterplot(data=merged_df, x='TotalSpent', y='InteractionCount', hue='TotalSpent', palette='viridis')
plt.title('Satış Tutarı ve Müşteri Etkileşim Sayısı Korelasyonu')
plt.xlabel('Toplam Harcama')
plt.ylabel('Etkileşim Sayısı')
plt.show()




# SQL Sorguları


query_interactions = '''
    SELECT 
        c.CustomerID, 
        c.Name, 
        COUNT(i.InteractionID) AS InteractionCount
    FROM 
        Customers c
    LEFT JOIN 
        Interactions i ON c.CustomerID = i.CustomerID
    GROUP BY 
        c.CustomerID, c.Name
    ORDER BY 
        InteractionCount DESC
'''

query_correlation = '''
    SELECT 
        c.CustomerID, 
        SUM(s.Amount) AS TotalSpent,
        COUNT(i.InteractionID) AS InteractionCount
    FROM 
        Customers c
    LEFT JOIN 
        Sales s ON c.CustomerID = s.CustomerID
    LEFT JOIN 
        Interactions i ON c.CustomerID = i.CustomerID
    GROUP BY 
        c.CustomerID
'''


query_ınteractiontype = '''
SELECT DISTINCT I.InteractionType, SUM(S.Amount) AS TotalAmountSum
FROM Sales S
INNER JOIN Interactions I ON I.CustomerID = S.CustomerID
GROUP BY I.InteractionType;
'''

df_interactiontype = pd.read_sql(query_ınteractiontype, conn)
print(df_interactiontype)

plt.figure(figsize=(10,8))
sns.barplot(data=df_interactiontype, x='InteractionType', y='TotalAmountSum', palette="viridis")
plt.title("TotalAmountSum")
plt.tight_layout()
plt.show()





df_interactions = pd.read_sql(query_interactions, conn)
df_correlation = pd.read_sql(query_correlation, conn)




conn.close()#kapatma 


