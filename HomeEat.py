from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

 
root = Tk()     # создаем корневой объект - окно
root.title("HomeEat")     # устанавливаем заголовок окна
root.iconbitmap(default=r"C:\Users\224\Desktop\HomeEat\HomeEat.ico")
root.geometry("1800x1000")    # устанавливаем размеры окна
root.resizable(False, True)
logo = PhotoImage(file=r"C:\Users\224\Desktop\HomeEat\IMG_0843 2.png")

upper_frame = ttk.Frame()
upper_frame_style = ttk.Style()
upper_frame_style.configure("TFrame", background="white")

canvas = Canvas(upper_frame, background="white", width=72, height=72, highlightthickness=0)
canvas.pack(anchor="nw", side=LEFT)

username = "Абчихба"
phone = "+7 800 555 35 35"
email = "abjihba@hotmail.ua"
def UserCircleClick(event):
    user_window = Toplevel(master=root)
    user_window.title(username)
    user_window.geometry("1800x1000")
    user_window.resizable(False, False)
    user_window.grab_set()

    upper_frame = ttk.Frame(master=user_window)
    canvas = Canvas(master=upper_frame, background="white", width=72, height=72, highlightthickness=0)
    canvas_logo = canvas.pack(anchor="nw", side=LEFT)

    canvas.create_image(36, 36, image=logo)

    user_canvas = Canvas(master=upper_frame, background="white", highlightthickness=0, height=60, width=60)
    user_canvas.pack(anchor=NE, side=RIGHT)
    idOval = user_canvas.create_oval(2, 2, 58, 58, fill="#777777", outline="#777777", tags=["clickable", "weakbutton"])
    user_canvas.create_text(30.5, 30, text=username[0], fill="white", font=("Arial", 20))

    label = ttk.Label(upper_frame, text="Профиль", background="white", font= ("Arial", 20)).pack()

    upper_frame.pack(anchor=N, fill=X, padx=315, pady=0)

    main_canvas = Canvas(master=user_window)
    main_frame = ttk.Frame(master=main_canvas)

    main_canvas.pack(fill=BOTH, padx=158)
    main_frame.pack(fill=BOTH, padx=158)
    
    username_label = ttk.Label(master=main_frame, text=username, font=("Arial", 20), background="white")
    username_label.pack(anchor=NE)
    phone_label = ttk.Label(master=main_frame, text=phone, font=("Arial", 20), background="white")
    phone_label.pack(anchor=NE)
    email_label = ttk.Label(master=main_frame, text=email, font=("Arial", 20), background="white")
    email_label.pack(anchor=NE)
    
    menuscreenpadd = 100
    menuelementspady = 20
    order_history = ttk.Label(master=main_frame, text="История заказов", font=("Arial", 22), background="white")
    order_history.pack(anchor=NW, padx=menuscreenpadd, ipady=menuelementspady)
    promocodes = ttk.Label(master=main_frame, text="Промокоды", font=("Arial", 22), background="white")
    promocodes.pack(anchor=NW, padx=menuscreenpadd, ipady=menuelementspady)
    collections = ttk.Label(master=main_frame, text="Колекции", font=("Arial", 22), background="white")
    collections.pack(anchor=NW, padx=menuscreenpadd, ipady=menuelementspady)
    become_a_cheif = ttk.Label(master=main_frame, text="Стать поваром", font=("Arial", 22), background="white")
    become_a_cheif.pack(anchor=NW, padx=menuscreenpadd, ipady=menuelementspady)
    become_a_courier = ttk.Label(master=main_frame, text="Стать курьером", font=("Arial", 22), background="white")
    become_a_courier.pack(anchor=NW, padx=menuscreenpadd, ipady=menuelementspady)
    support = ttk.Label(master=main_frame, text="Поддержка", font=("Arial", 22), background="white")
    support.pack(anchor=NW, padx=menuscreenpadd, ipady=menuelementspady)
    about_service = ttk.Label(master=main_frame, text="О сервисе", font=("Arial", 22), background="white")
    about_service.pack(anchor=NW, padx=menuscreenpadd, ipady=menuelementspady)
    log_out = ttk.Label(master=main_frame, text="Выйти из аккаунта", font=("Arial", 22), background="white")
    log_out.pack(anchor=NW, padx=menuscreenpadd, ipady=menuelementspady)
    confidential_politics = ttk.Label(master=main_frame, text="Политика конфиденциальности", font=("Arial", 18), background="white")
    confidential_politics.pack(anchor=NW, padx=menuscreenpadd, ipady=5)
    ensurance = ttk.Label(master=main_frame, text="Страхование", font=("Arial", 18), background="white")
    ensurance.pack(anchor=NW, padx=menuscreenpadd, ipady=5)


def BrightlessUp(event):
    more_bright = "#" + str(int(user_collor) + int(222222))
    canvas.itemconfigure("weakbutton", fill=more_bright)
def BrightlessDown(event): canvas.itemconfigure("weakbutton", fill="#" + str(user_collor));
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

# logo_label = ttk.Label(upper_frame, image=logo)
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