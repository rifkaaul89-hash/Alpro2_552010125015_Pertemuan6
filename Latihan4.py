import random

# INSERTION SORT
def insertion_sort(data):
    count = 0

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            count += 1
            data[j + 1] = data[j]
            j -= 1

        if j >= 0:
            count += 1

        data[j + 1] = key

    return count


# BUBBLE SORT
def bubble_sort(data):
    count = 0
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            count += 1

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return count


# SELECTION SORT
def selection_sort(data):
    count = 0
    n = len(data)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            count += 1

            if data[j] < data[min_index]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]

    return count


# DATA UJI
data6 = [6, 5, 4, 3, 2, 1]
data10 = random.sample(range(1, 50), 10)
data20 = random.sample(range(1, 100), 20)

# TABEL HASIL
print("==============================================")
print("Jumlah Data | Bubble | Selection | Insertion")
print("==============================================")

b6 = bubble_sort(data6.copy())
s6 = selection_sort(data6.copy())
i6 = insertion_sort(data6.copy())
print(f"6            | {b6:^6} | {s6:^9} | {i6:^9}")

b10 = bubble_sort(data10.copy())
s10 = selection_sort(data10.copy())
i10 = insertion_sort(data10.copy())
print(f"10           | {b10:^6} | {s10:^9} | {i10:^9}")

b20 = bubble_sort(data20.copy())
s20 = selection_sort(data20.copy())
i20 = insertion_sort(data20.copy())
print(f"20           | {b20:^6} | {s20:^9} | {i20:^9}")

print("==============================================")

# CHALLENGE
print("\n=== Challenge Insertion Sort ===")

# data hampir terurut
hampir_urut = [1, 2, 3, 5, 4, 6, 7, 8]

# data acak
acak = [8, 3, 1, 6, 2, 7, 5, 4]

hasil_hampir = insertion_sort(hampir_urut.copy())
hasil_acak = insertion_sort(acak.copy())

print("\nData hampir terurut :", hampir_urut)
print("Jumlah perbandingan :", hasil_hampir)

print("\nData acak           :", acak)
print("Jumlah perbandingan :", hasil_acak)

# ANALISIS
print("\n=== Analisis ===")
if hasil_hampir < hasil_acak:
    print("Insertion Sort lebih cepat pada data hampir terurut.")
else:
    print("Insertion Sort tidak lebih cepat.")