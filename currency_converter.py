import tkinter as tk
from tkinter import ttk

# Simple currency converter using static exchange rates relative to USD
RATES = {
    "USD": 1.0,
    "EUR": 0.94,
    "JPY": 134.22,
    "GBP": 0.82,
    "AUD": 1.48,
    "CAD": 1.36,
    "CHF": 0.90,
}

class CurrencyConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")
        self.geometry("300x200")

        currencies = sorted(RATES.keys())

        # Amount entry
        tk.Label(self, text="Amount:").pack(pady=5)
        self.amount_var = tk.StringVar()
        tk.Entry(self, textvariable=self.amount_var).pack()

        # From currency
        tk.Label(self, text="From:").pack(pady=5)
        self.from_var = tk.StringVar(value=currencies[0])
        ttk.OptionMenu(self, self.from_var, currencies[0], *currencies).pack()

        # To currency
        tk.Label(self, text="To:").pack(pady=5)
        self.to_var = tk.StringVar(value=currencies[1])
        ttk.OptionMenu(self, self.to_var, currencies[1], *currencies).pack()

        tk.Button(self, text="Convert", command=self.convert).pack(pady=10)

        self.result_label = tk.Label(self, text="Result:")
        self.result_label.pack()

    def convert(self):
        try:
            amount = float(self.amount_var.get())
            from_cur = self.from_var.get()
            to_cur = self.to_var.get()
            usd = amount / RATES[from_cur]
            converted = usd * RATES[to_cur]
            self.result_label.config(text=f"Result: {converted:.2f} {to_cur}")
        except ValueError:
            self.result_label.config(text="Please enter a valid number")

if __name__ == "__main__":
    app = CurrencyConverter()
    app.mainloop()
