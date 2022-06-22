# Apa itu k-Nearest Neighbors?

k-Nearest Neighbors atau kNN merupakan metode sederhana yang dapat memprediksi output numerik berdasarkan pada ukuran similaritas atau ukuran kemiripan data. k-Nearest Neighbors adalah algoritma yang berfungsi untuk melakukan klasifikasi suatu data berdasarkan data pembelajaran (train data sets) yang diambil dari ***k*** tetangga terdekatnya (nearest neighbors), dengan ***k*** merupakan nilai yang kita tentukan dan mewakili banyaknya tetangga terdekat.<br><br>
kNN merupakan algoritma non parametrik yang berarti tidak membuat asumsi apapun terhadap data. Algoritma KNN menerapkan *lazy learning* atau *instant based learning*. Artinya, algoritma tidak melakukan proses training dan membangun model. KNN menyimpan set data training dan “belajar” hanya pada saat membuat prediksi secara real-time.<br><br>
Algoritma KNN dapat digunakan untuk kasus klasifikasi (classification) maupun regresi (regression). Meskipun demikian, KNN lebih sering digunakan dalam proses klasifikasi.

## Algoritma kNN

1. Menentukan nilai ***k***
2. Menghitung jarak antara data uji dengan data latih
3. Mengurutkan jarak dari yang terkecil hingga terbesar
4. Mengambil data tetangga terdekat sebanyak ***k***
5. Menghitung rata-rata tetangga terdekat (dari langkah sebelumnya)