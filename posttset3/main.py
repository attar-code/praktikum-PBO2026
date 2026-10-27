from abc import ABC, abstractmethod

class Nasabah:
    NamaBank = "Bank Terserah"
    TotalNasabah = 0
    StatusLayanan = "Aktif"

    def __init__(self, nama, nik, pin):
        self.nama = nama
        self.nik = nik
        self.pin = pin

        # Agregasi: menyimpan referensi objek Rekening.
        self.rekening = []

        Nasabah.TotalNasabah += 1

    def tambah_rekening(self, rekening):
        # Implementasi agregasi.
        self.rekening.append(rekening)

class Rekening(ABC):
    NamaBank = "Bank Terserah"
    TotalRekening = 0
    BiayaAdmin = 5000

    def __init__(self, nomor_rekening, nasabah, saldo):
        self.NomorRekening = nomor_rekening
        self.nasabah = nasabah
        self._saldo = saldo
        self.__pin_transaksi = "474747"
        self.transaksi = []

        Rekening.TotalRekening += 1

    @abstractmethod
    def hitung_biaya(self):
        pass

    @abstractmethod
    def tampilkan_fitur(self):
        pass

    def jalankan(self):
        self.info_rekening()
        self.tampilkan_fitur()
        print(
            "Biaya layanan : Rp{:,.0f}".format(
                self.hitung_biaya()
            ).replace(",", ".")
        )

    def setor_tunai(self, nominal):
        if nominal > 0:
            self._saldo += nominal
            print("Setor tunai berhasil.")
        else:
            print("Nominal setor harus lebih dari 0.")

    def tarik_tunai(self, nominal):
        if 0 < nominal <= self._saldo:
            self._saldo -= nominal
            print("Tarik tunai berhasil.")
        else:
            print("Penarikan gagal.")

    def transfer(self, rekening_tujuan, nominal):
        if rekening_tujuan is self:
            print(
                "Transfer ke rekening yang sama "
                "tidak diperbolehkan."
            )
        elif nominal > 0 and nominal <= self._saldo:
            self._saldo -= nominal
            rekening_tujuan._saldo += nominal
            print("Transfer berhasil.")
        else:
            print("Transfer gagal.")

    def info_rekening(self):
        print("Nomor Rekening :", self.NomorRekening)
        print("Pemilik        :", self.nasabah.nama)
        print(
            "Saldo          : Rp{:,.0f}".format(
                self._saldo
            ).replace(",", ".")
        )

    def catat_transaksi(self, id_transaksi, jenis, nominal):
        transaksi = Transaksi(
            id_transaksi,
            self,
            jenis,
            nominal
        )

        self.transaksi.append(transaksi)

        return transaksi

class RekeningTabungan(Rekening):

    def __init__(
        self,
        nomor_rekening,
        nasabah,
        saldo,
        bunga
    ):
        super().__init__(
            nomor_rekening,
            nasabah,
            saldo
        )
        self.bunga = bunga

    def hitung_biaya(self):
        return Rekening.BiayaAdmin

    def tampilkan_fitur(self):
        print("Jenis          : Tabungan")
        print("Bunga          :", self.bunga, "%")

    def info_rekening(self):
        print("=== REKENING TABUNGAN ===")
        super().info_rekening()
        print("Bunga          :", self.bunga, "%")

class RekeningBisnis(Rekening):

    def __init__(
        self,
        nomor_rekening,
        nasabah,
        saldo,
        limit_transfer
    ):
        super().__init__(
            nomor_rekening,
            nasabah,
            saldo
        )
        self.limit_transfer = limit_transfer

    def hitung_biaya(self):
        return Rekening.BiayaAdmin + 2500

    def tampilkan_fitur(self):
        print("Jenis          : Bisnis")
        print(
            "Limit Transfer : Rp{:,.0f}".format(
                self.limit_transfer
            ).replace(",", ".")
        )

    def info_rekening(self):
        print("=== REKENING BISNIS ===")
        super().info_rekening()
        print(
            "Limit Transfer : Rp{:,.0f}".format(
                self.limit_transfer
            ).replace(",", ".")
        )

class Transaksi:
    NamaBank = "Bank Terserah"
    TotalTransaksi = 0
    BiayaTransaksi = 2500

    def __init__(
        self,
        id_transaksi,
        rekening,
        jenis,
        nominal
    ):
        self.IdTransaksi = id_transaksi
        self.rekening = rekening

        self.Jenis = jenis
        self.Nominal = nominal

        Transaksi.TotalTransaksi += 1

    def __str__(self):
        nominal_teks = "{:,.0f}".format(
            self.Nominal
        ).replace(",", ".")

        return (
            f"Transaksi {self.IdTransaksi} | "
            f"{self.Jenis} | Rp{nominal_teks}"
        )

    def tampilkan_transaksi(self):
        print("ID Transaksi :", self.IdTransaksi)
        print("Rekening     :", self.rekening.NomorRekening)
        print("Jenis        :", self.Jenis)
        print(
            "Nominal      : Rp{:,.0f}".format(
                self.Nominal
            ).replace(",", ".")
        )

    @staticmethod
    def validasi_jenis(jenis):
        jenis_valid = [
            "Setor Tunai",
            "Tarik Tunai",
            "Transfer",
            "Terima Transfer"
        ]

        return jenis in jenis_valid

