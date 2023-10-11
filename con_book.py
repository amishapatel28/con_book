import tkinter as tk
from tkinter import messagebox

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone and email and address:  # Corrected the syntax here
        contact_list.insert(tk.END, f"{name}: {phone}:{email}:{address}")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

    else:
        messagebox.showerror("Error", "Please enter name, phone number, email, and address.")

# Function to view selected contact
def view_contact():
    try:
        selected_contact = contact_list.get(contact_list.curselection())
        messagebox.showinfo("Contact Details", selected_contact)
    except:
        messagebox.showerror("Error", "Please select a contact first.")

# Function to delete selected contact
def delete_contact():
    try:
        selected_index = contact_list.curselection()[0]
        contact_list.delete(selected_index)
    except:
        messagebox.showerror("Error", "Please select a contact first.")

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Create input fields and labels
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Create buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

view_button = tk.Button(root, text="View Contact", command=view_contact)
view_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

# Create the listbox to display contacts
contact_list = tk.Listbox(root)
contact_list.pack()

# Start the GUI main loop
root.mainloop()
