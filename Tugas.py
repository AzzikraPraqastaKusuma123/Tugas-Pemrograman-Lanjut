def hitung_nilai_akhir(tugas, uts, uas):
    nilai_akhir = 0.25 * tugas + 0.35 * uts + 0.4 * uas
    return nilai_akhir

def tentukan_nilai_huruf(nilai_akhir):
    if nilai_akhir > 85:
        return 'A'
    elif nilai_akhir > 80:
        return 'A-'
    elif nilai_akhir > 75:
        return 'B+'
    elif nilai_akhir > 70:
        return 'B'
    elif nilai_akhir > 65:
        return 'B-'
    elif nilai_akhir > 60:
        return 'C+'
    elif nilai_akhir > 55:
        return 'C'
    elif nilai_akhir > 50:
        return 'C-'
    elif nilai_akhir > 30:
        return 'D'
    else:
        return 'E'

def main():
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))

    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    nilai_huruf = tentukan_nilai_huruf(nilai_akhir)

    print("Nilai akhir:", nilai_akhir)
    print("Nilai huruf:", nilai_huruf)

if __name__ == "__main__":
    main()
