def cek_ganjil_genap_dan_kuadrat(nums):
    ganjil = [num for num in nums if num % 2 != 0]
    for num in ganjil:
        print("Nilai:", num, "| Kuadrat:", num ** 2)

if __name__ == "__main__":

    jumlah = int(input("Masukkan jumlah bilangan: "))
    nums = []
    for _ in range(jumlah):
        num = int(input("Masukkan bilangan: "))
        nums.append(num)

    print("Bilangan ganjil dan kuadratnya:")
    cek_ganjil_genap_dan_kuadrat(nums)
