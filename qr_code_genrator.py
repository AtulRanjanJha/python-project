import qrcode
import tkinter as tk
from tkinter import filedialog

class QRCodeGenerator:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")

        # Create label and entry widgets
        self.label = tk.Label(master, text="Enter text or URL:")
        self.label.pack()
        self.entry = tk.Entry(master, width=50)
        self.entry.pack()

        # Create button widgets
        self.generate_button = tk.Button(master, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack()
        self.save_button = tk.Button(master, text="Save QR Code", command=self.save_qr_code, state=tk.DISABLED)
        self.save_button.pack()

        # Initialize variables
        self.qr_code = None

    def generate_qr_code(self):
        # Generate QR Code
        data = self.entry.get()
        if data:
            self.qr_code = qrcode.make(data)
            self.save_button.config(state=tk.NORMAL)
        else:
            self.qr_code = None
            self.save_button.config(state=tk.DISABLED)

    def save_qr_code(self):
        # Save QR Code as image file
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            self.qr_code.save(file_path)

root = tk.Tk()
qrcode_generator = QRCodeGenerator(root)
root.mainloop()