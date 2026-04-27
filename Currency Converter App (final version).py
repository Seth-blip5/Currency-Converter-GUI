import customtkinter as ctk
from tkinter import messagebox

# Set the appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CurrencyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- MAINTAINING YOUR DATA ---
        self.rates = {"USD": 1, "INR": 94, "LBR": 194, "EUR": 0.92, "GBP": 0.78}
        
        # Window Setup
        self.title("SETH AI | Currency Pro")
        self.geometry("400x500")

        # Title Header
        self.header = ctk.CTkLabel(self, text="CURRENCY CONVERTER", font=("Orbitron", 20, "bold"))
        self.header.pack(pady=20)

        # Main Card Frame
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=10, padx=30, fill="both", expand=True)

        # Amount Entry
        self.label_amt = ctk.CTkLabel(self.frame, text="Amount to Convert")
        self.label_amt.pack(pady=(20, 0))
        self.entry_amount = ctk.CTkEntry(self.frame, placeholder_text="e.g. 100", width=200)
        self.entry_amount.pack(pady=10)

        # From Currency Dropdown (COOL FEATURE: No more typing!)
        self.label_from = ctk.CTkLabel(self.frame, text="From")
        self.label_from.pack(pady=(10, 0))
        self.option_from = ctk.CTkOptionMenu(self.frame, values=list(self.rates.keys()))
        self.option_from.pack(pady=10)

        # To Currency Dropdown
        self.label_to = ctk.CTkLabel(self.frame, text="To")
        self.label_to.pack(pady=(10, 0))
        self.option_to = ctk.CTkOptionMenu(self.frame, values=list(self.rates.keys()))
        self.option_to.set("INR") # Default choice
        self.option_to.pack(pady=10)

        # Convert Button
        self.btn_convert = ctk.CTkButton(self, text="CONVERT NOW", command=self.perform_logic, corner_radius=10, font=("Arial", 14, "bold"))
        self.btn_convert.pack(pady=20)

        # Result Display (The 'Realistic' readout)
        self.result_display = ctk.CTkLabel(self, text="---", font=("Arial", 16, "bold"), text_color="#10b981")
        self.result_display.pack(pady=10)

    def perform_logic(self):
        # MAINTAINING YOUR EXACT LOGIC
        try:
            amount = float(self.entry_amount.get())
            from_currency = self.option_from.get()
            to_currency = self.option_to.get()

            if from_currency in self.rates and to_currency in self.rates:
                usd_amount = amount / self.rates[from_currency]
                converted = usd_amount * self.rates[to_currency]
                
                # Realistic formatting
                result_str = f"{amount:,} {from_currency} = {converted:,.2f} {to_currency}"
                self.result_display.configure(text=result_str)
            else:
                messagebox.showerror("Error", "Invalid selection.")
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid numeric amount.")

if __name__ == "__main__":
    app = CurrencyApp()
    app.mainloop()