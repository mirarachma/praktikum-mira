'''
Mira
2502383
1A
'''

bilangan = int(input("Masukkan bilangan = "))

for b in range(1, bilangan + 1):
    if b % 2 == 0:
        print(f"{b} adalah bilangan genap")
    else:
        print(f"{b} adalah bilangan ganjil")