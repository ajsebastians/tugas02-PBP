# Tugas 6: Javascript dan AJAX
### Abraham Javier Sebastian Situmorang -- 2106704364 -- Kelas D
### Link Aplikasi Heroku [di sini](https://tugas02pbpbas.herokuapp.com/todolist/login/)

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming merupakan progam yang berjalan secara berurutan (sequential). Saat suatu perintah dieksekusi, maka harus ditunggu hingga perintah tersebut selesai dieksekusi
dan pindah ke baris selanjutnya. Sementara itu, pada asynchrinous programming, program bisa dijalankan secara paralel karena program tidak perlu menunggu suatu proses selesai terlebih dahulu. 

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event Driven Programming merupakan paradigma ketika suatu program dieksekusi berdasarkan event yang ada. Salah satu contohnya adalah ketika sebuah tombol diklik
,akan dijalankan suatu fungsi. Contoh penerapannya adalah ketika menekan Buat Task

## Jelaskan penerapan asynchronous programming pada AJAX.
Asynchronous programming pada AJAX merupakan saat ketika method POST selesai dieksekusi maka method setelah post tersebut langsung dieksekusi. 
contohnya ketika membuat task baru maka card akan langsung muncul tanpa perlu refresh.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama-tama saya menambahkan ```def show_json``` pada views lalu meng-importnya ke dalam urls.py,
saya juga menambahkanAjax script, menambahkan add_task, dan membuat fungsi AJAX pada todolist.html dengan type POST untuk menambahkan data dari user.
Setelah itu, program pun selesai dan dapat berjalan secara asynchronus

