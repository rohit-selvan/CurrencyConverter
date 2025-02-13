import tkinter as tk
from tkinter import ttk, messagebox
import requests

class CurrencyConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")
        self.geometry("600x400")
        self.configure(bg="#f0f4f8")  # Light pastel background
        self.currencies = ["USD", "EUR", "INR", "GBP", "AUD", "CAD", "JPY", "CNY"]
        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self, text="Currency Converter", font=("Verdana", 24, "bold"), bg="#f0f4f8", fg="#2c3e50").pack(pady=20)
        
        # Amount Entry
        tk.Label(self, text="Enter Amount:", font=("Verdana", 14), bg="#f0f4f8").pack(pady=5)
        self.amount_entry = tk.Entry(self, font=("Verdana", 14), width=20)
        self.amount_entry.pack(pady=5)
        
        # From Currency Dropdown
        tk.Label(self, text="From Currency:", font=("Verdana", 14), bg="#f0f4f8").pack(pady=5)
        self.from_currency = ttk.Combobox(self, values=self.currencies, font=("Verdana", 12), state="readonly")
        self.from_currency.set("Select Currency")
        self.from_currency.pack(pady=5)
        
        # To Currency Dropdown
        tk.Label(self, text="To Currency:", font=("Verdana", 14), bg="#f0f4f8").pack(pady=5)
        self.to_currency = ttk.Combobox(self, values=self.currencies, font=("Verdana", 12), state="readonly")
        self.to_currency.set("Select Currency")
        self.to_currency.pack(pady=5)
        
        # Convert Button
        tk.Button(self, text="Convert", command=self.convert_currency, font=("Verdana", 14), bg="#3498db", fg="white", width=15).pack(pady=20)
        
        # Result Display
        self.result_label = tk.Label(self, text="", font=("Verdana", 16), bg="#f0f4f8", fg="#2c3e50")
        self.result_label.pack(pady=10)

    def convert_currency(self):
        amount = self.amount_entry.get().strip()
        from_curr = self.from_currency.get()
        to_curr = self.to_currency.get()
        
        if not amount or from_curr == "Select Currency" or to_curr == "Select Currency":
            messagebox.showwarning("Input Error", "Please fill all fields correctly.")
            return
        
        try:
            amount = float(amount)
            rate = self.get_exchange_rate(from_curr, to_curr)
            if rate:
                converted_amount = amount * rate
                self.result_label.config(text=f"{amount:.2f} {from_curr} = {converted_amount:.2f} {to_curr}")
            else:
                messagebox.showerror("Conversion Error", "Failed to fetch exchange rate.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the amount.")
    
    def get_exchange_rate(self, from_currency, to_currency):
        api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        try:
            response = requests.get(api_url)
            data = response.json()
            rate = data["rates"].get(to_currency)
            return rate
        except Exception as e:
            print(f"Error fetching exchange rate: {e}")
            return None

if __name__ == "__main__":
    app = CurrencyConverter()
    app.mainloop()
