# Continue, Pass, and Break

# MMULAI Pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi

# angka = 0

# while angka < 10:

#    angka += 1
#    if angka == 5:

#        pass # ini tidak akan dieksekusi

#    print(angka)

# MEMULAI CONTINUE
#angka = 0

#print(f"angka sekarang = {angka}")

#while angka < 10:
#    angka += 1
#    print(f"angka sekarang = {angka}") # aksi 1

#   if angka == 5:
#        print("Kelana")
#        continue    # ini akan membuat loop meloncat ke step selanjutnya

#    print("Halo") # aksi 2

#print("Selesai")

# MEMULAI BREAK 
# CONTOH BREAK 1


angka = 0

while angka < 10:
    angka += 1
    print (f"count = {angka}")

    if angka == 5:
        print("Kelana")

        break

    print("Halo")

print("Selesai")
print("================ \n")

# CONTOH BREAK 2

data_int = int(input("Hitung sampai = "))

angka = 0

while True:
    angka += 1
    print (f"count = {angka}")

    if angka == data_int:
        print("Kelana")

        break

    print("Halo")

print("Selesai")