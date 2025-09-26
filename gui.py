import tkinter as tk
from tkinter import messagebox
import requests

API_BASE = "http://localhost:8000/api/properties"

# Dummy fallback data
mock_properties = [
    {"id": 1, "name": "Green Acres", "address": "123 Main St"},
    {"id": 2, "name": "Sunset Villas", "address": "456 Sunset Blvd"},
    {"id": 3, "name": "Lakeside Residence", "address": "789 Lakeview Dr"},
]

def fetch_properties():
    listbox.delete(0, tk.END)
    try:
        response = requests.get(API_BASE, timeout=2)
        response.raise_for_status()
        properties = response.json()
        label_status.config(text="✅ Connected to backend", fg="green")
    except Exception as e:
        # Fallback to dummy data
        properties = mock_properties
        label_status.config(text="⚠️ Backend not running – using mock data", fg="orange")
    
    for prop in properties:
        listbox.insert(tk.END, f"{prop['id']}: {prop['name']} ({prop['address']})")

def add_mock_property():
    name = name_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not address:
        messagebox.showwarning("Input Error", "Both fields are required.")
        return

    new_id = len(mock_properties) + 1
    mock_properties.append({"id": new_id, "name": name, "address": address})
    name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    fetch_properties()
    messagebox.showinfo("Mock Property Added", f"Added '{name}' to mock list.")

# UI setup
root = tk.Tk()
root.title("Property Manager (GUI)")
root.geometry("500x450")

tk.Label(root, text="Landlord Property Manager", font=("Arial", 16)).pack(pady=10)

label_status = tk.Label(root, text="Connecting...", fg="blue")
label_status.pack()

listbox = tk.Listbox(root, width=60, height=12)
listbox.pack(pady=10)

refresh_btn = tk.Button(root, text="Refresh Properties", command=fetch_properties)
refresh_btn.pack(pady=5)

form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="e")
tk.Label(form_frame, text="Address:").grid(row=1, column=0, sticky="e")

name_entry = tk.Entry(form_frame, width=30)
address_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1)
address_entry.grid(row=1, column=1)

add_btn = tk.Button(root, text="Add Mock Property", command=add_mock_property)
add_btn.pack(pady=10)

fetch_properties()
root.mainloop()