class NotifikasiEmail:

    def kirim(self):
        print("Notifikasi dikirim melalui email.")

class NotifikasiSMS:

    def kirim(self):
        print("Notifikasi dikirim melalui SMS.")


def proses_notifikasi(notifikasi):
    notifikasi.kirim()

class StrukTransaksi:

    def __init__(self, transaksi):
        self.transaksi = transaksi

    def cetak(self):
        print("Struk dicetak:", self.transaksi)


def proses_struk(objek):
    objek.cetak()

if __name__ == "__main__":
    print("=== UJI ABSTRAKSI ===")

    try:
        Rekening("000", None, 0)

    except TypeError as error:
        print("Rekening tidak bisa dibuat langsung.")
        print("Bukti:", error)

    nasabah1 = Nasabah(
        "attar",
        "6471000000000001",
        "123456"
    )

    nasabah2 = Nasabah(
        "ryad",
        "6471000000000002",
        "654321"
    )

    print("\n=== DATA NASABAH ===")
    print("Nama:", nasabah1.nama, "| NIK:", nasabah1.nik)
    print("Nama:", nasabah2.nama, "| NIK:", nasabah2.nik)

    rekening1 = RekeningTabungan(
        "001",
        nasabah1,
        1_000_000,
        2.5
    )

    rekening2 = RekeningBisnis(
        "002",
        nasabah2,
        5_000_000,
        10_000_000
    )
    nasabah1.tambah_rekening(rekening1)
    nasabah2.tambah_rekening(rekening2)

    print("\n=== POLIMORFISME VIA PEWARISAN ===")

    daftar_rekening = [
        rekening1,
        rekening2
    ]

    for rekening in daftar_rekening:
        rekening.jalankan()
        print()

    print("=== SETOR TUNAI ===")

    rekening1.setor_tunai(200_000)

    print(
        "Saldo rekening 1: Rp{:,.0f}".format(
            rekening1._saldo
        ).replace(",", ".")
    )
    print("\n=== TARIK TUNAI ===")

    rekening2.tarik_tunai(500_000)

    print(
        "Saldo rekening 2: Rp{:,.0f}".format(
            rekening2._saldo
        ).replace(",", ".")
    )

    print("\n=== TRANSFER ===")

    rekening1.transfer(
        rekening2,
        300_000
    )

    print(
        "Saldo rekening 1: Rp{:,.0f}".format(
            rekening1._saldo
        ).replace(",", ".")
    )

    print(
        "Saldo rekening 2: Rp{:,.0f}".format(
            rekening2._saldo
        ).replace(",", ".")
    )

    transaksi1 = rekening1.catat_transaksi(
        "TR001",
        "Transfer",
        300_000
    )

    transaksi2 = rekening2.catat_transaksi(
        "TR002",
        "Terima Transfer",
        300_000
    )

    print("\n=== DATA TRANSAKSI ===")

    transaksi1.tampilkan_transaksi()
    print()

    transaksi2.tampilkan_transaksi()

    print("\n=== VALIDASI TRANSAKSI ===")

    print(
        "Transfer valid   :",
        Transaksi.validasi_jenis("Transfer")
    )

    print(
        "Pembayaran valid :",
        Transaksi.validasi_jenis("Pembayaran")
    )

    # ATRIBUT KELAS

    print("\n=== BIAYA ADMIN ===")

    print("Biaya admin awal:", Rekening.BiayaAdmin)

    Rekening.BiayaAdmin = 7500

    print("Biaya admin terbaru:", Rekening.BiayaAdmin)


    print("\n=== TOTAL DATA ===")

    print("Total Nasabah   :", Nasabah.TotalNasabah)
    print("Total Rekening  :", Rekening.TotalRekening)
    print("Total Transaksi :", Transaksi.TotalTransaksi)

    daftar_notifikasi = [
        NotifikasiEmail(),
        NotifikasiSMS()
    ]

    for notifikasi in daftar_notifikasi:
        proses_notifikasi(notifikasi)

    print("\n=== OPERATOR OVERLOADING ===")

    print(transaksi1)
    print(transaksi2)

    print("\n=== DUCK TYPING STRUK ===")

    struk = StrukTransaksi(transaksi1)

    proses_struk(struk)