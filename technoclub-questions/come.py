"""
Membuat Daftar Penumpang

Tugasmu adalah membuat program yang akan mengonversi data penumpang dari input yang diberikan menjadi list of dictionaries. 
Setiap penumpang memiliki tiga atribut: nama, umur, dan asal planet. 
Program harus meminta input untuk setiap atribut penumpang dan menyimpannya dalam dictionary, lalu memasukkan dictionary tersebut ke dalam list.

Contoh
Input:
Jumlah penumpang: 2

Penumpang 1
Nama: Hanif
Umur: 23
Asal planet: Mars

Penumpang 2
Nama: Rani
Umur: 25
Asal planet: Jupiter

Output:
[
    {'nama': 'Hanif', 'umur': 23, 'asal planet': 'Mars'},
    {'nama': 'Rani', 'umur': 25, 'asal planet': 'Jupiter'}
]
"""
penumpang = []
jumlah_penumpang = int(input("Jumlah penumpang: "))

for i in range(jumlah_penumpang):
    nama = input(f"Penumpang {i+1}\nNama: ")
    umur = int(input("Umur: "))
    asal_planet = input("Asal planet: ")
    
    print()
    
    # lanjutkan code dibawah ini
    
print(penumpang)
for idx, p in enumerate(penumpang, start=1):
    print(f"{idx}. Nama: {p['nama']}, Umur: {p['umur']}, Asal Planet: {p,['asal_planet']}")

with open('penumpang.txt','w') as file:
    for p in penumpang:
        file.write(f"Nama: {p['nama']}, Umur: {p['umur']}, Asal Planet: {p,['asal_planet']}Nama: {p['nama']}, Umur: {p['umur']}, Asal Planet: {p,['asal_planet']}\n ")
print("data penumpang telah disimpan ke dalam 'penumpang.txt'.")

cari_nama = input("\Masukkan nama penumpang yang ingin dicari:")
penumpang_ditemukan = [p for p in penumpang if p ['nama'].lower() == cari_nama.lower ()]

if penumpang_ditemukan:
    print("\Penumpang ditemukan:")
    for p in penumpang_ditemukan:
        print(f"Nama: {p['nama']}, Umur: {p['umur']}, Asal Planet: {p,['asal_planet']}Nama: {p['nama']}, Umur: {p['umur']}, Asal Planet: {p,['asal_planet']}")
    else:
        print("Penumpang tidak ditemukan.")