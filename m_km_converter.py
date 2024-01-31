import tkinter as tk

MILE_TO_KM = 1.609344
KM_TO_MILE = 0.621371

def calculate_miles():
    x = entry1.get()
    try:
        calculated = float(x) * KM_TO_MILE
        result_label1.config(text=f'{x} miles = {calculated:.3f} KM', fg='white')
    except ValueError:
        result_label1.config(text="Invalid input. Please enter a number.", fg='red')

def calculate_kilometers():
    x = entry2.get()
    try:
        calculated = float(x) * MILE_TO_KM
        result_label2.config(text=f'{x} KM = {calculated:.3f} miles', fg='white')
    except ValueError:
        result_label2.config(text="Invalid input. Please enter a number.", fg='red')

window = tk.Tk()
window.title("Miles/Kilometer Converter")
window.geometry('400x200')
window.resizable(False, False)
window.configure(bg='#2c3e50')  # Dark background color

# Title Label
title_label = tk.Label(window, text='Miles to Kilometer Converter', font=('Helvetica', 16, 'bold'), bg='#2c3e50', fg='white')
title_label.pack(pady=10)

# Miles to Kilometers Conversion
frame1 = tk.Frame(window, bg='#2c3e50')
frame1.pack(pady=10)

label_entry1 = tk.Label(frame1, text='Enter value in Miles:', bg='#2c3e50', fg='white')
label_entry1.grid(row=0, column=0, padx=5)

entry1 = tk.Entry(frame1, bg='#34495e', fg='white')  # Dark input field
entry1.grid(row=0, column=1, padx=5)

button1 = tk.Button(frame1, text='Calculate', command=calculate_miles, bg='#3498db', fg='white')  # Blue button
button1.grid(row=0, column=2, padx=5)

result_label1 = tk.Label(frame1, text='', font=('Helvetica', 10), bg='#2c3e50', fg='white')
result_label1.grid(row=1, column=0, columnspan=3)

# Kilometers to Miles Conversion
frame2 = tk.Frame(window, bg='#2c3e50')
frame2.pack(pady=10)

label_entry2 = tk.Label(frame2, text='Enter value in Kilometers:', bg='#2c3e50', fg='white')
label_entry2.grid(row=0, column=0, padx=5)

entry2 = tk.Entry(frame2, bg='#34495e', fg='white')  # Dark input field
entry2.grid(row=0, column=1, padx=5)

button2 = tk.Button(frame2, text='Calculate', command=calculate_kilometers, bg='#3498db', fg='white')  # Blue button
button2.grid(row=0, column=2, padx=5)

result_label2 = tk.Label(frame2, text='', font=('Helvetica', 10), bg='#2c3e50', fg='white')
result_label2.grid(row=1, column=0, columnspan=3)

window.mainloop()
