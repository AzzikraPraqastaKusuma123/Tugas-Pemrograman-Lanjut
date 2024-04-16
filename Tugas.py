def hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas):
    nilai_akhir = (0.25 * nilai_tugas) + (0.35 * nilai_uts) + (0.40 * nilai_uas)
    return nilai_akhir

def konversi_nilai(nilai_akhir):
    if nilai_akhir > 85:
        return "A"
    elif 80 <= nilai_akhir <= 85:
        return "A-"
    elif 75 <= nilai_akhir < 80:
        return "B+"
    elif 70 <= nilai_akhir < 75:
        return "B"
    elif 65 <= nilai_akhir < 70:
        return "B-"
    elif 60 <= nilai_akhir < 65:
        return "C+"
    elif 55 <= nilai_akhir < 60:
        return "C"
    elif 50 <= nilai_akhir < 55:
        return "C-"
    elif 30 <= nilai_akhir < 50:
        return "D"
    else:
        return "E"

print("Selamat datang di Aplikasi perhitungan nilai Mahasiswa")

# Nilai tugas, UTS, dan UAS sudah ditentukan sebelumnya
nilai_tugas = 89
nilai_uts = 90
nilai_uas = 90

# Hitung nilai akhir
nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)

# Konversi nilai akhir 
nilai_huruf = konversi_nilai(nilai_akhir)
# Output hasil
print(f"Nilai Tugas Anda: {nilai_tugas}")
print(f"Nilai UTS Anda: {nilai_uts}")
print(f"Nilai UAS Anda: {nilai_uas}")
print(f"Nilai Akhir Anda: {nilai_akhir},\nDalam Huruf {nilai_huruf}")
