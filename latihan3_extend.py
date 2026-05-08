import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

input("\nTekan Enter untuk membersihkan layar...")
clear_screen()

print("Nama: Rifka Aulia Putri")
print("NIM: 552010125015")
print("----------------------------------------------")

def insertion_sort(data):
    count = 0
    geser = 0

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # proses penyisipan
        while j >= 0 and data[j] > key:
            count += 1
            data[j + 1] = data[j]
            geser += 1
            j -= 1

        # jika while berhenti karena kondisi salah
        if j >= 0:
            count += 1

        data[j + 1] = key

        print(f"Langkah ke-{i}: {data}")

    return data, count, geser


print("=== Program Insertion Sort ===")

# input jumlah data
n = int(input("Masukkan jumlah data: "))

data = []

# input isi data
for i in range(n):
    angka = int(input(f"Masukkan angka ke-{i+1}: "))
    data.append(angka)

print("\nData sebelum sorting:", data)

hasil, langkah, pergeseran = insertion_sort(data.copy())

print("\nData setelah sorting :", hasil)
print("Jumlah perbandingan  :", langkah)
print("Jumlah pergeseran    :", pergeseran)