from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from random import randint

 
root = Tk()     # создаем корневой объект - окно
root.title("HomeEat")     # устанавливаем заголовок окна
root.iconbitmap(default=r"C:\Users\224\Desktop\HomeEat\HomeEat.ico")
root.geometry("1800x1000")    # устанавливаем размеры окна
root.resizable(False, True)
logo = PhotoImage(file=r"C:\Users\224\Desktop\HomeEat\IMG_0843 2.png")

upper_frame = ttk.Frame() # верхний фрейм первого окна
upper_frame_style = ttk.Style()
upper_frame_style.configure("TFrame", background="white")

canvas = Canvas(upper_frame, background="white", width=72, height=72, highlightthickness=0)
canvas.pack(anchor="nw", side=LEFT)

def CreateFromMenuWindow(name):
    window = Toplevel(master=root)
    window.title(name)
    window.geometry("1800x1000")
    window.resizable(False, False)
    window.grab_set()
    return window
def TextClick(event): # обработка кликера второго окна
    if event.type == '4':
        if event.widget["text"] == "История заказов":
            CreateFromMenuWindow(event.widget["text"]) # создание окна "История заказов"
        elif event.widget["text"] == "Промокоды":
            CreateFromMenuWindow(event.widget["text"]) # создание окна "Промокоды"
        elif event.widget["text"] == "Колекции":
            CreateFromMenuWindow(event.widget["text"]) # создание окна "Колекции"
        elif event.widget["text"] == "Стать поваром":
            CreateFromMenuWindow(event.widget["text"]) # создание окна "ИСтать поваром"
        elif event.widget["text"] == "Стать курьером":
            CreateFromMenuWindow(event.widget["text"]) # создание окна "Стать курьером"
        elif event.widget["text"] == "Поддержка":
            CreateFromMenuWindow(event.widget["text"]) # создание окна "Поддержка"
        elif event.widget["text"] == "О сервисе":
            CreateFromMenuWindow(event.widget["text"]) # создание окна "О сервисе"
        elif event.widget["text"] == "Выйти из аккаунта":
            return 0 # выход из аккаунта
        elif event.widget["text"] == "Политика конфиденциальности":
            CreateFromMenuWindow(event.widget["text"]) # создание окна "Политика конфиденциальности"
        elif event.widget["text"] == "Страхование":
            CreateFromMenuWindow(event.widget["text"]) # создание окна "Страхование"
def OnTextEntered(event): # обработка попадания курсора второго окна
    if event.type == '7':
        event.widget['background'] = ""
    elif event.type == '8':
        event.widget['background'] = "white"
username = "Абчихба"
phone = "+7 800 555 35 35"
email = "abjihba@hotmail.ua"
def UserCircleClick(event): # создание второго окна
    user_window = Toplevel(master=root)
    user_window.title(username)
    user_window.geometry("1800x1000")
    user_window.resizable(False, False)
    user_window.grab_set()

    upper_frame = ttk.Frame(master=user_window) # верхний фрейм второго окна
    canvas = Canvas(master=upper_frame, background="white", width=72, height=72, highlightthickness=0)
    canvas_logo = canvas.pack(anchor="nw", side=LEFT)

    canvas.create_image(36, 36, image=logo)

    user_canvas = Canvas(master=upper_frame, background="white", highlightthickness=0, height=60, width=60)
    user_canvas.pack(anchor=NE, side=RIGHT)
    idOval = user_canvas.create_oval(2, 2, 58, 58, fill=user_color, outline=user_color, tags=["clickable", "weakbutton"])
    user_canvas.create_text(30.5, 30, text=username[0], fill="white", font=("Arial", 20))

    label = ttk.Label(upper_frame, text="Профиль", background="white", font= ("Arial", 20)).pack()

    upper_frame.pack(anchor=N, fill=X, padx=315, pady=0)

    main_canvas = Canvas(master=user_window)
    main_frame = ttk.Frame(master=main_canvas) # главный фрейм второго окна

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
    order_history = ttk.Label(master=main_frame, text="История заказов", font=("Arial", 22), background="white", cursor="hand2")
    order_history.pack(anchor=NW, padx=menuscreenpadd, ipady=menuelementspady)
    order_history.bind('<Enter>', OnTextEntered)
    order_history.bind('<Leave>', OnTextEntered)
    order_history.bind('<ButtonPress-1>', TextClick)
    promocodes = ttk.Label(master=main_frame, text="Промокоды", font=("Arial", 22), background="white", cursor="hand2")
    promocodes.pack(anchor=NW, padx=menuscreenpadd, ipady=menuelementspady)
    promocodes.bind('<Enter>', OnTextEntered)
    promocodes.bind('<Leave>', OnTextEntered)
    promocodes.bind('<ButtonPress-1>', TextClick)
    collections = ttk.Label(master=main_frame, text="Колекции", font=("Arial", 22), background="white", cursor="hand2")
    collections.pack(anchor=NW, padx=menuscreenpadd, ipady=menuelementspady)
    collections.bind('<Enter>', OnTextEntered)
    collections.bind('<Leave>', OnTextEntered)
    collections.bind('<ButtonPress-1>', TextClick)
    become_a_cheif = ttk.Label(master=main_frame, text="Стать поваром", font=("Arial", 22), background="white", cursor="hand2")
    become_a_cheif.pack(anchor=NW, padx=menuscreenpadd, ipady=menuelementspady)
    become_a_cheif.bind('<Enter>', OnTextEntered)
    become_a_cheif.bind('<Leave>', OnTextEntered)
    become_a_cheif.bind('<ButtonPress-1>', TextClick)
    become_a_courier = ttk.Label(master=main_frame, text="Стать курьером", font=("Arial", 22), background="white", cursor="hand2")
    become_a_courier.pack(anchor=NW, padx=menuscreenpadd, ipady=menuelementspady)
    become_a_courier.bind('<Enter>', OnTextEntered)
    become_a_courier.bind('<Leave>', OnTextEntered)
    become_a_courier.bind('<ButtonPress-1>', TextClick)
    support = ttk.Label(master=main_frame, text="Поддержка", font=("Arial", 22), background="white", cursor="hand2")
    support.pack(anchor=NW, padx=menuscreenpadd, ipady=menuelementspady)
    support.bind('<Enter>', OnTextEntered)
    support.bind('<Leave>', OnTextEntered)
    support.bind('<ButtonPress-1>', TextClick)
    about_service = ttk.Label(master=main_frame, text="О сервисе", font=("Arial", 22), background="white", cursor="hand2")
    about_service.pack(anchor=NW, padx=menuscreenpadd, ipady=menuelementspady)
    about_service.bind('<Enter>', OnTextEntered)
    about_service.bind('<Leave>', OnTextEntered)
    about_service.bind('<ButtonPress-1>', TextClick)
    log_out = ttk.Label(master=main_frame, text="Выйти из аккаунта", font=("Arial", 22), background="white", cursor="hand2")
    log_out.pack(anchor=NW, padx=menuscreenpadd, ipady=menuelementspady)
    log_out.bind('<Enter>', OnTextEntered)
    log_out.bind('<Leave>', OnTextEntered)
    log_out.bind('<ButtonPress-1>', TextClick)
    confidential_politics = ttk.Label(master=main_frame, text="Политика конфиденциальности", font=("Arial", 18), background="white", cursor="hand2")
    confidential_politics.pack(anchor=NW, padx=menuscreenpadd, ipady=5)
    confidential_politics.bind('<Enter>', OnTextEntered)
    confidential_politics.bind('<Leave>', OnTextEntered)
    confidential_politics.bind('<ButtonPress-1>', TextClick)
    ensurance = ttk.Label(master=main_frame, text="Страхование", font=("Arial", 18), background="white", cursor="hand2")
    ensurance.pack(anchor=NW, padx=menuscreenpadd, ipady=5)
    ensurance.bind('<Enter>', OnTextEntered)
    ensurance.bind('<Leave>', OnTextEntered)
    ensurance.bind('<ButtonPress-1>', TextClick)

