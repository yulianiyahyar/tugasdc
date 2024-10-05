"""
Index yang tersusun rapih

ada array yang berisi ['T', 'E', 'C', 'H', 'N', 'O', 'C', 'L', 'U', 'B'].
guru meminta agar tulisan C saja yang ditampilkan ke dalam layar.
penuhi permintaan guru tersebut.

Contoh
Input:
['T', 'E', 'C', 'H', 'N', 'O', 'C', 'L', 'U', 'B']

Output:
C C
"""
tech = ['T', 'E', 'C', 'H', 'N', 'O', 'C', 'L', 'U', 'B']

# lanjutkan code dibawah ini

sorted_tech = sorted(tech)
duplicates = [char for char in sorted_tech if sorted_tech.count(char)>1]
print("Karakter yang muncul lebih dari sekali:")
for char in duplicates:
    print(char, end='')