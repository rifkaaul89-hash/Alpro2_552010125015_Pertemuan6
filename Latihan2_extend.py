import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def selection_sort(data, tampilkan_proses=False):
    n = len(data)
    count = 0

    for i in range(n):
        min_index = i
        
        if tampilkan_proses:
            print(f"\nIterasi {i+1}:")
        
        for j in range(i+1, n):
            count += 1
            
            if tampilkan_proses:
                print(f"Bandingkan {data[j]} dengan {data[min_index]}")
            
            if data[j] < data[min_index]:
                min_index = j
        
        # swap
        data[i], data[min_index] = data[min_index], data[i]

        if tampilkan_proses:
            print("Hasil sementara:", data)

    return data, count


# ================= MENU =================
while True:
    print("\n=== PROGRAM SELECTION SORT ===")
    print("1. Input & Sorting")
    print("2. Sorting dengan proses")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        data = list(map(int, input("Masukkan data (pisahkan spasi): ").split()))
        hasil, langkah = selection_sort(data.copy())

        print("Hasil:", hasil)
        print("Jumlah perbandingan:", langkah)

        input("Tekan ENTER untuk lanjut...")
        clear_screen()

    elif pilihan == "2":
        data = list(map(int, input("Masukkan data (pisahkan spasi): ").split()))
        hasil, langkah = selection_sort(data.copy(), True)

        print("\nHasil akhir:", hasil)
        print("Jumlah perbandingan:", langkah)

        input("Tekan ENTER untuk lanjut...")
        clear_screen()

    elif pilihan == "3":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")