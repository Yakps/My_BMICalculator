import tkinter as tk



#window
window = tk.Tk()
window.title("BMI CALCULATOR")
window.minsize(width=300, height=200)


#label
my_label = tk.Label(text="Enter your Weight(kg) : ")
my_label.config(fg="black")
my_label.config(padx=10, pady=10)
my_label.pack()

#entry
my_entry = tk.Entry(width=20)
my_entry.pack()

#label2
my_label2 = tk.Label(text="Enter your Height(cm): ")
my_label2.config(fg="black")
my_label2.config(padx=10, pady=10)
my_label2.pack()

#entry2
my_entry2 = tk.Entry(width=20)
my_entry2.pack()


#result label
result_label = tk.Label( text="")
result_label.pack(side=tk.BOTTOM)




def button_clicked():
    try:
        kilo = float(my_entry.get())             #değerlerin float olup olmadığını kontrol ediyoruz
        boy = float(my_entry2.get())             #değerlerin float olup olmadığını kontrol ediyoruz
    except ValueError:               #hariç demek
        result = "Value Error.Please enter correct values"
        result_label.config(text=result)
        return

    bmi = kilo / ((boy/100)**2)

    if bmi <= 18.4:
        result = f"Underweight: {bmi}"
        result_label.config(text=result)
    elif bmi > 18.4 and bmi <= 24.9:
        result = f"Normal:{bmi}"
        result_label.config(text=result)
    elif bmi >= 25.0 and bmi <= 39.9:
        result = f"Overweight:{bmi}"
        result_label.config(text=result)
    elif bmi >= 40.0:
        result = f"Obese:{bmi}"
        result_label.config(text=result)








#button
button = tk.Button(text="Click me",command=button_clicked)
button.pack()







window.mainloop()
