# Aplikasi Catatan Buku Telepon

## Deskripsi
Aplikasi Catatan Buku Telepon adalah aplikasi sederhana untuk mengelola kontak telepon. Aplikasi ini mendukung dua antarmuka:
1. **CLI (Command-Line Interface)**: Memungkinkan pengguna mengelola kontak melalui terminal.
2. **GUI (Graphical User Interface)**: Memungkinkan pengguna mengelola kontak melalui antarmuka grafis yang mudah digunakan.

Aplikasi ini menggunakan SQLite sebagai database untuk menyimpan data kontak secara lokal.

## Fitur Utama
- **Tambah Kontak**: Tambahkan nama dan nomor telepon baru.
- **Lihat Kontak**: Lihat daftar kontak yang tersimpan.
- **Cari Kontak**: Cari kontak berdasarkan nama atau nomor telepon.
- **Hapus Kontak**: Hapus kontak dari daftar.

## Struktur Proyek
```
phonebook/
├── main.py         # Versi CLI
├── main_2.py       # Versi GUI
├── database.py     # Pengelola database
└── README.md       # Dokumentasi proyek
```

## Persyaratan
- Python 3.x
- Library Tkinter (untuk GUI)
- Library sqlite3 (bawaan Python)

## Cara Menggunakan

### 1. Menggunakan Versi CLI
1. Jalankan file `main.py`:
   ```bash
   python main.py
   ```
2. Ikuti menu yang ditampilkan untuk mengelola kontak.

### 2. Menggunakan Versi GUI
1. Jalankan file `main_2.py`:
   ```bash
   python main_2.py
   ```
2. Gunakan antarmuka grafis untuk menambah, mencari, melihat, atau menghapus kontak.

## File Penting
- **`database.py`**: Berisi fungsi untuk mengelola database SQLite.
  - `init_db()`: Membuat tabel jika belum ada.
  - `add_contact(name, phone)`: Menambahkan kontak baru.
  - `view_contacts()`: Mengambil semua kontak dari database.
  - `search_contact(keyword)`: Mencari kontak berdasarkan nama atau nomor telepon.
  - `delete_contact(contact_id)`: Menghapus kontak berdasarkan ID.

- **`main.py`**: Implementasi antarmuka CLI.
- **`main_2.py`**: Implementasi antarmuka GUI dengan Tkinter.

## Contoh Tampilan GUI
### Tampilan Utama
Antarmuka grafis terdiri dari:
- **Input Form**: Untuk menambahkan kontak baru.
- **Search Bar**: Untuk mencari kontak.
- **Contact Table**: Menampilkan semua kontak yang tersimpan.
- **Action Buttons**: Tombol untuk menyegarkan data atau menghapus kontak.

## Lisensi
Aplikasi ini dirilis di bawah lisensi MIT. Anda bebas menggunakannya untuk keperluan pribadi maupun komersial.

---
Dibuat dengan dedikasi oleh [Anugrah Romadhon](https://github.com/anugrahromadhon).