def DishWindowCreate(name): # создание окна конкретного блюда
    window = Toplevel(master=root)
    window.title(name)
    window.geometry("1800x1000")
    window.resizable(False, False)
    window.grab_set()
    return window

def DishCardClick(event): # событие клика на карточку блюда
    DishWindowCreate("nullreference")

def BrightlessUp(event):
    more_bright = user_color
    canvas.itemconfigure("weakbutton", fill=more_bright)
def BrightlessDown(event): canvas.itemconfigure("weakbutton", fill=user_color);
def RandomCollor(): # генератор случайного цвета
    colorgen = lambda: randint(0,255)
    color = '#%02X%02X%02X' % (colorgen(), colorgen(), colorgen())
    return str(color)
user_color = RandomCollor()
user_canvas = Canvas(upper_frame, background="white", highlightthickness=0, height=60, width=60)
user_canvas.pack(anchor=NE, side=RIGHT)
idOval = user_canvas.create_oval(2, 2, 58, 58, fill=user_color, outline=user_color, tags=["clickable", "weakbutton"])
user_first_letter = username.upper
user_canvas.create_text(30.5, 30, text=username[0], fill="white", font=("Arial", 20))
user_canvas.bind("<ButtonPress-1>", UserCircleClick)
user_canvas.bind("<Enter>", BrightlessUp)
user_canvas.bind("<Leave>", BrightlessDown)

adress = "Луначарского, 66"
adress_label = ttk.Label(upper_frame, text=adress, background="white", font= ("Arial", 24)).pack()

# user_btn = ttk.Button(upper_frame, text="A")
# user_btn.place(height=60, width=60, anchor=NE)
# user_btn.pack(anchor="ne", side=RIGHT)

# logo_label = ttk.Label(upper_frame, image=logo)
canvas.create_image(36, 36, image=logo)
#logo_label.pack(anchor="nw", side=LEFT)

upper_frame.pack(anchor=N, fill=X, padx=315, pady=0)

separation_line = Canvas(width=1170, height=1, background="black").pack()

main_canvas = Canvas(scrollregion=(0, 0, 5000, 5000)) # главный фрейм первого окна
main_frame = ttk.Frame(master=main_canvas)
def CreateDishWidget(): # функция создания карточек блююда
    element = ttk.Frame(master=main_frame, height=250, width=210, borderwidth=1, relief=SOLID)
    element.pack_propagate(False) 
    photo = PhotoImage(file=r"C:\Users\224\Desktop\HomeEat\IMG_0843 2.png")
    photo_canvas = Canvas(element, width=190, height=190)
    photo_canvas.pack(pady=8)
    photo_canvas.create_image(95, 95, image=photo)
    photo_canvas.bind('<ButtonPress-1>', DishCardClick)
    name_label = ttk.Label(master=element, text="nullreference", font=("Arial", 16))
    name_label.pack()
    name_label.bind('<ButtonPress-1>', DishCardClick)
    element.bind('<ButtonPress-1>', DishCardClick)
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