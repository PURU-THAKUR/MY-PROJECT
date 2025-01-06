import tkinter as tk
from tkinter import messagebox

class InventoryManagement:
    def __init__(self):
        self.inventory = {}

    def add_product(self, name, qty):
        if name in self.inventory:
            self.inventory[name] += qty
        else:
            self.inventory[name] = qty

    def delete_product(self, name):
        if name in self.inventory:
            del self.inventory[name]

    def view_inventory(self):
        return "\n".join([f"{name}: {qty}" for name, qty in self.inventory.items()])

# GUI
class InventoryApp:
    def __init__(self, root):
        self.system = InventoryManagement()
        self.root = root
        self.root.title("Inventory Management")

        # UI Components
        self.label = tk.Label(root, text="Inventory Management System")
        self.label.pack()

        self.name_label = tk.Label(root, text="Product Name")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.qty_label = tk.Label(root, text="Quantity")
        self.qty_label.pack()
        self.qty_entry = tk.Entry(root)
        self.qty_entry.pack()

        self.add_button = tk.Button(root, text="Add Product", command=self.add_product)
        self.add_button.pack()

        self.view_button = tk.Button(root, text="View Inventory", command=self.view_inventory)
        self.view_button.pack()

    def add_product(self):
        name = self.name_entry.get()
        qty = int(self.qty_entry.get())
        self.system.add_product(name, qty)
        messagebox.showinfo("Success", f"Added {qty} of {name}")

    def view_inventory(self):
        inventory = self.system.view_inventory()
        if inventory:
            messagebox.showinfo("Inventory", inventory)
        else:
            messagebox.showinfo("Inventory", "No items in inventory")

# Run the Inventory app
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()

