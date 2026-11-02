def input_angka(message):
    while True:
        try:
            nilai = int(input(message))
            if nilai <= 0:
                print("Nilai harus lebih dari 0, coba lagi.")
                continue
            return nilai
        except ValueError:
            print("Input harus berupa bilangan bulat, coba lagi.")

def rupiah(angka):
    teks = f"{angka:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return "Rp" + teks

nama_barang = input("Masukkan nama barang  : ")
harga_satuan = input_angka("Masukkan harga satuan : ")
jumlah_barang = input_angka("Masukkan jumlah barang: ")

subtotal = harga_satuan * jumlah_barang
ppn = subtotal * 0.11
total_bayar = subtotal + ppn

print(f"Subtotal {rupiah(subtotal)}, PPN {rupiah(ppn)}, Total {rupiah(total_bayar)}")
