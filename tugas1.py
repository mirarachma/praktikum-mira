'''
Mira
2502383
1A
'''

for i in range(1, 51):
    if i % 5 == 0:
        print("pass")
        count_pass += 1
    else:
        print(i, end=" ")

print("\nJumlah 'pass' muncul sebanyak:", count_pass)
