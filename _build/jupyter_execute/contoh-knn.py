#!/usr/bin/env python
# coding: utf-8

# # Contoh Program kNN Classification
# Berikut adalah contoh program kNN klasifikasi yang dibuat menggunakan bahasa pemrograman python.
# 
# ## Data Latih
# Pertama, disediakan data latih yang berisi 2 fitur dan targetnya. Dua fitur tersebut yaitu ***weather*** (cuaca) dan ***temp*** (temperatur). Kemudian targetnya adalah ***play*** (bermain). Target (***play***) akan bernilai *Yes* (bermain) atau *No* (tidak bermain) tergantung pada nilai kedua fitur.

# In[1]:


# Data Fitur 1
weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
# Data Fitur 2
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

# Target
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']


# ## Mengubah Data String Menjadi Angka
# Untuk mengubah data fitur dan target yang bertipe string menjadi data numerik, dapat menggunakan LabelEncoder yang bisa diimport dari `scikit-learn`.

# In[2]:


# Import LabelEncoder
from sklearn import preprocessing
# Membuat LabelEncoder
le = preprocessing.LabelEncoder()


# In[3]:


# Mengubah data string menjadi angka
weather_encoded=le.fit_transform(weather)
print("weather:")
print(weather_encoded)
print("")
temp_encoded=le.fit_transform(temp)
print("temp:")
print(temp_encoded)
print("")
label=le.fit_transform(play)
print("play:")
print(label)


# Pada hasil pengubahan data diatas, untuk baris pertama yaitu fitur ***weather***, nilai **0** mewakili *Overcast*, nilai **1** mewakili *Rainy*, dan **2** mewakili *Sunny*. Untuk baris kedua yaitu fitur ***temp***, nilai **0** mewakili *Cool*, nilai **1** mewakili *Hot*, dan nilai **2** mewakili *Mild*. Kemudian untuk baris ketiga yaitu ***play***, nilai **0** mewakili *No* dan **1** mewakili *Yes*.

# In[4]:


# Menggabungkan data weather dan temp menjadi satu tuple
features=list(zip(weather_encoded,temp_encoded))


# ## Membuat Model
# Langkah berikutnya adalah membuat model dan melatih model menggunakan data latih.

# In[5]:


# Membuat model
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)

# Melatih model
model.fit(features,label)


# ## Memprediksi
# Lalu kita coba untuk memprediksi nilai target (***play***) menggunakan fitur yang kita tentukan sendiri, misalnya ***weather*** bernilai *Sunny* (**2**) dan ***temp*** bernilai *Hot* (**1**).

# In[6]:


# Memprediksi
predicted= model.predict([[2,1]]) # 2:Sunny, 1:Hot
if predicted==1:
    print("Yes")
else:
    print("No")

