#MENAMPILKAN ADN MENGGANTI DATA DALAM TUPLE
#Tuple tidak bisa dirubah sehingga jika ingin megganti isinya harus diubah daj=hulu menjadi list

data = [ #list of tupple
    (100, "Bambang", 3.76), (97, "Chanyeol", 2.12), (85, "Baek",1.23), (90,"Sehun", 0.86)]

#tampilkan jumlah orang 
print (f"Ada {len(data)} orang")

#tampilkan dengan urutan nomor
data.sort (key=lambda x: x[1]) #artinya data diurutkan  berdasarkan namanya dahulu karena pada indx 1 berisi nama 
print (data)

#ascending default (berdaarkan nilai)
data.sort() #default ascnding, pakai key index 0
print (data)

#urutkan berdasarkan ipk terbaik
data.sort(key=lambda x: x[2], reverse=True) #descending, pakai key index ke 2
print (data)
    
#tampilkan data dengan urutan nama


#tampilkan data lengkap bernama wati
print (data[1]) #data yang diambil dari pengurutan yang terakhir
#menemtukan ipk wati
print (data[1][2])

#menambahkan Joni
data.append((99,"Joni",4.0))

#urutkan berdasarkan ipk
data.sort(key=lambda x: x[2]) #ascending berdasarkan ipk
print (data)

#siapkan data agus yang baru
bambang = (102, "Bambang", 3.0)

#hapus agus dalam list
del data[0]

#masukkan bamabng yang baru ke dalm list
data.append(bambang)

#urutkan berdasarkan ipk
data.sort(key=lambda x: x[2])
print (data)

