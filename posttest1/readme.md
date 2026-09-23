# Sistem Manajemen Rekening dan Transaksi Perbankan Berbasis PBO

### Deskripsi

Program ini merupakan sistem perbankan sederhana yang dibuat menggunakan konsep PBO. Program digunakan untuk mengelola data nasabah, rekening, tabungan, dan transaksi.

Program dapat melakukan beberapa kegiatan dasar seperti:

* Menampilkan data nasabah dan rekening
* Setor tunai
* Tarik tunai
* Transfer antar rekening
* Menyimpan data tabungan
* Mencatat transaksi

### Class yang Digunakan

Program memiliki 4 class utama:

* **Nasabah** → menyimpan data nasabah seperti nama, NIK, dan PIN.
* **Rekening** → menyimpan data rekening dan saldo serta menangani setor, tarik, dan transfer.
* **Tabungan** → menyimpan data tabungan dan target tabungan nasabah.
* **Transaksi** → menyimpan data transaksi seperti ID, jenis transaksi, rekening, dan nominal.

### Konsep PBO yang Digunakan

* **Class & Object** -> menggunakan 4 class dan membuat objek dari masing-masing class.
* **Atribut & Method** -> menggunakan atribut kelas, atribut instance, serta method untuk menjalankan fungsi program.
* **Encapsulation & Property** -> saldo rekening menggunakan atribut private __saldo, kemudian diakses melalui @property dan setter.
* **Class Method** -> digunakan untuk mengubah biaya admin.
* **Static Method** -> digunakan untuk memvalidasi jenis transaksi
