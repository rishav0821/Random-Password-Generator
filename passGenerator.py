import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")

        # Password length label and entry
        tk.Label(root, text="Password Length:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
        self.length_var = tk.StringVar()
        tk.Entry(root, textvariable=self.length_var, width=10).grid(row=0, column=1, padx=10, pady=10)

        # Include checkboxes
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)

        tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=self.include_uppercase).grid(row=1, column=0, columnspan=2, sticky="w", padx=10)
        tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=self.include_lowercase).grid(row=2, column=0, columnspan=2, sticky="w", padx=10)
        tk.Checkbutton(root, text="Include Numbers (0-9)", variable=self.include_numbers).grid(row=3, column=0, columnspan=2, sticky="w", padx=10)
        tk.Checkbutton(root, text="Include Symbols (!@#$)", variable=self.include_symbols).grid(row=4, column=0, columnspan=2, sticky="w", padx=10)

        # Generate button
        tk.Button(root, text="Generate Password", command=self.generate_password, bg="green", fg="white").grid(row=5, column=0, columnspan=2, pady=10)

        # Output area
        tk.Label(root, text="Generated Password:", font=("Arial", 12)).grid(row=6, column=0, padx=10, pady=10)
        self.output_entry = tk.Entry(root, width=40, state="readonly")
        self.output_entry.grid(row=6, column=1, padx=10, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length < 1:
                raise ValueError("Length must be at least 1.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid password length (positive integer).")
            return

        # Build character pool based on user selections
        char_pool = ""
        if self.include_uppercase.get():
            char_pool += string.ascii_uppercase
        if self.include_lowercase.get():
            char_pool += string.ascii_lowercase
        if self.include_numbers.get():
            char_pool += string.digits
        if self.include_symbols.get():
            char_pool += string.punctuation

        if not char_pool:
            messagebox.showerror("No Characters Selected", "Please select at least one character set.")
            return

        # Generate password
        password = ''.join(random.choice(char_pool) for _ in range(length))
        self.output_entry.config(state="normal")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, password)
        self.output_entry.config(state="readonly")
        messagebox.showinfo("Success", "Password generated successfully!")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()
