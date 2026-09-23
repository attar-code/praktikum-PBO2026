class Nasabah:
    NamaBank = "Bank Terserah"
    TotalNasabah = 0
    StatusLayanan = "Aktif"

    def __init__(self, nama, nik, pin):
        self.nama = nama
        self.nik = nik
        self.pin = pin
        Nasabah.TotalNasabah += 1


class Rekening:
    NamaBank = "Bank Terserah"
    TotalRekening = 0
    BiayaAdmin = 5000

    def __init__(self, NomorRekening, nasabah, saldo):
        self.NomorRekening = NomorRekening
        self.nasabah = nasabah
        self.__saldo = saldo
        Rekening.TotalRekening += 1

    def setor_tunai(self, nominal):
        if nominal > 0:
            self.__saldo += nominal
            print("Setor tunai berhasil.")
        else:
            print("Nominal setor harus lebih dari 0.")

    def tarik_tunai(self, nominal):
        if nominal > 0 and nominal <= self.__saldo:
            self.__saldo -= nominal
            print("Tarik tunai berhasil.")
        else:
            print("Penarikan gagal.")

    def transfer(self, RekeningTujuan, nominal):
        if nominal > 0 and nominal <= self.__saldo:
            self.__saldo -= nominal
            RekeningTujuan.saldo += nominal
            print("Transfer berhasil.")
        else:
            print("Transfer gagal.")

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo_baru):
        if saldo_baru >= 0:
            self.__saldo = saldo_baru
        else:
            print("Saldo tidak boleh negatif.")

    @classmethod
    def ubah_biaya_admin(cls, biaya_baru):
        if biaya_baru >= 0:
            cls.BiayaAdmin = biaya_baru
            print("Biaya admin berhasil diubah.")
        else:
            print("Biaya admin tidak boleh negatif.")


class Tabungan:
    NamaProduk = "Tabungan Silver"
    TotalTabungan = 0
    BungaTahunan = 2.5

    def __init__(self, NomorTabungan, nasabah, TargetTabungan):
        self.NomorTabungan = NomorTabungan
        self.nasabah = nasabah
        self.TargetTabungan = TargetTabungan
        Tabungan.TotalTabungan += 1


class Transaksi:
    NamaBank = "Bank Terserah"
    TotalTransaksi = 0
    BiayaTransaksi = 2500

    def __init__(self, IdTransaksi, rekening, Jenis, Nominal):
        self.IdTransaksi = IdTransaksi
        self.rekening = rekening
        self.Jenis = Jenis
        self.Nominal = Nominal
        Transaksi.TotalTransaksi += 1

    def TampilkanTransaksi(self):
        print("ID Transaksi :", self.IdTransaksi)
        print("Rekening     :", self.rekening.NomorRekening)
        print("Jenis        :", self.Jenis)
        print("Nominal      :", self.Nominal)

    @staticmethod
    def ValidasiJenis(jenis):
        jenis_valid = ["Setor Tunai", "Tarik Tunai",
                       "Transfer", "Terima Transfer"]

        return jenis in jenis_valid

nasabah1 = Nasabah("Ahmad", "6471000000000001", "123456")
nasabah2 = Nasabah("Rizky", "6471000000000002", "654321")

print(nasabah1.nama, nasabah1.nik)
print(nasabah2.nama, nasabah2.nik)

rekening1 = Rekening("001", nasabah1, 1_000_000)
rekening2 = Rekening("002", nasabah2, 500_000)
print("Rekening 1 :", rekening1.NomorRekening)
print("Pemilik    :", rekening1.nasabah.nama)
print("Saldo      :", rekening1.saldo)

print()
print("Rekening 2 :", rekening2.NomorRekening)
print("Pemilik    :", rekening2.nasabah.nama)
print("Saldo      :", rekening2.saldo)


rekening1.setor_tunai(200_000)
print("Saldo rekening 1 :", rekening1.saldo)

rekening2.tarik_tunai(100_000)
print("Saldo rekening 2 :", rekening2.saldo)
rekening1.transfer(rekening2, 300_000)

print("Saldo rekening 1 :", rekening1.saldo)
print("Saldo rekening 2 :", rekening2.saldo)

tabungan1 = Tabungan("T001", nasabah1, 5_000_000)
tabungan2 = Tabungan("T002", nasabah2, 3_000_000)

print(tabungan1.NomorTabungan, tabungan1.nasabah.nama, tabungan1.TargetTabungan)
print(tabungan2.NomorTabungan, tabungan2.nasabah.nama, tabungan2.TargetTabungan)
transaksi1 = Transaksi(
    "TR001",
    rekening1,
    "Transfer",
    300_000
)

transaksi2 = Transaksi(
    "TR002",
    rekening2,
    "Terima Transfer",
    300_000
)

transaksi1.TampilkanTransaksi()
print()
transaksi2.TampilkanTransaksi()

print("Biaya admin :", Rekening.BiayaAdmin)
Rekening.ubah_biaya_admin(7500)

print("Biaya admin :", Rekening.BiayaAdmin)

print(
    "Transfer valid :",
    Transaksi.ValidasiJenis("Transfer")
)
print(
    "Pembayaran valid :",
    Transaksi.ValidasiJenis("Pembayaran")
)
print("\nSaldo rekening 1 :", rekening1.saldo)
rekening1.saldo = 2_000_000
print("Saldo setelah diubah :", rekening1.saldo)
rekening1.saldo = -500_000
print("\nTOTAL DATA")
print("Total Nasabah   :", Nasabah.TotalNasabah)
print("Total Rekening  :", Rekening.TotalRekening)
print("Total Tabungan  :", Tabungan.TotalTabungan)
print("Total Transaksi :", Transaksi.TotalTransaksi)