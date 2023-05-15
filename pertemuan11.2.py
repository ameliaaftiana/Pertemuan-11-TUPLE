data = {
    'nama' : 'Maju Jaya',
    'no data': 1,
    'kepada': 'Bambang',
    'barang': [
        (1, 'Penghapus', 1000, 3, 3000), #no, nama, harga satuan, jumlah beli, subtotal
        (2, 'Pengggaris', 2000, 10, 20000),
        # {'no': 3, 'nama _barang':'rautan', 'harga_satuan':4500, 'jumlah_beli':3, 'subtotal':13500}
    ],
}

for key, value in data.items():  #menghasilkan semua key dan value dalam dictionary
    print(f"{key}: {value}")
    
    
#menampilkan data secara terbalik
#misal
klas = 1,2,3,4,5,6
print (klas)
print (klas[::-1]) #[::-1] digunakan untuk membalik data 