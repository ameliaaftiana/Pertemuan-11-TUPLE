#list

def tiga_nilai_terbaik(daftar_nilai): #hasilnya tuple (a,b,c)
    #urutkan secara descending 
    daftar_nilai.sort(reverse=True) #urutkan secara descending
    hasil = tuple(daftar_nilai[:3]) #ambil tiga yang terdepan, [:3] adalah slicing artinya diambil 3 yang palig depan
    return hasil

#input user
n = 0
while n < 3:
    n = int(input("Masukkan n(minimal 3): "))

data = []
for i in range(n):
    nilai = int(input("Masukkan nilai: "))
    data.append(nilai)
    
#proses
hasil = tiga_nilai_terbaik(data) #hasilnya tuple (a,b,c)

#output
print (f"1. {hasil[0]}\n2. {hasil[1]}\n3. {hasil[2]}")
print (f"Nilai maksimumnya adalah {max(hasil)}")
print (f"Nilai minimumnya adalah {min(hasil)}")