# Tugas 5: Web Design Using HTML, CSS, and CSS Framework
### Abraham Javier Sebastian Situmorang -- 2106704364 -- Kelas D
### Link Aplikasi Heroku [di sini](https://tugas02pbpbas.herokuapp.com/todolist/login/)

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
### Inline CSS
Inline CSS merupakan kode CSS yang ditulis langsung pada atribut elemen HTML. Atribut <style> digunakan untuk memberikan style ke tag HTML tertentu.

Kelebihan Inline CSS:
- Sangat membantu jika hanya melakukan pengujian dan melihat perubahan suatu elemen
- Berguna untuk memperbaiki kode program dengan cepat
- Proses Request HTTP yang lebih kecil dan load akan lebih cepat
  
Kekurangan Inline CSS:
- Inline CSS harus diterapkan pada setiap elemen, sehingga kurang efisien
  
### Internal CSS
Dalam Internal CSS, Kode diletakkan di dalam bagian <head> pada halaman dan di dalam tag <style></style>.

Kelebihan Internal CSS:
- Perubahan hanya terjadi pada 1 halaman
- Class dan ID dapat digunakan oleh internal stylesheet
- Tidak perlu melakukan upload beberapa file karena HTML dan CSS bisa digunakan di file yang sama.

Kekurangan Internal CSS:
- Waktu akses website jadi meningkat
- kurang efisien jika menggunakan CSS yang sama pada beberapa file karena perubahan hanya terjadi pada 1 halaman  
  
### External CSS
Dalam External CSS, File CSS  diletakkan setelah bagian <head> pada halaman

Kelebihdan External CSS:
- Ukuran file HTML menjadi lebih kecil serta strukturnya menjadi lebih rapi
- Kecepatan loading meningkat
- File CSS yang sama dapat digunakan pada banyak halaman.

Kekurangan External CSS:
- Halaman belum dapat tampil secara sempurna hingga file CSS selesai dipanggil.
  
## Jelaskan tag HTML5 yang kamu ketahui.
```<button>```	membuat button yang dapat diklik.
```<div>```     menspesifikan sebuah section dalam document.
```<form>```	  men-define HTML form untuk input user.
```<html>```	  men-define root dari HTML document.
```<i>```	      mengubah style teks menjadi huruf itallic.
```<img>```	    merepresentasikan sebuah gambar.
```<input>```	  men-define input control.
```<li>```	    men-define list item.
```<title>```	  men-define title dari document.

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Terdapat 6 macam selektor di CSS, yaitu:
1. Selektor Tag, memilih elemen berdasarkan nama tag
2. Selektor Class, memilih elemen berdasarkan nama class yang diberikan. Selektor class dibuat dengan tanda titik di depannya.
3. Selektor ID, hampir sama dengan class, tetapi bersifat unik dan hanya boleh digunakan oleh satu elemen saja.
4. Selektor Atribut, memilih elemen berdasarkan atribut
5. Selektor Universal, digunakan untuk menyeleksi semua elemen pada jangkauan tertentu.
6. Selektor Pseudo, memilih elemen semu seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagainya. Terdapat dua macam selektor pseudo, yaitu pseudo-class selektor untuk state elemen dan pseudo-element selektor untuk elemen semu di HTML

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pada tugas 5 ini saya sebagian besar melakukan perubahan pada template di app todolist karena melakukan styling. Saya menggunakan framework Bootstrap karena telah dipelajari pada tutorial sebelumnya. Untuk menggunakannya, saya memasukan kode ```<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">``` pada bagian head. 

Styling yang saya lakukan di antaranya menambahkan background, merapikan layout, mengubah table pada todolist.html menjadi bentuk card, styling agar card berubah warna ketika di-checklist sudah selesai, hingga mengerjakan soal bonus yakni menambahkan efeh hover zoom dan shadow pada card todolist.
