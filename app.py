import os
from tracker import RekapKelas, build_markdown_report, save_text

DATA_DIR, OUT_DIR = 'data', 'out'
GRADES_CSV, ATTENDANCE_CSV = os.path.join(DATA_DIR, 'grades.csv'), os.path.join(DATA_DIR, 'attendance.csv')
REPORT_MD = os.path.join(OUT_DIR, 'report.md')

def muat_data(rekap):
    try:
        with open(GRADES_CSV, 'r') as f:
            for baris in f:
                if baris.strip():
                    nim, nama, q, t, uts, uas = baris.strip().split(',')
                    rekap.tambah_mahasiswa(nim, nama)
                    rekap.set_penilaian(nim, float(q), float(t), float(uts), float(uas))
        with open(ATTENDANCE_CSV, 'r') as f:
            for baris in f:
                if baris.strip():
                    nim, hadir = baris.strip().split(',')
                    rekap.set_hadir(nim, float(hadir))
        print("Data berhasil dimuat.")
    except FileNotFoundError:
        print("Error: File CSV tidak ditemukan.")

def simpan_ke_csv(rekap):
    semua_baris_nilai = []
    semua_baris_hadir = []
    for nim, data in rekap.data_mahasiswa.items():
        mhs, nilai = data['mhs'], data['nilai']
        semua_baris_nilai.append(f"{mhs.nim},{mhs.nama},{nilai.quiz},{nilai.tugas},{nilai.uts},{nilai.uas}")
        semua_baris_hadir.append(f"{mhs.nim},{mhs.hadir_persen}")
    with open(GRADES_CSV, 'w') as f: f.write('\n'.join(semua_baris_nilai))
    with open(ATTENDANCE_CSV, 'w') as f: f.write('\n'.join(semua_baris_hadir))
    print("Data terbaru berhasil disimpan ke CSV.")

rekap_manager = RekapKelas()
while True:
    print("\nMenu:")
    print("1. Muat Data")
    print("2. Tambah Mahasiswa")
    print("3. Ubah Presensi")
    print("4. Ubah Nilai")
    print("5. Lihat Rekap")
    print("6. Simpan Laporan")
    print("7. Keluar")
    pilihan = input("Pilih : ")

    if pilihan == '1': muat_data(rekap_manager)

    elif pilihan == '2':
        nim, nama = input("NIM: "), input("Nama: ")
        rekap_manager.tambah_mahasiswa(nim, nama)
        rekap_manager.set_penilaian(nim, 0,0,0,0)
        rekap_manager.set_hadir(nim, 0)

    elif pilihan == '3':
        nim = input("NIM: ")
        if nim in rekap_manager.data_mahasiswa:
            hadir = float(input("Persen kehadiran baru: "))
            rekap_manager.set_hadir(nim, hadir)

    elif pilihan == '4':
        nim = input("NIM: ")
        if nim in rekap_manager.data_mahasiswa:
            q,t,uts,uas = float(input("Quiz: ")), float(input("Tugas: ")), float(input("UTS: ")), float(input("UAS: "))
            rekap_manager.set_penilaian(nim, q, t, uts, uas)

    elif pilihan == '5':
        records = rekap_manager.rekap()
        for r in records: print(f"{r['nim']} | {r['nama']} | Hadir: {r['hadir']}% | Nilai Akhir: {r['nilai_akhir']} | Predikat: {r['predikat']}")
    
    elif pilihan == '6':
        if not os.path.exists(OUT_DIR): os.makedirs(OUT_DIR)
        report_content = build_markdown_report(rekap_manager.rekap())
        save_text(REPORT_MD, report_content)
        simpan_ke_csv(rekap_manager)
    
    elif pilihan == '7':
        print("Selesai."); break
