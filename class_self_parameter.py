class Pesanan:
    def __init__(self, menu, porsi):
        self.menu = menu
        self.porsi = porsi

    def total(self, harga):
        return self.porsi * harga

    def tambah_porsi(self, jumlah):
        self.porsi += jumlah

pesanan1 = Pesanan("seblak", 2)
print(pesanan1.total(12000))
pesanan1.tambah_porsi(1)
print(pesanan1.porsi)
print(pesanan1.total(12000))