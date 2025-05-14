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

username = "Абчихба"
def UserCircleClick(event):
    user_window = Tk()
    user_window.title(username)
    user_window.geometry("1800x1000")
    user_window.resizable(False, True)
    user_window.grab_set()
def BrightlessUp(event):
    more_bright = int(str(user_collor)) + int("222222")
    canvas.itemconfigure("weakbutton", fill="#" + str(more_bright))
def BrightlessDown(event): canvas.itemconfigure("weakbutton", fill="#" + str(user_collor))
user_collor = int("777777")
user_canvas = Canvas(upper_frame, background="white", highlightthickness=0, height=60, width=60)
user_canvas.pack(anchor=NE, side=RIGHT)
idOval = user_canvas.create_oval(2, 2, 58, 58, fill="#777777", outline="#777777", tags=["clickable", "weakbutton"])
user_first_letter = username.upper
user_canvas.create_text(30.5, 30, text=username[0], fill="white", font=("Arial", 20))
user_canvas.bind("<ButtonPress-1>", UserCircleClick)
user_canvas.bind("<Enter>", BrightlessUp)
user_canvas.bind("<Leave>", BrightlessDown)

adress = "Луначарского, 66"
label = ttk.Label(upper_frame, text=adress, background="white", font= ("Arial", 24)).pack()

# user_btn = ttk.Button(upper_frame, text="A")
# user_btn.place(height=60, width=60, anchor=NE)
# user_btn.pack(anchor="ne", side=RIGHT)

logo = PhotoImage(file=r"C:\Users\224\Desktop\HomeEat\IMG_0843 2.png")
logo_label = ttk.Label(upper_frame, image=logo)
canvas.create_image(36, 36, image=logo)
#logo_label.pack(anchor="nw", side=LEFT)

upper_frame.pack(anchor=N, fill=X, padx=315, pady=0)

separation_line = Canvas(width=1170, height=1, background="black").pack()

main_canvas = Canvas(scrollregion=(0, 0, 5000, 5000))
main_frame = ttk.Frame(master=main_canvas)
def CreateDishWidget():
    element = ttk.Frame(master=main_frame, height=250, width=210, borderwidth=1, relief=SOLID)
    element.pack_propagate(False) 
    photo = PhotoImage(file=r"C:\Users\224\Desktop\HomeEat\IMG_0843 2.png")
    photo_canvas = Canvas(element, width=190, height=190)
    photo_canvas.pack(pady=8)
    photo_canvas.create_image(95, 95, image=photo)
    name_label = ttk.Label(master=element, text="nullreference", font=("Arial", 16)).pack()
    return element
for i in range(4):
    for j in range(5):
        element = CreateDishWidget()
        element.grid(row=i, column=j, padx=5, pady=5, ipadx=6, ipady=6, sticky= EW)
scrollbar = ttk.Scrollbar(main_canvas, orient="vertical", command=main_canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
main_frame.pack(fill=Y)
main_canvas.pack(fill=Y)
main_canvas["yscrollcommand"] = scrollbar.set


root.mainloop()