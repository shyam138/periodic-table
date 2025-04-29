import tkinter as tk
from tkinter import messagebox
import sqlite3

class AtomicTable:
    def __init__(self, root):
        self.root = root
        self.root.title("Atomic Table")
        self.conn = sqlite3.connect('atomic_table.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS elements
            (atomic_number INTEGER PRIMARY KEY, name TEXT, symbol TEXT)
        ''')
        self.conn.commit()
        self.atomic_number_label = tk.Label(self.root, text="Enter Atomic Number:")
        self.atomic_number_label.pack()
        self.atomic_number_entry = tk.Entry(self.root)
        self.atomic_number_entry.pack()
        self.name_label = tk.Label(self.root, text="Enter Element Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        self.symbol_label = tk.Label(self.root, text="Enter Element Symbol:")
        self.symbol_label.pack()
        self.symbol_entry = tk.Entry(self.root)
        self.symbol_entry.pack()
        self.add_element_button = tk.Button(self.root, text="Add Element", command=self.add_element)
        self.add_element_button.pack()
        self.get_element_button = tk.Button(self.root, text="Get Element", command=self.get_element)
        self.get_element_button.pack()
        self.element_info_label = tk.Label(self.root, text="")
        self.element_info_label.pack()

    def add_element(self):
        atomic_number = int(self.atomic_number_entry.get())
        name = self.name_entry.get()
        symbol = self.symbol_entry.get()
        self.cursor.execute('INSERT INTO elements VALUES (?, ?, ?)', (atomic_number, name, symbol))
        self.conn.commit()
        self.atomic_number_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.symbol_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Element added successfully")

    def get_element(self):
        atomic_number = int(self.atomic_number_entry.get())
        self.cursor.execute('SELECT * FROM elements WHERE atomic_number=?', (atomic_number,))
        row = self.cursor.fetchone()
        if row:
            self.element_info_label.config(text=f"Name: {row[1]}, Symbol: {row[2]}, Atomic Number: {row[0]}")
        else:
            self.element_info_label.config(text="Element not found")

root = tk.Tk()
atomic_table = AtomicTable(root)
root.mainloop()
