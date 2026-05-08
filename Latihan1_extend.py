import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def bubble_sort_extended(data):
    n = len(data)
    total_count = 0

    for i in range(n):
        swapped = False
        print(f"\nIterasi {i+1}:")
        
        for j in range(0, n - i - 1):
            total_count += 1
            print(f"Bandingkan {data[j]} dengan {data[j+1]}")
            
            if data[j] > data[j + 1]:
                print("→ Tukar")
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
            else:
                print("→ Tidak tukar")
        
        print("Hasil sementara:", data)

        # 🔥 OPTIMASI: kalau tidak ada pertukaran, berhenti
        if not swapped:
            print("Data sudah urut, berhenti lebih awal!")
            break

    return data, total_count


data = [5, 2, 9, 1, 5, 6]
hasil, langkah = bubble_sort_extended(data.copy())

print("\nHasil akhir:", hasil)
print("Jumlah perbandingan:", langkah)