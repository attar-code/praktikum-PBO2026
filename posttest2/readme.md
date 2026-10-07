# Sistem Perbankan Sederhana

Program ini merupakan implementasi **Pemrograman Berorientasi Objek (PBO)** menggunakan Python dengan studi kasus sistem perbankan sederhana.

## Konsep PBO yang Diterapkan

* **Class & Object** — membuat class `Nasabah`, `Rekening`, dan `Transaksi`.
* **Constructor** — menggunakan `__init__()` untuk memberikan nilai awal pada object.
* **Encapsulation** — menggunakan atribut `protected` (`_saldo`) dan `private` (`__pin_transaksi`).
* **Inheritance** — `RekeningTabungan` dan `RekeningBisnis` mewarisi class `Rekening`.
* **Polymorphism / Method Overriding** — method `info_rekening()` dibuat berbeda pada setiap subclass.
* **Association** — `Rekening` memiliki hubungan dengan `Nasabah`.
* **Aggregation** — `Nasabah` dapat memiliki beberapa `Rekening`.
* **Composition** — `Rekening` memiliki kumpulan `Transaksi`.
* **Static Method** — `ValidasiJenis()` digunakan untuk memvalidasi jenis transaksi.
* **Class Attribute** — digunakan untuk menyimpan data seperti `TotalNasabah`, `TotalRekening`, dan `TotalTransaksi`.

## Fitur

Program dapat melakukan:

* Menampilkan data nasabah dan rekening
* Setor tunai
* Tarik tunai
* Transfer
* Menampilkan data transaksi
* Validasi jenis transaksi
* Menghitung total nasabah, rekening, dan transaksi