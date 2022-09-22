### Abraham Javier Sebastian Situmorang
### 2106704364 -- PBP-D
https://tugas02pbpbas.herokuapp.com/mywatchlist/html/
 
## 1. Jelaskan perbedaan antara JSON, XML, dan HTML!
### a) JSON (JavaScript Object Notation)
JSON merupakan format data open-standard data atau bersifat semi-structured. JSON besifat text-based dan dapat dibaca oleh manusia atau mesin. JSON dikumpulkan sebagai sebuh "events" yang diorganisasi secara batches. JSON dapat digunakan pada banyak aplikasi, tetapi JSON utamanya digunakan untuk mentransfer data antara server dan web application atau device yang terkoneksi dengan web karena aplikasi tersebut umumnya hanya dapat menerima data berbentuk text. File JSON menyimpan data di dalam nested objects and arrays yang berisi value dirinya sendiri. Struktur ini sangat bersifat adaptable, columns dari data source tidak membatasi penambahan data ke collection. JSON merupakan alternatif XML untuk semi-structured data karena JSON dapat menyampaikan representasi objek secara lebih compact
 
### a) XML (eXtensible Markup Language) 
XML adalah bahasa untuk menyederhanakan proses pertukaran dan penyimpanan data. XML akan menyimpan data dalam format teks yang sederhana, dengan struktur yang terdiri dari 3 segmen yaitu Deklarasi, Atribut, dan Elemen. Sekilas, XML memang mempunyai kemiripan dengan HTML. Namun, XML dan HTML mempunyai beberapa perbedaan. XML lebih berfungsi untuk menyimpan dan mengirimkan data, bersifat case sensitive, terdiri dari data struktural, dan bersifat dinamis

### a) HTML (Hypertext Markup Language) 
HTML adalah bahasa markup yang digunakan untuk membuat halaman website. HTML terdiri dari kombinasi teks dan simbol yang disimpan dalam sebuah file. HTML memang mempunyai kemiripan dengan XML. Namun, HTML dan XML mempunyai beberapa perbedaan. XML lebih berfungsi untuk menampilkan data, bersifat case insensitive, tidak terdiri dari data struktural, dan bersifat statis
 
### 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Dalam pengimplementasian sebuah platform kita memerlukan data delivery data yang dibuat atau dikirmkan bisa saja memiliki format berbeda, oleh karena itu agar mempermudah pengiriman antar komputer dan platform kita menggunakan data delivery ini.

### 3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama-tama saya membuat app bernama ```mywatchlist``` dengan memasukan `python3 manage.py startapp mywatchlist` pada terminal

Kemudian, saya menambahkan aplikasi mywatchlist ke dalam `INSTALLED_APPS` di direktori ```project_django/settings.py```. setelah itu, di ```project_django/urls.py``` saya menambahkan url ke mywatchlist, lalu membuat ```urls.py``` di `/mywatchlist` untuk melakukan routing `/mywatchlist` ke ```views.py```
Setelah itu, saya membuat model dengan field sesuai dengan ketentuan. 
Setelah itu saya menjalankan `python manage.py makemigrations` dan `python manage.py migrate`
Saya pun membuat folder fixtures, dan file html
Saya juga membuat testing ke file test.py
 
### 4. Mengakses tiga URL di poin 6 menggunakan Postman, menangkap screenshot, dan menambahkannya ke dalam README.md
HTML
<img width="1552" alt="Screen Shot 2022-09-22 at 10 38 17" src="https://user-images.githubusercontent.com/101565771/191653271-8db086fc-a156-44cc-a3ef-bc456ad4276c.png">

XML
<img width="1552" alt="Screen Shot 2022-09-22 at 10 38 35" src="https://user-images.githubusercontent.com/101565771/191653279-f9934626-16c6-4314-903a-b1c163650115.png">

JSON
<img width="1552" alt="Screen Shot 2022-09-22 at 10 38 51" src="https://user-images.githubusercontent.com/101565771/191653284-75a98d69-87c9-4e99-abea-887beeb58ba3.png">
