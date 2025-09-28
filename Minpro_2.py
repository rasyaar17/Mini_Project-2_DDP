# Rasya Aditya Ramadani (Rasya)
# NIM : 2509116082
# Sistem Informasi (C)
#MinPro 2

import pwinput
from prettytable import PrettyTable

# DATA USER
users = {
    "manager":  {"password": "manager123",  "role": "Manager"},
    "karyawan": {"password": "karyawan123", "role": "Karyawan"}
}

# DATA PEMINJAMAN
peminjaman_buku = {}
next_id_list = [1]   
# LOGIN
def login():
    print("="*45)
    print("SISTEM LOGIN PERPUSTAKAAN")
    print("="*45)
    percobaan = 0
    while percobaan < 3:
        u = input("Username : ")
        p = pwinput.pwinput("Password : ")
        if u in users and users[u]["password"] == p:
            print("\nLogin berhasil! Role:", users[u]["role"], "\n")
            return users[u]["role"]
        else:
            print("Username atau password salah!\n")
            percobaan = percobaan + 1
    print("Terlalu banyak percobaan, program berhenti.")
    exit()

# CRUD
def create_data():
    nama  = input("Nama Peminjam : ")
    judul = input("Judul Buku    : ")
    lama  = int(input("Lama Pinjam (hari): "))
    tgl   = input("Tanggal Pinjam (Tgl-Bln-Thun): ")
    
    id_baru = next_id_list[0]
    peminjaman_buku[id_baru] = {
        "nama": nama,
        "judul": judul,
        "lama": lama,
        "tgl_pinjam": tgl,
        "status": "Dipinjam"
    }
    print("Data berhasil ditambahkan dengan ID", id_baru, "\n")
    next_id_list[0] = next_id_list[0] + 1

def read_data():
    if not peminjaman_buku:
        print("Belum ada data peminjaman.\n")
        return
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Judul Buku", "Lama (hari)", "Tanggal Pinjam", "Status"]
    for i, d in peminjaman_buku.items():
        table.add_row([i, d["nama"], d["judul"], d["lama"], d["tgl_pinjam"], d["status"]])
    print(table)
    print()

def update_data():
    try:
        idp = int(input("Masukkan ID yang akan diubah: "))
        if idp not in peminjaman_buku:
            print("ID tidak ditemukan!\n")
            return
        d = peminjaman_buku[idp]
        print("Data lama:", d)
        nama  = input("Nama baru (kosongkan jika tidak diubah): ")
        judul = input("Judul baru (kosongkan jika tidak diubah): ")
        lama  = input("Lama pinjam baru (kosongkan jika tidak diubah): ")
        tgl   = input("Tanggal pinjam baru (kosongkan jika tidak diubah): ")
        if nama: d["nama"] = nama
        if judul: d["judul"] = judul
        if lama: d["lama"] = int(lama)
        if tgl:  d["tgl_pinjam"] = tgl
        print("Data berhasil diupdate!\n")
    except ValueError:
        print("Input angka tidak valid!\n")

def delete_data():
    try:
        idp = int(input("Masukkan ID yang akan dihapus: "))
        if idp in peminjaman_buku:
            konfirmasi = input("Yakin hapus? (Hooh/Gaa): ")
            if konfirmasi == "Hooh":
                del peminjaman_buku[idp]
                print("Data berhasil dihapus.\n")
            else:
                print("Penghapusan dibatalkan.\n")
        else:
            print("ID tidak ditemukan!\n")
    except ValueError:
        print("Input ID harus angka!\n")

def pengembalian():
    try:
        idp = int(input("Masukkan ID peminjaman yang dikembalikan: "))
        if idp not in peminjaman_buku:
            print("ID tidak ditemukan!\n")
            return
        d = peminjaman_buku[idp]
        if d["status"] == "Dikembalikan":
            print("Buku ini sudah dikembalikan.\n")
            return
        hari_total = int(input("Total hari peminjaman sebenarnya: "))
        terlambat  = hari_total - d["lama"]
        if terlambat > 0:
            denda = terlambat * 2500
            print("Terlambat", terlambat, "hari. Denda Rp", denda)
        else:
            print("Dikembalikan tepat waktu, tidak ada denda.")
        d["status"] = "Dikembalikan"
        print("Status buku diperbarui.\n")
    except ValueError:
        print("Input harus angka!\n")

# MENU MANAGER
def menu_manager():
    while True:
        print("===== MENU MANAGER =====")
        print("1. Tambah Data (Create)")
        print("2. Lihat Data  (Read)")
        print("3. Ubah Data   (Update)")
        print("4. Hapus Data  (Delete)")
        print("5. Pengembalian & Denda")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")
        if   pilihan == "1": create_data()
        elif pilihan == "2": read_data()
        elif pilihan == "3": update_data()
        elif pilihan == "4": delete_data()
        elif pilihan == "5": pengembalian()
        elif pilihan == "6": break
        else: print("Pilihan tidak valid!\n")

# MENU KARYAWAN
def menu_karyawan():
    while True:
        print("===== MENU KARYAWAN =====")
        print("1. Tambah Data (Create)")
        print("2. Lihat Data  (Read)")
        print("3. Pengembalian & Denda")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")
        if   pilihan == "1": create_data()
        elif pilihan == "2": read_data()
        elif pilihan == "3": pengembalian()
        elif pilihan == "4": break
        else: print("Pilihan tidak valid!\n")

# MAIN
if __name__ == "__main__":
    role = login()
    if role == "Manager":
        menu_manager()
    else:
        menu_karyawan()
    print("\n Makasih Bosq Sudah ke Perpus Banggeris FKIP UNMUL.")
