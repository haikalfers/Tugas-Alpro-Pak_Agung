"""
Kelas : 2023E
Prodi : D4 Manajemen Informatika
Kelompok 4
Anggota Kelompok
1. Zaidan Dhiya' Ulhaq (23091397152)
2. Alya Faadhilah Putri (23091397153)
3. Haikal Ferdian Saputra (23091397154)
"""
print("WELCOME TO PIZZA HUT WIYUNG")
print("SILAHKAN PILIH MENU")

total_harga = 0
Rupiah = f"Rp {total_harga:,.0f}"
print(
    """
    1. Frankfuter BBQ
    2. Meat Monsta
    3. Super Supreme
    4. Super Supreme Chicken
    """)

topping_pizza = int(input("Pilih Topping Pizza yang diinginkan(piih angka 1-4) : "))
if topping_pizza == 1:
    topping_pizza = "Frankfuter BBQ"
if topping_pizza == 2:
    topping_pizza = "Meat Monsta"
if topping_pizza == 3:
    topping_pizza = "Super Supreme"
if topping_pizza == 4:
    topping_pizza = "Super Supreme Chicken"

print(
    """
    Pilih Crust/ Pinggiran Pizza yang anda mau : 
    1. Pan
    2. StuffedCrust Cheese
    3. StuffedCrust Sausage
    4. Cheesy Bites
    5. Crown Bites
    """)
pilihCrust = int(input("Pilih nomor crust yang ingin kamu pilih (1-5): "))
ukuran = input("Pilih ukuran yang kamu inginkan:\n Personal/Regular/Large (tulis sesuai huruf besar dan kecilnya) : \n")
if pilihCrust == 1:
    pilihCrust = "Pan"
    if ukuran == "Personal":
        total_harga = 43_637
    elif ukuran == "Regular":
        total_harga = 100_910
    elif ukuran == "Large":
        total_harga = 132_728
        
if pilihCrust == 2:
    pilihCrust = "StuffedCrust Cheese"
    if ukuran == "Personal":
        total_harga = 55_455
    elif ukuran == "Regular":
        total_harga = 120_910
    elif ukuran == "Large":
        total_harga = 160_000

if pilihCrust == 3:
    pilihCrust = "StuffedCrust Sausage"
    if ukuran == "Personal":
        total_harga = 52_728
    elif ukuran == "Regular":
        total_harga = 117_273
    elif ukuran == "Large":
        total_harga = 155_455

if pilihCrust == 4:
    pilihCrust = "Cheesy Bites"
    if ukuran == "Personal":
        total_harga = 57_273
    elif ukuran == "Regular":
        total_harga = 123_637
    elif ukuran == "Large":
        total_harga = 164_546   
    
if pilihCrust == 5:
    pilihCrust = "Crown Bites"
    if ukuran == "Personal":
        total_harga = 55_455
    elif ukuran == "Regular":
        total_harga = 120_910
    elif ukuran == "Large":
        total_harga = 160_000    
    
extra_cheese = input("Apakah Anda Mau menambahkan Keju (y/n) : ").lower()
while extra_cheese not in ["y", "n"]:
    extra_cheese = input("Apakah Annda Mau menambahkan Keju (y/n) : ").lower()
if extra_cheese == "y":
    total_harga += 13_636
    extra_cheese =True
elif extra_cheese == "n":
    extra_cheese = False


print("\nTerima Kasih telah membeli di Pizza Hut")
print(f"\nPesanan Anda\nPizza Dengan Topping {topping_pizza}")
print(f"Menggunakan Crust {pilihCrust}")
print(f"Dengan Ukuran {ukuran}")
print(f"{'dengan'if extra_cheese else 'tanpa'} Tambahan Keju")
print("Jadi untuk seluruhnya")
print(f"Total Bill anda adalah Rp{total_harga}")
print("\nSilahkan Bayar Bill kamu di kasir, TERIMA KASIH!!!")
