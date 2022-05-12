# %%
import numpy as numpy
import pandas as pd
import math
import random
import seaborn as sns
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

# %%
print("TAMAÑO DEL DATASET")
print(" ")
print("Número de filas del dataset: ", len(df)) 
print("Número de columnas del dataset:", len(df.columns))

# --------------------- Análisis general --------------------- #
# %%
df.describe()

# ------------------- Análisis por variable ------------------- #

# %%
#total_items
print("valor mínimo: ", df['total_items'].min())
print("valor máximo: ", df['total_items'].max())
print("mean: ", df['total_items'].mean())
print("median: ", df['total_items'].median())
print("std: ", df['total_items'].std())

# %%
#discount
print("valor mínimo: ", df['discount%'].min())
print("valor máximo: ", df['discount%'].max())
print("mean: ", df['discount%'].mean())
print("median: ", df['discount%'].median())
print("std: ", df['discount%'].std())

# %%
#Food%
print("valor mínimo: ", df['Food%'].min())
print("valor máximo: ", df['Food%'].max())
print("mean: ", df['Food%'].mean())
print("median: ", df['Food%'].median())
print("std: ", df['Food%'].std())

# %%
#Fresh%
print("valor mínimo: ", df['Fresh%'].min())
print("valor máximo: ", df['Fresh%'].max())
print("mean: ", df['Fresh%'].mean())
print("median: ", df['Fresh%'].median())
print("std: ", df['Fresh%'].std())

# %%
#Drinks%
print("valor mínimo: ", df['Drinks%'].min())
print("valor máximo: ", df['Drinks%'].max())
print("mean: ", df['Drinks%'].mean())
print("median: ", df['Drinks%'].median())
print("std: ", df['Drinks%'].std())

# %%
#Home%
print("valor mínimo: ", df['Home%'].min())
print("valor máximo: ", df['Home%'].max())
print("mean: ", df['Home%'].mean())
print("median: ", df['Home%'].median())
print("std: ", df['Home%'].std())

# %%
#Beauty%
print("valor mínimo: ", df['Beauty%'].min())
print("valor máximo: ", df['Beauty%'].max())
print("mean: ", df['Beauty%'].mean())
print("median: ", df['Beauty%'].median())
print("std: ", df['Beauty%'].std())

# %%
#Health%
print("valor mínimo: ", df['Health%'].min())
print("valor máximo: ", df['Health%'].max())
print("mean: ", df['Health%'].mean())
print("median: ", df['Health%'].median())
print("std: ", df['Health%'].std())

# %%
#Baby%
print("valor mínimo: ", df['Baby%'].min())
print("valor máximo: ", df['Baby%'].max())
print("mean: ", df['Baby%'].mean())
print("median: ", df['Baby%'].median())
print("std: ", df['Baby%'].std())

# %%
#Pets%
print("valor mínimo: ", df['Pets%'].min())
print("valor máximo: ", df['Pets%'].max())
print("mean: ", df['Pets%'].mean())
print("median: ", df['Pets%'].median())
print("std: ", df['Pets%'].std())

# --------------------- Graficas --------------------- #

# %%
sns.set_style("white")
sns.displot(data=df, x="customer")
plt.show()

# %%
df.corr()
sns.heatmap(df.corr(), annot=True)

# %%
sns.scatterplot(data=df, x="total_items", y="discount%")
plt.show()

# %%
sns.displot(data=df, x="weekday", y="Food%")

# %%
T_items = df[df["total_items"] < 29] 
sns.boxplot(data=T_items,x="weekday",y="total_items")

# %%
Hour = df[df["hour"] > 0]
sns.boxplot(data=Hour,x="weekday",y="hour")
