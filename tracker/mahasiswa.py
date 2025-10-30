class Mahasiswa:

    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self._hadir_persen = 0

    @property
    def hadir_persen(self):
        return self._hadir_persen
    
    @hadir_persen.setter
    def hadir_persen(self, nilai):
        if 0 <= nilai <= 100:
            self._hadir_persen = float(nilai)
        else:
            print("Error: Persentase kehadiran harus antara 0 dan 100.")
