'''
Mira
2502383
1A
'''

jhewan = int(input("Jumlah Hewan = "))
hewan = str(input("Nama Hewan (pisahkan nama hewan dengan koma (,) tanpa spasi): "))
nhewan = hewan.split(",")

while len(nhewan) < jhewan:
    nhewan.append("tidak ada")

for h in range(min(jhewan, len(nhewan))):
    print(f"Hewan ke {h+1} adalah: {nhewan[h]}")