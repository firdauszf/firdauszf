# Firdaus Zamroni Fauzi
# JCDS - 0212
# Purwadhika On Campus Surabaya

# Deklarasi Buku
daftar_buku = {
    "COMP-001" : {"Judul" : "Programming with Python", 
                  "Penulis" : "Arnold Costa", "Stok" : 2, 
                  "Genre" : "Science", "Status" : "Tersedia"},
    "COMP-002" : {"Judul" : "Implementation R", 
                  "Penulis" : "Natasha Angel", "Stok" : 1, 
                  "Genre" : "Science", "Status" : "Tersedia"},                
    "LIF-001" : {"Judul" : "Create a Good Relationship", 
                  "Penulis" : "Taufik Mubarak", "Stok" : 1, 
                  "Genre" : "Romance", "Status" : "Tersedia"},             
    "LIF-002" : {"Judul" : "Definition of True Love", 
                  "Penulis" : "Rizdin Fahrezi", "Stok" : 2, 
                  "Genre" : "Romance", "Status" : "Tersedia"},
    "FAN-001" : {"Judul" : "Journey to Atlantis", 
                  "Penulis" : "Jason Mamoa", "Stok" : 1, 
                  "Genre" : "Fantasy", "Status" : "Tersedia"},
    "FAN-002" : {"Judul" : "Hello Heaven !", 
                  "Penulis" : "Mark Harley", "Stok" : 1, 
                  "Genre" : "Fantasy", "Status" : "Tersedia"}              
}

def daftar_lengkap():
    while True:
        if daftar_buku:
            print("\n Daftar Buku Perpustakaan Suroboyo :")
            print("-" * 110)
            print(f"|{"Kode Buku":^10} | {"Judul":^27} | {"Penulis":^20} | {"Stok":^10} | {"Genre":^10} | {"Status":^14} |")
            print("-" * 110)

            for kode_buku, buku_info in daftar_buku.items():
                print(f"|{kode_buku:^10} | {buku_info["Judul"]:^27} | {buku_info["Penulis"]:^20} | {buku_info["Stok"]:^10} | {buku_info["Genre"]:^10} | {buku_info["Status"]:^14} |")
            print("-" * 110)
            break

buku_dipinjam = []
def lend_book():
    daftar_lengkap()
    kode_buku = input("\nMasukkan Kode Buku untuk dipinjam : ").upper()
    if kode_buku in daftar_buku and daftar_buku[kode_buku]["Stok"] > 0:
        nama_pembaca = input("Masukkan nama pembaca: ").title()
        id_pembaca = input("Masukkan ID pembaca : ")

        if nama_pembaca:
            daftar_buku[kode_buku]["Pembaca"] = nama_pembaca
            daftar_buku[kode_buku]["ID Pembaca"] = id_pembaca
            daftar_buku[kode_buku]["Stok"] -= 1

            if daftar_buku[kode_buku]["Stok"] == 0:
                daftar_buku[kode_buku]["Status"] = "Habis"

            print(f"\nBuku berhasil dipinjam ke {nama_pembaca} {id_pembaca}.")
            buku_dipinjam.append({"Kode Buku" : kode_buku, "Pembaca" : nama_pembaca, "ID Pembaca" : id_pembaca})
        else:
            print("Nama tidak boleh kosong. input nama yang valid.")
    elif kode_buku in daftar_buku and daftar_buku[kode_buku]["Stok"] == 0:
        print("\nMaaf buku sudah habis, cek lagi nanti.")
    else:
        print("\nKode Buku tidak ditemukan. Masukkan Kode Buku yang benar.")

def return_book():
    daftar_lengkap()
    kode_buku = input("\n Masukkan Kode Buku yang dikembalikan: ").upper()
    if kode_buku in daftar_buku:
        nama_pembaca = input("Masukkan nama pembaca: ").title()
        id_pembaca = input("Masukkan ID pembaca : ")
        if daftar_buku[kode_buku].get("Pembaca").title() == nama_pembaca and daftar_buku[kode_buku].get("ID Pembaca") == id_pembaca:
            daftar_buku[kode_buku]["Stok"] += 1

            if daftar_buku[kode_buku]["Stok"] > 0:
                daftar_buku[kode_buku]["Status"] = "Tersedia"
            
            for book in buku_dipinjam:
                if book in buku_dipinjam:
                    if book['Kode Buku'] == kode_buku and book["Pembaca"] == nama_pembaca:
                        buku_dipinjam.remove(book)
            print(f"\nBuku berhasil dikembalikan oleh {nama_pembaca}.")

        else:
            print("\nNama peminjam salah. Silahkan input nama yang benar.")
    elif kode_buku in daftar_buku and daftar_buku[kode_buku]["Stok"] == "Tersedia":
        print("\nBuku ini sedang tidak dipinjam. silahkan cek kembali Kode Buku.")
    else:
        print("\nKode Buku tidak ditemukan. Silahkan input Kode Buku dengan benar.")

