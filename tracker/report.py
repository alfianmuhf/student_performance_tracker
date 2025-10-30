def build_markdown_report(records):
    header = "| NIM       | Nama   | Hadir (%) | Nilai Akhir | Predikat |\n"
    separator = "|-----------|--------|-----------|-------------|----------|\n"
    body = ""
    for rec in records:
        body += f"| {rec['nim']} | {rec['nama']}  | {rec['hadir']:.1f} | {rec['nilai_akhir']:.2f} | {rec['predikat']} |\n"
    return f"# Rekap Nilai Mahasiswa\n\n{header}{separator}{body}"

def save_text(path, content):
    with open(path, 'w') as file:
        file.write(content)
    print(f"Laporan berhasil disimpan di: {path}")
