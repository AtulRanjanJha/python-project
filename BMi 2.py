Weight= float(input("Enter your weight in kg: "))
Height= float(input("Enter your Height in m: "))

Bmi=Weight/Height**2
Bmi=round(Bmi,2)
if Bmi<18.5:
    print(f"You are Underweight as you Bmi is {Bmi}")
elif 18.5<Bmi<25:
    print(f"You are Normal weight as you Bmi is {Bmi}")
elif 25<Bmi<30:
    print(f"You are Overweight as you Bmi is {Bmi}")
elif 30<Bmi<35:
    print(f"You are Obese as you Bmi is {Bmi}")
elif 35<Bmi:
    print(f"You are Clinically Obese as you Bmi is {Bmi}")
