class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def perkenalan(self):
        print("Halo, nama saya", self.nama, "dari kelas", self.kelas)

rahma = Siswa("Rahmayanti", "XI RPL B")
print(rahma.nama)
print(rahma.kelas)
rahma.perkenalan()