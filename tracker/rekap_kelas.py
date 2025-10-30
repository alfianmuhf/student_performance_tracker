from .mahasiswa import Mahasiswa
from .penilaian import Penilaian
class RekapKelas:
    def __init__(self):
        self.data_mahasiswa = {}

    def tambah_mahasiswa(self, nim, nama):
        if nim not in self.data_mahasiswa:
            self.data_mahasiswa[nim] = {'mhs': Mahasiswa(nim, nama), 'nilai': Penilaian()}
        else:
            print(f"Error: NIM {nim} sudah ada.")

    def set_hadir(self, nim, persen):
        if nim in self.data_mahasiswa:
            self.data_mahasiswa[nim]['mhs'].hadir_persen = persen

    def set_penilaian(self, nim, quiz, tugas, uts, uas):
        if nim in self.data_mahasiswa:
            n = self.data_mahasiswa[nim]['nilai']
            n.quiz, n.tugas, n.uts, n.uas = quiz, tugas, uts, uas

    def predikat(self, nilai_akhir):
        if nilai_akhir >= 85: return 'A'
        elif nilai_akhir >= 75: return 'B'
        elif nilai_akhir >= 60: return 'C'
        elif nilai_akhir >= 50: return 'D'
        else: return 'E'
        
    def rekap(self):
        daftar_rekap = []
        for nim, data in self.data_mahasiswa.items():
            mhs, nilai = data['mhs'], data['nilai']
            nilai_final = nilai.nilai_akhir()
            predikat_mhs = self.predikat(nilai_final)
            daftar_rekap.append({'nim': mhs.nim, 'nama': mhs.nama, 'hadir': mhs.hadir_persen, 'nilai_akhir': round(nilai_final, 2), 'predikat': predikat_mhs})
        return daftar_rekap