def view_books():
    daftar_lengkap()
    print("1. Kembali ke Menu Utama")
    pilih_opsi = input("Masukkan angka 1 untuk kembali ke menu utama: ")
    while True:
        if pilih_opsi == "1":
            break
        else:
            print("Opsi tidak valid. Silahkan pilih opsi yang ada")
            

def edit_book():
    daftar_lengkap()
    kode_buku = input("Masukkan Kode Buku yang ingin diedit: ").upper()
    if kode_buku in daftar_buku:
        print(f"\nEdit Kode Buku : {kode_buku}")
        print("1. Edit Judul")
        print("2. Edit Penulis")
        print("3. Edit Stok")
        print("4. Edit Genre")
        print("5. Kembali ke Menu Utama")

        edit_opsi = input("\nPilih Opsi (1/2/3/4/5): ")

        if edit_opsi == "1":
            judul_baru = input("Masukkan baru Judul: ").title()
            daftar_buku[kode_buku]["Judul"] = judul_baru
            print("\nJudul Berhasil di Update.")
        elif edit_opsi == "2":
            penulis_baru = input("Masukkan penulis baru: ").title()
            daftar_buku[kode_buku]["Penulis"] = penulis_baru
            print("\nPenulis berhasil diupdate.")
        elif edit_opsi == "3":
            while True:
                stok_baru = int(input("Masukkan stok baru: "))
                if stok_baru == 0 or stok_baru == 1:
                    daftar_buku[kode_buku]["Stok"] = stok_baru
                    if stok_baru == 0:
                        daftar_buku[kode_buku]["Status"] = "Habis"
                    print("\nStok berhasil di Update.")
                    break
                else:
                    print("Jumlah harus 0 atau 1. ")
        elif edit_opsi == "4":
            genre_baru = input("Masukkan genre baru: ").title()
            daftar_buku[kode_buku]["Genre"] = genre_baru
            print("\nGenre berhasil diUpdate.")
        elif edit_opsi == "5":
            print("\nKembali Ke Menu Utama.")
        else:
            print("\nOpsi tidak valid. kembali ke menu utama.")
    else:
        print("\nKode Buku tidak ditemukan. Silahkan masukkan kode buku ulang  .")

def view_borrowed_books():
    while True:
        if buku_dipinjam:
            print("\nBuku yang Dipinjam.")
            print("-"*80)
            print(f"| {"Kode Buku":^10} | {"Judul":^27} | {"Dipinjam":^20} | {"ID Pembaca" :^10} |")
            print("-"*80)

            for book in buku_dipinjam:
                kode_buku = book.get("Kode Buku")
                Judul = daftar_buku.get(kode_buku).get("Judul")
                Pembaca = book.get("Pembaca")
                id_pembaca = book.get("ID Pembaca")

                print(f"| {kode_buku :^10} | {Judul :^27} | {Pembaca :^20} | {id_pembaca :^10} |")
            print("-" * 80)
            print("1. Kembalikan ke Buku")
            print("2. Kembali Ke Menu Utama")
            pilih_opsi = input("Pilih Opsi (1/2): ")

            if pilih_opsi == "1":
                return_book()
            elif pilih_opsi == "2":
                break
            else:
                print("Opsi tidak valid. Pilih opsi yang ada")
        
        else:
            print("\nSaat ini tidak ada buku yang di pinjam.")
            break
def add_book():
    daftar_lengkap()
    kode_buku = input("\nMasukkan Kode Buku: ").upper()
    Judul = input("\nMasukkan Judul Buku: ").title()
    penulis = input("\nMasukkan Penulis: ").title()

    while True:
        stock = int(input("Masukkan Stok: "))
        if stock >= 0:
            break
        else:
            print("Masukkan stok ulang.")
    if stock == 0:
        status ="Habis"
    else:
        status = "Tersedia"
    genre = input("Masukkan Genre: ")
    konfirmasi = input(f"\nApakah kamu yakin menambahkan'{Judul}' pada daftar_buku ? (Y/N): ").lower()

    if konfirmasi == "y":
        daftar_buku[kode_buku] = {"Judul" : Judul, "Penulis" : penulis, "Stok" : stock, "Genre" : genre, "Status" : status}
        print("\nBuku berhasil ditambahkan. Buku ini tersedia untuk pembaca.")
    else:
        print("\nPenambahan dibatalkan")

