from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
 
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

def UserCircleClick(event):
    showinfo(title="Информация", message="Кликер работает!")
def BrightlessUp(event):
    more_bright = int(user_collor, base=16) + int(222222, base=16)
    canvas.itemconfigure("weakbutton", fill="#" + str(more_bright))
    print(more_bright)
def BrightlessDown(event): canvas.itemconfigure("weakbutton", fill=user_collor)
username = "Абчихба"
user_collor = "777777"
user_canvas = Canvas(upper_frame, background="white", highlightthickness=0, height=60, width=60)
user_canvas.pack(anchor=NE, side=RIGHT)
idOval = user_canvas.create_oval(2, 2, 58, 58, fill="#777777", outline="#777777", tags=["clickable", "weakbutton"])
user_first_letter = username.upper
user_canvas.create_text(30.5, 30, text=username[0], fill="white", font=("Arial", 20))
user_canvas.bind("<ButtonPress-1>", UserCircleClick)
user_canvas.bind("<Enter>", BrightlessUp)
user_canvas.bind("<Leave>", BrightlessDown)

adress = "Луначарского, 66"
label = ttk.Label(upper_frame, text=adress, background="white", font= ("Arial", 24))
label.pack()

# user_btn = ttk.Button(upper_frame, text="A")
# user_btn.place(height=60, width=60, anchor=NE)
# user_btn.pack(anchor="ne", side=RIGHT)

logo = PhotoImage(file=r"C:\Users\224\Desktop\HomeEat\IMG_0843 2.png")
logo_label = ttk.Label(upper_frame, image=logo)
canvas.create_image(36, 36, image=logo)
#logo_label.pack(anchor="nw", side=LEFT)

upper_frame.pack(anchor=N, fill=X, padx=315, pady=0)

separation_line = Canvas(width=1170, height=1, background="black")
separation_line.pack()

main_frame = ttk.Frame()

scrollbar = ttk.Scrollbar(orient="vertical")
scrollbar.pack(side=RIGHT, fill=Y)

root.mainloop()