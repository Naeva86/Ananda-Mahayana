def merge_sort(list_bilangan):
    jumlah_bilangan = len(list_bilangan)
    if jumlah_bilangan > 1:
        posisi_tengah = len(list_bilangan) // 2
        potongan_kiri = list_bilangan[:posisi_tengah]
        potongan_kanan = list_bilangan[posisi_tengah:]

        merge_sort(potongan_kiri)
        merge_sort(potongan_kanan)

        jumlah_bilangan_kiri = len(potongan_kiri)
        jumlah_bilangan_kanan = len(potongan_kanan)
        c_all, c_kiri, c_kanan = 0, 0, 0  

        while c_kiri < jumlah_bilangan_kiri or c_kanan < jumlah_bilangan_kanan:
            if c_kiri == jumlah_bilangan_kiri: 
                list_bilangan[c_all] = potongan_kanan[c_kanan]
                c_kanan = c_kanan + 1
            elif c_kanan == jumlah_bilangan_kanan:  
                list_bilangan[c_all] = potongan_kiri[c_kiri]
                c_kiri = c_kiri + 1
            elif potongan_kiri[c_kiri] >= potongan_kanan[c_kanan]: 
                list_bilangan[c_all] = potongan_kiri[c_kiri]
                c_kiri = c_kiri + 1
            else: 
                list_bilangan[c_all] = potongan_kanan[c_kanan]
                c_kanan = c_kanan + 1
            c_all = c_all + 1

# Mengubah angka menjadi descending
def merge_sort_descending(list_bilangan):
    merge_sort(list_bilangan)
    list_bilangan.reverse()

data = input("Masukkan Data :")
angka_descending = list(map(int, data.split()))
print('Sebelum sort (descending):', angka_descending)
merge_sort(angka_descending)
print('Setelah sort (descending):', angka_descending)

