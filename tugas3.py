'''
Mira
2502383
1A
'''

bilangan = int(input("Masukkan bilangan = "))

jumlah_genap = 0
jumlah_ganjil = 0

for b in range(1, bilangan + 1):
    if b % 2 == 0:
        print(f"{b} adalah bilangan genap")
        jumlah_genap += 1
    else:
        print(f"{b} adalah bilangan ganjil")
        jumlah_ganjil += 1

print("\nJumlah bilangan genap:", jumlah_genap)
print("\nJumlah bilangan ganjil:", jumlah_ganjil)