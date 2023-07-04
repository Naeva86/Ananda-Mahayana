def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

input_str = input("Masukkan elemen-elemen data dalam urutan terurut (pisahkan dengan spasi): ")
arr = list(map(int, input_str.split()))

x = int(input("Masukkan data yang ingin dicari: "))

hasil = binary_search(arr, 0, len(arr)-1, x)

if hasil != -1:
    print("Elemen ditemukan pada indeks ke-", str(hasil))
else:
    print("Elemen tidak ditemukan")