def delete_book():
    daftar_lengkap()
    kode_buku = input("\nMasukkan Kode Buku yang ingin dihapus: ").upper()
    if kode_buku in daftar_buku:
        konfirmasi = input(f"\nApakah kamu yakin untuk menghapus '{daftar_buku[kode_buku]['Judul']}' dari daftar_buku? (Y/N):").lower()

        if konfirmasi == "y":
            del daftar_buku[kode_buku]
            print("\nBuku berhasil dihapus dari daftar buku.")
        else:
            print("\nHapus Buku dibatalkan.")
    else:
        print("\nKode Buku tidak ditemukan. Silahkan masukkan Kode Buku yang benar.")

def first_display():
    while True:
        print("-" * 43)
        print("| SELAMAT DATANG DI PERPUSTAKAAN SUROBOYO |")
        print("-" * 43)
        print("Anda sebagai apa")
        print("1. Admin")
        print("2. Peminjam")
        print("3. Keluar")

        pilih_user = input('Masukan angka menu yang diinginkan: ')

        if pilih_user == '1':
            user_admin()
        elif pilih_user == '2':
            user_peminjam()
        elif pilih_user == '3':
            print('Terimakasih')
            break
        else:
            print('Angka menu yang anda masukan tidak tersedia, silahkan masukkan angka dengan benar.')
            continue

def admin():
    while True:
        print("-" * 43)
        print("| SELAMAT DATANG DI PERPUSTAKAAN SUROBOYO |")
        print("-" * 43)
        print("1. Tampilkan Daftar Buku")
        print("2. Tampilkan Buku yang Dipinjam")
        print("3. Tambahkan Buku Baru")
        print("4. Edit Buku")
        print("5. Menghapus Buku")
        print("6. Kembali ke menu utama admin")
        pilih_opsi = input("\nPilih Opsi (1/2/3/4/5/6): ")

        if pilih_opsi == "1":
            view_books()
        elif pilih_opsi == "2":
            view_borrowed_books()
        elif pilih_opsi == "3":
            add_book()
        elif pilih_opsi == "4":
            edit_book()
        elif pilih_opsi == "5":
            delete_book()
        elif pilih_opsi == "6":
            print("Anda kembali ke menu utama admin")
            break
        else:
            print("\nOpsi tidak valid. Pilih opsi yang ada.")
            continue
def peminjam():
    while True:
        print("-" * 43)
        print("| SELAMAT DATANG DI PERPUSTAKAAN SUROBOYO |")
        print("-" * 43)
        print("1. Pinjam Buku")
        print("2. Kembalikan Buku")
        print("3. Tampilkan Daftar Buku")
        print("4. Kembali ke menu utama peminjam")
        pilih_opsi = input("\nPilih Opsi (1/2/3/4): ")

        if pilih_opsi == "1":
            lend_book()
        elif pilih_opsi == "2":
            return_book()
        elif pilih_opsi == "3":
            view_books()
        elif pilih_opsi == "4":
            print("\n Kembali ke menu utama peminjam")
            break
        else:
            print("\nOpsi tidak valid. Pilih opsi yang ada.")

username_admin = "admin"
password_admin = "admin123"
username_peminjam = "roni"
password_peminjam = "roni123"
def user_admin():
    username = input("Masukkan username anda: ")
    while True:
        if username == username_admin:
            input_password = input("Masukkan password anda: ")
            if input_password == password_admin:
                admin()
            else:
                print("password yang anda masukkan salah, ulangi")
            break
        else:
            print("Anda bukan admin, silahkan masuk ke menu peminjam")
            break
def user_peminjam():
    username = input("Masukkan username anda: ")
    while True:
        if username == username_peminjam:
            input_password = input("Masukkan password anda: ")
            if input_password == password_peminjam:
                peminjam()
            else:
                print("password yang anda masukkan salah, ulangi")
            break
        else:
            print("Anda adalah admin, silahkan masuk kemenu admin")
            break
    
first_display()



    