"""
Kelas : 2023E
Prodi : D4 Manajemen Informatika
Kelompok 4
Anggota Kelompok
1. Zaidan Dhiya Ulhaq (23091397152)
2. Alya Faadhilah Putri (23091397153)
3. Haikal Ferdian Saputra (23091397154)
"""

total_harga : 0

print(
    """
    1. Frankfuter BBQ
    2. Meat Monsta
    3. Super Supreme
    4. Super Supreme Chicken
    """)

topping_pizza = int(input("Pilih Topping Pizza (piih angka): "))
if topping_pizza == 1:
    topping_pizza = "Frankfuter BBQ"
if topping_pizza == 2:
    topping_pizza = "Meat Monsta"
if topping_pizza == 3:
    topping_pizza = "Super Supreme"
if topping_pizza == 4:
    topping_pizza = "Super Supreme Chicken"
