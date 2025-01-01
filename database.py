import sqlite3

# Inisialisasi dan pengelolaan database
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

def add_contact(name, phone):
    try:
        connection = sqlite3.connect("phonebook.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
        connection.commit()
    except sqlite3.IntegrityError:
        print("Nomor telepon sudah terdaftar!")
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
