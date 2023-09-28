import tkinter as tk
from datetime import datetime
from tkinter import messagebox  # Hata mesajı için gerekli import

def calculate_age(birthdate):
    try:
        current_date = datetime.now()
        birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        age = current_date.year - birthdate.year
        if current_date.month < birthdate.month or (current_date.month == birthdate.month and current_date.day < birthdate.day):
            age -= 1
        return age
    except ValueError:
        # Hatalı giriş durumu için hata mesajı
        return "Hatalı Giriş"

def show_age():
    birthdate = entry.get()
    age = calculate_age(birthdate)
    
    if age == "Hatalı Giriş":
        messagebox.showerror("Error", "Invalid date format! Please enter in 'YYYY-MM-DD' format.")
    elif age is not None:
        result_label.config(text=f'''
Your Age: {age}
        ''')
    else:
        # Boş giriş durumu için hata mesajı
        messagebox.showerror("Error", "Date of birth field cannot be left blank.")

# Ana uygulama penceresini oluştur
app = tk.Tk()
app.title("Age Calculation Application")

# Giriş etiketi ve alanı
label = tk.Label(app, text='''

Enter your date of birth (YYYY-MM-DD):
    ''')
label.pack()

entry = tk.Entry(app)
entry.pack()

label = tk.Label(app, text='''
 ''')
label.pack()

# Yaşı gösterme düğmesi
calculate_button = tk.Button(app, text="Calculate", command=show_age)
calculate_button.pack()

# Yaş sonucunu gösteren etiket
result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()