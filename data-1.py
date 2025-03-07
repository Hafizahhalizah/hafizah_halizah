class Mahasiswa:
    def _init_(self):
        self.nama = "Hafizah Halizah"
        self.rumah = "Poris Gaga"
        self.hobi = "Mendengarkan Musik"
        self.status = "Mahasiswa"
        self.kampus = "Unibang"

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Rumah: {self.rumah}")
        print(f"Hobi: {self.hobi}")
        print(f"Status: {self.status}")
        print(f"Kampus: {self.kampus}")

# Buat objek dan tampilkan data
mhs1 = Mahasiswa()
mhs1.tampilkan_info()