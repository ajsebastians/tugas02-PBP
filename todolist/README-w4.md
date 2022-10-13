# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django
### Abraham Javier Sebastian Situmorang -- 2106704364 -- Kelas D
### Link Aplikasi Heroku [di sini](https://tugas02pbpbas.herokuapp.com/todolist/login/)

## 1. Apa kegunaan ```{% csrf_token %}``` pada elemen ```<form>```? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen ```<form>```?
Cross-Site Request Forgery (CSRF) merupakan sebuah serangan yang membuat pengguna mengirimkan request ke app lain melalui app yang sedang digunakan tanpa disadari. Hal ini tentu tidak kita inginkan. Oleh karena itu, untuk mencegahnya digunakanlah ```{% csrf_token %}```.  

Dengan menggunakan ```{% csrf_token %}``` pada elemen ```<form>```, nantinya sebuah string akan dibuat untuk membandingkan nilai unik dari csrf_token pada saat pengguna akan mengakses method POST. Lalu, elemen ```form``` akan menyetujuinya jika pengguna mengakses dengan benar. Hal ini pun akan terus  diperbaharui setiap pengguna melakukan reload data. Karena inilah, data tidak dapat disalahgunakan.

Jika tidak terdapat potongan kode ```{% csrf_token %}``` pada elemen ```form```, akan muncul Forbidden Error (403), CSRF Verification Failed 

## 2. Apakah kita dapat membuat elemen ```<form>``` secara manual (tanpa menggunakan generator seperti ```{{ form.as_table }})```? Jelaskan secara gambaran besar bagaimana cara membuat ```<form>``` secara manual.
Bisa, kita dapat membuat elemen ```<form>``` secara manual. 
Hal yang perlu dilakukan yaitu ```{% csrf_token %}```, membuat method POST (`<form method="POST">`), membuat form dengan tabel yang dibuat 
pada HTML, dan menggunakan form pada context untuk melakukan update form.

## 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Ketika pengguna mensubmit data yang telah diisi melalui HTML form (menekan tombol submit), request berupa "POST" akan terkirim dan akan memanggil method dari view. Method tersebut akan mendapatkan data dari request serta membuat object baru pada database. Lalu, nantinya kita dapat mengambil data pada database ini dan di-filter sesuai data pengguna yang sedang login. 

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Pertama-tama saya membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya dengan mengetik ```python manage.py startapp todolist``` pada terminal dan menambahkan ```todolist``` pada ```INSTALLED_APPS``` di ```project_django/settings.py```

Kemudian, saya menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist dengan memasukkan ```path("todolist/", include("todolist.urls"))``` pada ```urlpatterns``` di ```project_django/urls.py```.

Lalu, saya membuat sebuah model Task yang memiliki atribut sesuai ketentuan di ```todolist/models.py```. Kemudian, tidak lupa saya menjalankan ```python manage.py makemigrations``` lalu ```python manage.py migrate``` untuk melakukan migrasi perubahan model ke database.

Kemudian, saya mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik dengan membuat fungi pada ```views.py```.

Kemudian, saya membuat halaman-halaman pada ```todolist/templates```. Misalnya halaman utama todolist dengan membuat file ```todolist.html```, halaman login dengan membuat ```login.html```, halaman register dengan membuat ```register.html```, dan halaman membuat task baru dengan membuat ```create_task.html``` 

Kemudian, saya membuat routing sehingga beberapa fungsi dapat diakses melalui URL sesuai ketentuan dengan menambahkan ```urlpatterns``` pada ```todolist/urls.py```.

Selanjutnya, saya melakukan git ```add```, ```commit```, dan  ```push```, melakukan deployment ke Heroku dengan ke Action lalu Re-run all jobs, dan menunggu deploy.

Kemudian, saya masuk ke heroku, membuka app, menekan tombol more di kanan atas, dropdown ke bawah hingga menemukan run console, mengetik bash, lalu nantinya akan masuk ke terminal heroku. Saya pun mengetik ```python manage.py createsuperuser``` lalu memasukkan username, email, dan password. Superuser pun dapat diakses melalui https://tugas02pbpbas.herokuapp.com/admin/login/?next=/admin/. 

Kemudian, saya membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku sesuai ketentuan. Tugas 4 pun selesai.
