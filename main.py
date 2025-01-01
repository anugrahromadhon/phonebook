from database import init_db, add_contact, view_contacts, search_contact, delete_contact

def main_menu():
    print("\n=== Aplikasi Catatan Buku Telepon ===")
    print("1. Tambah Kontak")
    print("2. Lihat Semua Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")

def main():
    init_db()
    while True:
        main_menu()
        choice = input("Pilih opsi: ")

        if choice == "1":
            name = input("Nama: ")
            phone = input("Nomor Telepon: ")
            add_contact(name, phone)
            print("Kontak berhasil ditambahkan!")

        elif choice == "2":
            contacts = view_contacts()
            print("\nDaftar Kontak:")
            for contact in contacts:
                print(f"[{contact[0]}] {contact[1]} - {contact[2]}")

        elif choice == "3":
            keyword = input("Masukkan nama atau nomor: ")
            results = search_contact(keyword)
            print("\nHasil Pencarian:")
            for result in results:
                print(f"[{result[0]}] {result[1]} - {result[2]}")

        elif choice == "4":
            contact_id = int(input("Masukkan ID kontak yang akan dihapus: "))
            delete_contact(contact_id)
            print("Kontak berhasil dihapus!")

        elif choice == "5":
            print("Terima kasih telah menggunakan aplikasi ini.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
