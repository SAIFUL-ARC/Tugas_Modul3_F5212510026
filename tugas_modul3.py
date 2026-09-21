# Nama : Saiful
# NIM  : F5212510026
# Kelas: SI-A


print("=== KALKULATOR LINGKARAN SEDEERHANA ===")

print("== Menu ==")
print("1. Luas Lingkaran")
print("2. Panjang Diameter")
print("3. Keliling Lingkaran")
print("4. Luas bola")


jari2    = float(input("Masukkan Jari-jari: "))
masukkan = int(input("Masukkan Rumus yang diinginkan: "))

if masukkan == 1:
    luas = 3.14 * jari2**2
    print(" Jawabannya adalah :", luas )

elif masukkan == 2:
    Diameter = 2 * jari2
    print(" Jawabannya adalah :", Diameter)

elif masukkan == 3 :
    keliling = 2 * 3.14 * jari2
    print(" Jawabannya adalah :", keliling)

elif masukkan == 4:
    bola = (4/3) * 3.14 * jari2**3
    print(" Jawabannya adalah :", bola)

else:
    print("Menu tidak tersedia, harap masukkan angka yang benar!!!")
