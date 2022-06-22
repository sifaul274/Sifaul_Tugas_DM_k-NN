# Data Kolom 1
weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
# Data Kolom 2
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

# Target
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

# Import LabelEncoder
from sklearn import preprocessing
# Membuat LabelEncoder
le = preprocessing.LabelEncoder()

# Mengubah data string menjadi angka
weather_encoded=le.fit_transform(weather)
print(weather_encoded)
temp_encoded=le.fit_transform(temp)
print(temp_encoded)
label=le.fit_transform(play)
print(label)

# Menggabungkan data weather dan temp menjadi satu tuple
features=list(zip(weather_encoded,temp_encoded))

# Membuat model
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)

# Melatih model
model.fit(features,label)

# Memprediksi
predicted= model.predict([[2,1]]) # 2:Sunny, 1:Hot
if predicted==1:
    print("Yes")
else:
    print("No")