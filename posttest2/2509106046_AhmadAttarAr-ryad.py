class Nasabah:
    NamaBank = "Bank Terserah"
    TotalNasabah = 0
    StatusLayanan = "Aktif"

    def __init__(self, nama, nik, pin):
        self.nama = nama
        self.nik = nik
        self.pin = pin

        # agregasi untuk nasabah berapa rekening
        self.rekening = []
        Nasabah.TotalNasabah += 1

    def tambah_rekening(self, rekening):
        self.rekening.append(rekening)


#superclass
class Rekening:
    NamaBank = "Bank Terserah"
    TotalRekening = 0
    BiayaAdmin = 5000

    def __init__(self, nomor_rekening, nasabah, saldo):
        self.NomorRekening = nomor_rekening

        # asosiasi dengan Nasabah
        self.nasabah = nasabah

        # protected
        self._saldo = saldo

        self.__pin_transaksi = "1234" #private

        # komposisi : rekening ada transaksi
        self.transaksi = []

        Rekening.TotalRekening += 1

    def setor_tunai(self, nominal):
        if nominal > 0:
            self._saldo += nominal
            print("Setor tunai berhasil.")
        else:
            print("Nominal setor harus lebih dari 0.")

    def tarik_tunai(self, nominal):
        if nominal > 0 and nominal <= self._saldo:
            self._saldo -= nominal
            print("Tarik tunai berhasil.")
        else:
            print("Penarikan gagal.")

    def transfer(self, rekening_tujuan, nominal):
        if nominal > 0 and nominal <= self._saldo:
            self._saldo -= nominal
            rekening_tujuan._saldo += nominal
            print("Transfer berhasil.")
        else:
            print("Transfer gagal.")

    def info_rekening(self):
        print("Nomor Rekening :", self.NomorRekening)
        print("Pemilik        :", self.nasabah.nama)
        print("Saldo          :", self._saldo)

    def tambah_transaksi(self, transaksi):
        self.transaksi.append(transaksi)

# subclass 1
class RekeningTabungan(Rekening):

    def __init__(self, nomor_rekening, nasabah, saldo, bunga):
        # constructor superclass
        super().__init__(nomor_rekening, nasabah, saldo)

        # atribut unik
        self.bunga = bunga

    # Method overriding
    def info_rekening(self):
        print("=== REKENING TABUNGAN ===")
        print("Nomor Rekening :", self.NomorRekening)
        print("Pemilik        :", self.nasabah.nama)
        print("Saldo          :", self._saldo)
        print("Bunga          :", self.bunga, "%")


# SUBCLASS 2
class RekeningBisnis(Rekening):

    def __init__(self, nomor_rekening, nasabah, saldo, limit_transfer):
        # memanggil constructor superclass
        super().__init__(nomor_rekening, nasabah, saldo)

        # atribut unik
        self.limit_transfer = limit_transfer

    # overriding
    def info_rekening(self):
        print("=== REKENING BISNIS ===")
        print("Nomor Rekening :", self.NomorRekening)
        print("Pemilik        :", self.nasabah.nama)
        print("Saldo          :", self._saldo)
        print("Limit Transfer :", self.limit_transfer)


# CLASS TRANSAKSI
class Transaksi:
    NamaBank = "Bank Terserah"
    TotalTransaksi = 0
    BiayaTransaksi = 2500

    def __init__(self, id_transaksi, rekening, jenis, nominal):
        self.IdTransaksi = id_transaksi
        self.rekening = rekening
        self.Jenis = jenis
        self.Nominal = nominal
        Transaksi.TotalTransaksi += 1

    def TampilkanTransaksi(self):
        print("ID Transaksi :", self.IdTransaksi)
        print("Rekening     :", self.rekening.NomorRekening)
        print("Jenis        :", self.Jenis)
        print("Nominal      :", self.Nominal)

    @staticmethod
    def ValidasiJenis(jenis):
        jenis_valid = [
            "Setor Tunai",
            "Tarik Tunai",
            "Transfer",
            "Terima Transfer"
        ]
        return jenis in jenis_valid
    
#NASABAH
nasabah1 = Nasabah(
    "Ahmad",
    "6471000000000001",
    "123456"
)

nasabah2 = Nasabah(
    "Rizky",
    "6471000000000002",
    "654321"
)

print("=== DATA NASABAH ===")
print("Nama :", nasabah1.nama)
print("NIK  :", nasabah1.nik)
print()
print("Nama :", nasabah2.nama)
print("NIK  :", nasabah2.nik)

#REKENING  
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

# agregasi
nasabah1.tambah_rekening(rekening1)
nasabah2.tambah_rekening(rekening2)

# info rekening
print()
rekening1.info_rekening()

print()
rekening2.info_rekening()

#transaksi setor tunai
print()
print("=== SETOR TUNAI ===")

rekening1.setor_tunai(200_000)

print("Saldo rekening 1 :", rekening1._saldo)

# tarik tunai
print()
print("=== TARIK TUNAI ===")

rekening2.tarik_tunai(500_000)

print("Saldo rekening 2 :", rekening2._saldo)

#transfer
print()
print("=== TRANSFER ===")

rekening1.transfer(rekening2, 300_000)

print("Saldo rekening 1 :", rekening1._saldo)
print("Saldo rekening 2 :", rekening2._saldo)

# data transaksi
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

# komposisi
rekening1.tambah_transaksi(transaksi1)
rekening2.tambah_transaksi(transaksi2)

print()
print("=== DATA TRANSAKSI ===")

transaksi1.TampilkanTransaksi()

print()

transaksi2.TampilkanTransaksi()
print()
print("=== VALIDASI TRANSAKSI ===")

print(
    "Transfer valid :",
    Transaksi.ValidasiJenis("Transfer")
)

print(
    "Pembayaran valid :",
    Transaksi.ValidasiJenis("Pembayaran")
)

print()
print("=== BIAYA ADMIN ===")

print("Biaya admin :", Rekening.BiayaAdmin)

Rekening.BiayaAdmin = 7500

print("Biaya admin setelah diubah :", Rekening.BiayaAdmin)

# totalan data
print()
print("=== TOTAL DATA ===")

print("Total Nasabah   :", Nasabah.TotalNasabah)
print("Total Rekening  :", Rekening.TotalRekening)
print("Total Transaksi :", Transaksi.TotalTransaksi)