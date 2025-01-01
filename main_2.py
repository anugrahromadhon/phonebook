import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Inisialisasi database
def init_db():
    connection = sqlite3.connect("phonebook.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE
        )
    """)
    connection.commit()
    connection.close()

# Fungsi Database
def add_contact(name, phone):
    try:
        connection = sqlite3.connect("phonebook.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
        connection.commit()
        messagebox.showinfo("Berhasil", "Kontak berhasil ditambahkan!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Kesalahan", "Nomor telepon sudah terdaftar!")
    finally:
        connection.close()

def view_contacts():
    connection = sqlite3.connect("phonebook.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    connection.close()
    return contacts

def search_contact(keyword):
    connection = sqlite3.connect("phonebook.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", (f"%{keyword}%", f"%{keyword}%"))
    results = cursor.fetchall()
    connection.close()
    return results

def delete_contact(contact_id):
    connection = sqlite3.connect("phonebook.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    connection.commit()
    connection.close()

# Fungsi GUI
def add_contact_gui():
    name = entry_name.get()
    phone = entry_phone.get()
    if name and phone:
        add_contact(name, phone)
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        refresh_contacts()
    else:
        messagebox.showerror("Kesalahan", "Nama dan Nomor Telepon tidak boleh kosong!")

def refresh_contacts():
    for row in tree.get_children():
        tree.delete(row)
    for contact in view_contacts():
        tree.insert("", tk.END, values=contact)

def search_gui():
    keyword = entry_search.get()
    results = search_contact(keyword)
    for row in tree.get_children():
        tree.delete(row)
    for contact in results:
        tree.insert("", tk.END, values=contact)

def delete_gui():
    selected_item = tree.selection()
    if selected_item:
        contact_id = tree.item(selected_item[0])["values"][0]
        delete_contact(contact_id)
        refresh_contacts()
        messagebox.showinfo("Berhasil", "Kontak berhasil dihapus!")
    else:
        messagebox.showerror("Kesalahan", "Pilih kontak yang akan dihapus!")

# Inisialisasi GUI
init_db()
root = tk.Tk()
root.title("Aplikasi Catatan Buku Telepon")
root.geometry("800x500")
root.configure(bg="#f7f7f7")

# Header
header = tk.Label(root, text="Aplikasi Catatan Buku Telepon", bg="#4CAF50", fg="white", font=("Arial", 18, "bold"))
header.pack(fill=tk.X)

# Frame Input
frame_input = tk.Frame(root, bg="#f7f7f7", pady=10)
frame_input.pack(fill=tk.X, padx=20)

tk.Label(frame_input, text="Nama:", bg="#f7f7f7", font=("Arial", 12)).grid(row=0, column=0, padx=10, sticky="w")
entry_name = ttk.Entry(frame_input, width=30, font=("Arial", 12))
entry_name.grid(row=0, column=1, padx=10)

tk.Label(frame_input, text="Nomor Telepon:", bg="#f7f7f7", font=("Arial", 12)).grid(row=0, column=2, padx=10, sticky="w")
entry_phone = ttk.Entry(frame_input, width=30, font=("Arial", 12))
entry_phone.grid(row=0, column=3, padx=10)

btn_add = tk.Button(frame_input, text="Tambah Kontak", bg="#4CAF50", fg="white", font=("Arial", 12), command=add_contact_gui)
btn_add.grid(row=0, column=4, padx=10)

# Frame Pencarian
frame_search = tk.Frame(root, bg="#f7f7f7", pady=10)
frame_search.pack(fill=tk.X, padx=20)

tk.Label(frame_search, text="Cari:", bg="#f7f7f7", font=("Arial", 12)).grid(row=0, column=0, padx=10, sticky="w")
entry_search = ttk.Entry(frame_search, width=50, font=("Arial", 12))
entry_search.grid(row=0, column=1, padx=10)

btn_search = tk.Button(frame_search, text="Cari Kontak", bg="#2196F3", fg="white", font=("Arial", 12), command=search_gui)
btn_search.grid(row=0, column=2, padx=10)

# Frame Tabel
frame_table = tk.Frame(root, bg="#f7f7f7")
frame_table.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

columns = ("ID", "Nama", "Nomor Telepon")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=15)
tree.heading("ID", text="ID")
tree.heading("Nama", text="Nama")
tree.heading("Nomor Telepon", text="Nomor Telepon")
tree.column("ID", width=50, anchor="center")
tree.column("Nama", width=200, anchor="w")
tree.column("Nomor Telepon", width=200, anchor="w")
tree.pack(fill=tk.BOTH, expand=True)

# Frame Tombol
frame_buttons = tk.Frame(root, bg="#f7f7f7", pady=10)
frame_buttons.pack(fill=tk.X, padx=20)

btn_refresh = tk.Button(frame_buttons, text="Refresh", bg="#FF9800", fg="white", font=("Arial", 12), command=refresh_contacts)
btn_refresh.pack(side=tk.LEFT, padx=10)

btn_delete = tk.Button(frame_buttons, text="Hapus Kontak", bg="#F44336", fg="white", font=("Arial", 12), command=delete_gui)
btn_delete.pack(side=tk.LEFT, padx=10)

# Refresh awal
refresh_contacts()

# Main Loop
root.mainloop()
