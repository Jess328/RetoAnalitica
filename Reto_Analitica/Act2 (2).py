# %%
import math
import random
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns
from kneed import KneeLocator
import matplotlib.pyplot as plt

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

# %%
dfp = df[["total_items", "discount%", "Food%", "Fresh%", "Drinks%", "Home%", "Beauty%", "Health%", "Baby%", "Pets%"]]

ssd = []
ks = range(1,11)
for k in range(1,11):
    km = KMeans(n_clusters=k)
    km = km.fit(dfp)
    ssd.append(km.inertia_)

kneedle = KneeLocator(ks, ssd, S=1.0, curve="convex", direction="decreasing")
kneedle.plot_knee()
plt.show()

k = round(kneedle.knee)

print(f"Number of clusters suggested by knee method: {k}")

kmeans = KMeans(n_clusters=k).fit(df[["total_items", "discount%", "Food%", "Fresh%", "Drinks%", "Home%", "Beauty%", "Health%", "Baby%", "Pets%"]])
sns.scatterplot(data=df, x="weekday", y="hour", hue=kmeans.labels_)
plt.show()
# %%
cluster0 = df[kmeans.labels_==0]
#print(cluster0.describe())
sns.boxplot(x="variable", y="value", data=pd.melt(cluster0[["Food%", "Fresh%", "Drinks%", "Home%", "Beauty%", "Health%", "Baby%", "Pets%"]]))

# %%
cluster1 = df[kmeans.labels_==1]
print(cluster1.describe())
sns.boxplot(x="variable", y="value", data=pd.melt(cluster1[["Food%", "Fresh%", "Drinks%", "Home%", "Beauty%", "Health%", "Baby%", "Pets%"]]))

# %%
cluster2 = df[kmeans.labels_==2]
#print(cluster2.describe())
sns.boxplot(x="variable", y="value", data=pd.melt(cluster2[["Food%", "Fresh%", "Drinks%", "Home%", "Beauty%", "Health%", "Baby%", "Pets%"]]))

#%%
sns.boxplot(x="weekday", y="discount%", data=(cluster0))

#%%
cluster3 = df[kmeans.labels_==3]
print(cluster3.describe())
sns.boxplot(x="variable", y="value", data=pd.melt(cluster3[["Food%", "Fresh%", "Drinks%", "Home%", "Beauty%", "Health%", "Baby%", "Pets%"]]))


# %%
sns.boxplot(data=cluster0[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']])
plt.show()
sns.boxplot(data=cluster1[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']])
plt.show()
sns.boxplot(data=cluster2[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']])
plt.show()
sns.boxplot(data=cluster3[['Food%','Fresh%','Drinks%','Home%','Beauty%','Health%','Baby%','Pets%']])
plt.show()

# %%
sns.histplot(data=cluster0, x= 'weekday')
plt.show()
sns.histplot(data=cluster1, x= 'weekday')
plt.show()
sns.histplot(data=cluster2, x= 'weekday')
plt.show()
sns.histplot(data=cluster3, x= 'weekday')
plt.show()
# %%
sns.histplot(data=cluster0, x= 'hour')
plt.show()
sns.histplot(data=cluster1, x= 'hour')
plt.show()
sns.histplot(data=cluster2, x= 'hour')
plt.show()
sns.histplot(data=cluster3, x= 'hour')
plt.show()
# %%
