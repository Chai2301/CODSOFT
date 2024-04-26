import sqlite3 as sql

class Contact_Book:

    def __init__(self):
        self.connection = sql.connect("contacts_Book.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                email TEXT NOT NULL,
                address TEXT
            )
        ''')
        self.connection.commit()

    def view_contacts(self):
        self.cursor.execute("SELECT * FROM contacts")
        self.contacts = self.cursor.fetchall()

        print("---- Contact List ----")
        for contact in self.contacts:
            print("ID:", contact[0])
            print("Name:", contact[1])
            print("Phone Number:", contact[2])
            print("Email:", contact[3])
            print("Address:", contact[4])
            print("---------------------")

    def add_contact(self):
        self.name = input("Enter name: ")
        self.phone_number = input("Enter phone number: ")
        self.email = input("Enter email: ")
        self.address = input("Enter address: ")
        self.cursor.execute("INSERT INTO contacts (name, phone_number, email, address) VALUES (?, ?, ?, ?)",
                            (self.name, self.phone_number, self.email, self.address))
        self.connection.commit()
        print("--------Contact added successfully------------")

    def update_contact(self):
        self.contact_id = int(input("Enter the ID of the contact you want to update: "))
        self.cursor.execute("SELECT * FROM contacts WHERE id=?", (self.contact_id,))
        self.contact = self.cursor.fetchone()
        if self.contact:
            print("Current Details:")
            print("Name:", self.contact[1])
            print("Phone Number:", self.contact[2])
            print("Email:", self.contact[3])
            print("Address:", self.contact[4])
            print("---------------------")
            self.name = input("Enter new name (press Enter to keep current): ") or self.contact[1]
            self.phone_number = input("Enter new phone number (press Enter to keep current): ") or self.contact[2]
            self.email = input("Enter new email (press Enter to keep current): ") or self.contact[3]
            self.address = input("Enter new address (press Enter to keep current): ") or self.contact[4]
            self.cursor.execute("UPDATE contacts SET name=?, phone_number=?, email=?, address=? WHERE id=?",
                                (self.name, self.phone_number, self.email, self.address, self.contact_id))
            self.connection.commit()
            print("Contact updated successfully.")
        else:
            print("Contact not found.")
        self.connection.close()

    def delete_contact(self):
        self.contact_id = int(input("Enter the ID of the contact you want to delete: "))
        self.cursor.execute("SELECT * FROM contacts WHERE id=?", (self.contact_id,))
        self.contact = self.cursor.fetchone()
        if self.contact:
            self.cursor.execute("DELETE FROM contacts WHERE id=?", (self.contact_id,))
            self.connection.commit()
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")
        self.connection.close()

    def search_contact(self):
        search_term = input("Enter name or email to search: ")
        self.cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR email LIKE ?", ('%' + search_term + '%', '%' + search_term + '%'))
        self.contacts = self.cursor.fetchall()
        if self.contacts:
            print("Search Results:")
            for contact in self.contacts:
                print("ID:", contact[0])
                print("Name:", contact[1])
                print("Phone Number:", contact[2])
                print("Email:", contact[3])
                print("Address:", contact[4])
                print("---------------------")
        else:
            print("No matching contacts found.")
        self.connection.close()

    def main(self):
        while True:
            print("---------Contact Information-----------")
            print("1. View Contact List")
            print("2. Add Contact")
            print("3. Update Contact")
            print("4. Delete Contact")
            print("5. Search Contact")
            print("6. Exit")
            print("---------------------------------------")

            user = int(input("Enter your choice: "))

            if user == 1:
                self.view_contacts()
            elif user == 2:
                self.add_contact()
            elif user == 3:
                self.update_contact()
            elif user == 4:
                self.delete_contact()
            elif user == 5:
                self.search_contact()
            elif user == 6:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

# main program
obj= Contact_Book()
obj.main()
