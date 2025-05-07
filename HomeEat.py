from tkinter import *
from tkinter import ttk
 
root = Tk()     # создаем корневой объект - окно
root.title("HomeEat")     # устанавливаем заголовок окна
root.iconbitmap(default=r"C:\Users\224\Desktop\HomeEat\HomeEat.ico")
root.geometry("1800x1000")    # устанавливаем размеры окна
root.resizable(False, True)

upper_frame = ttk.Frame()
upper_frame_style = ttk.Style()
upper_frame_style.configure("TFrame", background="white")

canvas = Canvas(upper_frame, background="white", width=72, height=72, highlightthickness=0)
canvas.pack(anchor="nw", side=LEFT)

adress = "Луначарского, 66"
label = ttk.Label(upper_frame, text=adress, background="white")
label.pack()

user_btn = ttk.Button(upper_frame, text="A")
user_btn.place(height=60, width=60, anchor=NE)
user_btn.pack(anchor="ne", side=RIGHT)

logo = PhotoImage(file=r"C:\Users\224\Desktop\HomeEat\IMG_0843 2.png")
logo_label = ttk.Label(upper_frame, image=logo)
canvas.create_image(36, 36, image=logo)
#logo_label.pack(anchor="nw", side=LEFT)

upper_frame.pack(anchor=N, fill=X, padx=8, pady=8)

root.mainloop()