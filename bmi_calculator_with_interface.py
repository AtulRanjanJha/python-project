from tkinter import *
from tkinter import messagebox

class BMI:
    def __init__(self):
        self.root = Tk()
        self.root.title("BMI Calculator")
        self.label = Label(self.root, text="BMI Calculator")
        self.label.pack()

        # Creating labels and entry fields for age, height, and weight
        self.label_age = Label(self.root, text="Age:")
        self.label_age.pack()
        self.entry_age = Entry(self.root)
        self.entry_age.pack()

        self.label_height = Label(self.root, text="Height (cm):")
        self.label_height.pack()
        self.entry_height = Entry(self.root)
        self.entry_height.pack()

        self.label_weight = Label(self.root, text="Weight (kg):")
        self.label_weight.pack()
        self.entry_weight = Entry(self.root)
        self.entry_weight.pack()

        # Creating a calculate button
        self.button_calculate = Button(self.root, text="Calculate BMI", command=self.calculate_bmi)
        self.button_calculate.pack()

        # Creating a clear button
        self.button_clear = Button(self.root, text="Clear", command=self.clear)
        self.button_clear.pack()

        self.root.mainloop()

    def calculate_bmi(self):
        # Getting input from entry fields
        age = self.entry_age.get()
        height = self.entry_height.get()
        weight = self.entry_weight.get()

        # Validating input
        if not age or not height or not weight:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        age = int(age)
        height = float(height)
        weight = float(weight)

        # Calculating BMI
        bmi = weight / (height / 100) ** 2
        bmi = round(bmi, 2)

        # Displaying BMI
        message = f"Your BMI is {bmi}"
        if bmi < 18.5:
            message += "\nYou are underweight."
        elif 18.5 <= bmi <= 24.9:
            message += "\nYou have a normal weight."
        elif 25.0 <= bmi <= 29.9:
            message += "\nYou are overweight."
        elif 30.0 <= bmi:
            message += "\nYou are obese."

        messagebox.showinfo("BMI Result", message)

    def clear(self):
        self.entry_age.delete(0, END)
        self.entry_height.delete(0, END)
        self.entry_weight.delete(0, END)

if __name__ == "__main__":
    BMI()