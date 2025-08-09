Travel Insurance



Contents: 
Business Problem Understanding
Data Understanding
Data Preprocessing
Modeling
Conclusion


Business Problem Understanding

context

Asuransi Perjalanan (Travel Insurance) adalah salah satu dari sekian banyak asuransi yang menyediakan perlindungan selama 
anggota asuransi yang memiliki asiransi perjalanan ini sedang berpergian ke dalam kota maupun luar kota. 
Bahkan sekarang ini ada beberapa Negara yang mengharuskan traveller untuk memiliki asuransi perjalanan (travel Insurance) ini, 
sebagai contoh adalah Eropa dan Amerika. Jumlah Harga premi yang diberikan semua berdasarkan apa saja yang ingin 
dapat di cover, berapa lama dari trip nya, dan tujuan dari tripnya. 


Goals 

sebuah perusahaan yang bergerak di bidang travel insurance ingin mengetahui pemegang polis yang seperti apa yang akan
mengajukan claim untuk mendapatkan coverage yang dimiliki pemegang polisnya berdarahkan data history perjalanan, jenis
produk asuransi dan yang lainnya.

Analytic Approach

Jadi dari data histori yang kita miliki, Pertama-tama kita akan melakukan analisi data dan cleaning data agar data yang di
analisis tidak banyak error yang akan terjadi.

Setelah itu, kita akan melakukan klasifikasi pemegang polis yang akan mengajukan adalah yang seperti apa
agar dapat memahami jenis produk yang seperti apa yang risknya lebih tinggi sehingga memungkinkan pemegang
asuransi untuk melakukan claim.

Metric Evaluation

Karena disini goal kita adalah untuk mengetahui pemegang polis dengan jenis asuransi yang seperti apa yang akan melakukan
claim, maka untuk metric evaluation ini saya akan menggunakan Classification Metrics. Maka dari itu saya akan melakukan 
percobaan dengan melakukan evaluasi menggunakan  Accuracy,Precision, Recall, and F1-score,Confusion Matrix,
dan ROC-AUC (Receiver Operating Characteristic - Area Under Curve). 

Evaluasi evaluasi ini berguna untuk melakukan comparing jenis product untuk mengasilkan data yang balance dan hasil detect
data claim atau tidak claim yang baik.

Dataset Overview

-	Agency: Nama Agensi.
-	Agency Type: Tipe travel insurance.
-	Distribution Channel: Channel of travel insurance agencies.
-	Product Name: Nama Product asuransinya.
-	Gender: Jenis Kelamin.
-	Duration: berapa lama trip nya.
-	Destination: tujuan tripnya.
-	Net Sales: harga total premi yang di jualkan.
-	Commission (in value): komisi yang diterima.
-	Age: umur yang tertanggung.
-	Claim: Claim status.


Data Cleaning & Preprocessing
Membersihkan missing values(Gender)
Encoding Categorical dan numeric variable
Outliner

Exploratory Data Analysis
Data Visualisation dan relation

Feature Engineering
Membuat CommissionRate dan riskScore
Drop property yang tidak digunakan (agency)

Model Building & Evaluasi
. melakukan evaluasi seperti accurancy, Precision, Recall, F1-score
. melakukan LogisticRegression, RandomForestClassifier, dan AUC-ROC

Kesimpulan dan Recomendasi
memberikan kesimpulan dan recomendasi