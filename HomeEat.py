from tkinter import *
from tkinter import ttk
import tkinter.font
from tkinter.messagebox import showinfo
from random import randint
import codecs
import sqlite3
import tkinter
from tkinter import font
from tkinter import colorchooser

con = sqlite3.connect('userdata.db') # запрос на создание таблицы пользователей, если её не существует
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    id integer primary key,
                    name text, 
                    email text, 
                    phone number,
                    password text
                )
            ''')
con.commit()
con = sqlite3.connect('userdata.db') # запрос на создание таблицы блюд, если её не существует
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS dishes(
                    id integer primary key,
                    name text, 
                    price int,
                    composition text,
                    weight int,
                    photo text
                )
            ''')
con.commit()
# cur.execute("INSERT INTO record(name, email, phone, password) VALUES (:name, :email, :phone, :password)", {
#                             'name': "Абчихба",
#                             'email': "abjihba@hotmail.ua",
#                             'phone': 88005553535,
#                             'password': "12345678"

#             })
# con.commit()

class Account: # класс аккаунта
    def __init__(self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

class Dish: # класс блюда
    def __init__(self, name, price, composition, weight, photo):
        self.name = name
        self.price = price
        self.composition = composition
        self.weight = weight
        self.photo = photo


accounts = list() # нулевой элемент - всегда пустой аккаунт
accounts.append(Account("Войти", "", "", ""))
#accounts.append(Account("Абчихба", "abjihba@hotmail.ua", "12345678", "+7 800 555 35 35"))
dishes = list()

con = sqlite3.connect('userdata.db')
cur = con.cursor()
for row in con.execute("Select * from record"):
    accounts.append(Account(row[1], row[2], row[3], row[4]))
    
user = accounts[0] # текущий пользователь
 
root = Tk()     # создаем корневой объект - окно
root.title("HomeEat")     # устанавливаем заголовок окна
root.iconbitmap(default=r"C:\Users\224\Desktop\HomeEat\HomeEat.ico")
root.geometry("1800x1000")    # устанавливаем размеры окна
root.resizable(False, True)
logo = tkinter.PhotoImage(file=r"C:\Users\224\Desktop\HomeEat\IMG_0843 2.png")
def RandomCollor(): # генератор случайного цвета
    colorgen = lambda: randint(0,255)
    color = '#%02X%02X%02X' % (colorgen(), colorgen(), colorgen())
    return str(color)
user_color = RandomCollor()
con = sqlite3.connect('userdata.db')
cur = con.cursor()
for row in con.execute("Select * from dishes"):
    insert_photo = tkinter.PhotoImage(file=r"C:\Users\224\Desktop" + row[5])
    dishes.append(Dish(row[1], row[2], row[3], row[4], insert_photo))

upper_frame = ttk.Frame() # верхний фрейм первого окна
upper_frame_style = ttk.Style(master=root)
upper_frame_style.configure("TFrame", background="white")

canvas = Canvas(upper_frame, background="white", width=72, height=72, highlightthickness=0)
canvas.pack(anchor="nw", side=LEFT)

def UserMenuCircleClickToChangeColor(event):
    global user_color
    result = colorchooser.askcolor(initialcolor=user_color)
    user_color = result[1]
    if result is not None:
        user_canvas.itemconfigure(idOval, fill=user_color, outline=user_color)
        RestartRootWindow(user_window)
        UserCircleClick('<ButtonPress-1>')

reg_warn = StringVar(value='')
def RegistrationAllowing(username, email, phone, password, rep_password): # проверка на соответствие требованиям регистрации
    check_counter = 0
    global reg_warn
    if username == "":
        reg_warn = "Name can't be empty"
    else:
        check_counter += 1
    if email == "":
        reg_warn = "Email can't be empty"
    else:
        check_counter += 1
    if phone == "":
        reg_warn = "Phone can't be empty"
    else:
        check_counter += 1
    if len(password) < 8 and len(password) > 30:
        reg_warn = "Too short or too long password"
    else:
        check_counter += 1
    if password != rep_password:
        reg_warn = "Repeat password correctly"
    else:
        check_counter += 1
    if check_counter == 5:
        return True
    else:
        return False

def Registration(username, email, phone , password, rep_password): # функция регистрации
    if RegistrationAllowing(username, email, phone, password, rep_password):
        try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record (name, email, phone, password) VALUES (:name, :email, :phone, :password)", {
                            'name': username,
                            'email': email,
                            'phone': phone,
                            'password': password

            })
            con.commit()
            accounts.append(Account(username, email, phone, password))
            user = accounts[len(accounts)-1]
            print("Succesful")
            UserCircleClick("<ButtonPress-1>")
            registration_window.destroy()
        except Exception as ep:
            print(ep)
    else:
        print("Not allowed")

def OnTextUnderline(event): # подчёркивание на наведение на текст
    if event.type == '7':
        event.widget['font'] = font.Font(family="Arial", size=10, weight=NORMAL, underline=True, overstrike=False)
    elif event.type == '8':
        event.widget['font'] = font.Font(family="Arial", size=10, weight=NORMAL, underline=False, overstrike=False)

def RestartRootWindow(window): # показ главного окна, если оно свёрнуто
    window.destroy()
    root.update()
    root.update_idletasks()
    root.deiconify()

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
            order_history_window = CreateFromMenuWindow(event.widget["text"]) # создание окна "История заказов"
        elif event.widget["text"] == "Промокоды":
            promocodes_window = CreateFromMenuWindow(event.widget["text"]) # создание окна "Промокоды"
        elif event.widget["text"] == "Колекции":
            collections_window = CreateFromMenuWindow(event.widget["text"]) # создание окна "Колекции"
        elif event.widget["text"] == "Стать поваром":
            become_a_cheif_window = CreateFromMenuWindow(event.widget["text"]) # создание окна "Стать поваром"
        elif event.widget["text"] == "Стать курьером":
            become_a_courier_window = CreateFromMenuWindow(event.widget["text"]) # создание окна "Стать курьером"
        elif event.widget["text"] == "Поддержка":
            support_window = CreateFromMenuWindow(event.widget["text"]) # создание окна "Поддержка"
        elif event.widget["text"] == "О сервисе":
            about_service_window = CreateFromMenuWindow(event.widget["text"]) # создание окна "О сервисе"
        elif event.widget["text"] == "Выйти из аккаунта":
            global user
            user = accounts[0]
            root.update()
            RestartRootWindow(user_window)
            UserCircleClick("<Button-Press-1>")
        elif event.widget["text"] == "Политика конфиденциальности":
            confidentiality_politics_window = CreateFromMenuWindow(event.widget["text"]) # создание окна "Политика конфиденциальности"
            confidentiality_politics_window.grid_columnconfigure(0, weight = 1)
            confidentiality_politics_window.grid_rowconfigure(0, weight = 1)

            confidential_politics_file = codecs.open(r"C:\Users\224\Desktop\HomeEat\confedintial_politics.txt", "r", "utf_8_sig")
            content = confidential_politics_file.read()

            sc = Text(master=confidentiality_politics_window, wrap=WORD)
            sc.grid(column = 0, row = 0, sticky = NSEW)
            doc_scrollbar = ttk.Scrollbar(master=confidentiality_politics_window, orient = "vertical", command = sc.yview)
            doc_scrollbar.grid(column = 1, row = 0, sticky = NS)
            sc.insert(END, content)
            sc["state"] = DISABLED
            sc["yscrollcommand"] = doc_scrollbar.set
            confidential_politics_file.close()
        elif event.widget["text"] == "Пользовательское соглашение":
            user_argeement_window = CreateFromMenuWindow(event.widget["text"]) # создание окна "Пользовательское соглашение"
            user_argeement_window.grid_columnconfigure(0, weight = 1)
            user_argeement_window.grid_rowconfigure(0, weight = 1)

            user_argeement_file = codecs.open(r"C:\Users\224\Desktop\HomeEat\user_agreement.txt", "r", "utf_8_sig")
            content = user_argeement_file.read()

            sc = Text(master=user_argeement_window, wrap=WORD)
            sc.grid(column = 0, row = 0, sticky = NSEW)
            doc_scrollbar = ttk.Scrollbar(master=user_argeement_window, orient = "vertical", command = sc.yview)
            doc_scrollbar.grid(column = 1, row = 0, sticky = NS)
            sc.insert(END, content)
            sc["state"] = DISABLED
            sc["yscrollcommand"] = doc_scrollbar.set
            user_argeement_file.close()
        elif event.widget["text"] == "Регистрация":
            global registration_window
            registration_window = CreateFromMenuWindow(event.widget["text"]) # создание окна "регистрация"
            registration_window.protocol("WM_DELETE_WINDOW", lambda: RestartRootWindow(registration_window))
            login_window.destroy()

            form = ttk.Frame(master=registration_window, style="TFrame")
            form.pack(anchor=CENTER, pady=250, ipadx=15, ipady=15)
            registrarion_label = ttk.Label(form, text="Регистрация", background="white", font=("Arial", 32))
            registrarion_label.pack(anchor=N, pady=20)
            username_form_label = ttk.Label(form, text="Придумайте псевдоним", background="white")
            username_form_label.pack(anchor=W, padx=12)
            username_input = ttk.Entry(form)
            username_input.pack(anchor=N, pady=10, fill=X, padx=10)
            email_form_label = ttk.Label(form, text="E-mail", background="white")
            email_form_label.pack(anchor=W, padx=12)
            email_input = ttk.Entry(form)
            email_input.pack(anchor=N, pady=10, fill=X, padx=10)
            phone_form_label = ttk.Label(form, text="Номер телефона", background="white")
            phone_form_label.pack(anchor=W, padx=12)
            phone_input = ttk.Entry(form)
            phone_input.pack(anchor=N, pady=10, fill=X, padx=10)
            password_form_label = ttk.Label(form, text="Придумайте пароль", background="white")
            password_form_label.pack(anchor=W, padx=12)
            password_input = ttk.Entry(form, show='*')
            password_input.pack(anchor=N, pady=10, fill=X, padx=10)
            passwordrepeat_form_label = ttk.Label(form, text="Повторите парль", background="white")
            passwordrepeat_form_label.pack(anchor=W, padx=12)
            passwordrepeat_input = ttk.Entry(form, show='*')
            passwordrepeat_input.pack(anchor=N, pady=10, fill=X, padx=10)
            reg_btn = ttk.Button(form, text="ЗАРЕГИСТРИРОВАТЬСЯ", command= lambda: Registration(username_input.get(), email_input.get(), phone_input.get(), password_input.get(), passwordrepeat_input.get()))
            reg_btn.pack(anchor=S, fill=X, pady=2, padx=15)
            global reg_warn
            errmsg = StringVar(value=reg_warn)
            reg_error_label = ttk.Label(form, foreground="red", background="white", textvariable=errmsg)
            reg_error_label.pack(anchor=NW, padx=12, pady=5)
            font1 = font.Font(family="Arial", size=10, weight=NORMAL, underline=False, overstrike=False)
            login_label = ttk.Label(form, foreground="#0089EC", background="white", text="Есть аккаунт? Авторизация", font=font1, cursor="hand2")
            login_label.pack(anchor=S, padx=15, pady=2)
            login_label.bind('<ButtonPress-1>', UserCircleClick)
            login_label.bind('<Enter>', OnTextUnderline)
            login_label.bind('<Leave>', OnTextUnderline)

def OnTextEntered(event): # обработка попадания курсора второго окна
    if event.type == '7':
        event.widget['background'] = ""
    elif event.type == '8':
        event.widget['background'] = "white"

def UserChecker(email, password): # функция проверки почты и пароля
    global user
    global login_window
    try:
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
    except Exception as ep:
        print('error')
    # for row in c.execute("Select * from record"):
    #     demail = row[2]
    #     pwd = row[4]
    for i in accounts:
        if email == i.email and password == i.password:
            user = i
   
            root.update()
            root.update_idletasks()

            print("Succesful")
            print("Logged", i.name)
            RestartRootWindow(login_window)
            UserCircleClick("<ButtonPress-1>")
            break

def UserCircleClick(event): # создание второго окна
    if user != accounts[0]:
        root.withdraw()
        global user_window
        user_window = Toplevel()
        user_window.title(user.name)
        user_window.geometry("1800x1000")
        user_window.resizable(False, False)
        user_window.grab_set()
        user_window.protocol("WM_DELETE_WINDOW", lambda: RestartRootWindow(user_window))

        upper_frame = ttk.Frame(master=user_window) # верхний фрейм второго окна
        canvas = Canvas(master=upper_frame, background="white", width=72, height=72, highlightthickness=0)
        canvas_logo = canvas.pack(anchor="nw", side=LEFT)

        canvas.create_image(36, 36, image=logo)

        user_canvas = Canvas(master=upper_frame, background="white", highlightthickness=0, height=60, width=60)
        user_canvas.pack(anchor=NE, side=RIGHT)
        idOval = user_canvas.create_oval(2, 2, 58, 58, fill=user_color, outline=user_color, tags=["clickable", "weakbutton"])
        user_canvas.bind("<ButtonPress-1>", UserMenuCircleClickToChangeColor)
        user_canvas.itemconfigure(idOval, fill=user_color, outline=user_color)
        user_canvas.create_text(30.5, 30, text=user.name[0], fill="white", font=("Arial", 20))

        label = ttk.Label(upper_frame, text="Профиль", background="white", font= ("Arial", 20)).pack()

        upper_frame.pack(anchor=N, fill=X, padx=315, pady=0)

        main_canvas = Canvas(master=user_window)
        main_frame = ttk.Frame(master=main_canvas) # главный фрейм второго окна

        main_canvas.pack(fill=BOTH, padx=158)
        main_frame.pack(fill=BOTH, padx=158)
        
        username_label = ttk.Label(master=main_frame, text=user.name, font=("Arial", 20), background="white")
        username_label.pack(anchor=NE)
        phone_label = ttk.Label(master=main_frame, text=user.phone, font=("Arial", 20), background="white")
        phone_label.pack(anchor=NE)
        email_label = ttk.Label(master=main_frame, text=user.email, font=("Arial", 20), background="white")
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
        user_argeement = ttk.Label(master=main_frame, text="Пользовательское соглашение", font=("Arial", 18), background="white", cursor="hand2")
        user_argeement.pack(anchor=NW, padx=menuscreenpadd, ipady=5)
        user_argeement.bind('<Enter>', OnTextEntered)
        user_argeement.bind('<Leave>', OnTextEntered)
        user_argeement.bind('<ButtonPress-1>', TextClick)

        user_window.mainloop()
        user_window.update()
        user_window.update_idletasks()
        if user == accounts[0]:
            RestartRootWindow(user_window)

    elif user == accounts[0]: # иначе окно входа
        root.withdraw()
        global login_window
        if "registration_window" in locals():
            registration_window.destroy()
        login_window = Toplevel() # создание окна входа
        login_window.title("Вход в аккаунт")
        login_window.geometry("1800x1000")
        login_window.resizable(False, False)
        login_window.grab_set()
        login_window.update()
        login_window.protocol("WM_DELETE_WINDOW", lambda: RestartRootWindow(login_window))

        form = ttk.Frame(login_window, style="TFrame")
        form.pack(anchor=CENTER, pady=350, ipadx=15, ipady=15)
        login_label = ttk.Label(form, text="Вход в аккаунт", background="white", font=("Arial", 32))
        login_label.pack(anchor=N, pady=20)
        form_email_label = ttk.Label(form, text="Эл. почта", background="white")
        form_email_label.pack(anchor=W, padx=12)
        email_input = ttk.Entry(form)
        email_input.pack(anchor=N, pady=10, fill=X, padx=10)
        form_password_label = ttk.Label(form, text="Пароль", background="white")
        form_password_label.pack(anchor=W, padx=12)
        password_input = ttk.Entry(form, show='*')
        password_input.pack(anchor=N, pady=10, fill=X, padx=10)
        login_btn = ttk.Button(form, text="ВОЙТИ", command=lambda: UserChecker(email_input.get(), password_input.get()))
        login_btn.pack(anchor=S, fill=X, pady=2, padx=15)
        errmsg = StringVar()
        login_error_label = ttk.Label(form, foreground="red", background="white", textvariable=errmsg)
        login_error_label.pack(anchor=NW, padx=12, pady=5)
        font1 = font.Font(family="Arial", size=10, weight=NORMAL, underline=False, overstrike=False)
        registration_label = ttk.Label(form, foreground="#0089EC", background="white", text="Регистрация", font=font1, cursor="hand2")
        registration_label.pack(anchor=S, padx=15, pady=2)
        registration_label.bind('<ButtonPress-1>', TextClick)
        registration_label.bind('<Enter>', OnTextUnderline)
        registration_label.bind('<Leave>', OnTextUnderline)
        login_window.mainloop()
        if user != accounts[0]:
            RestartRootWindow(login_window)

def DishWindowCreate(name): # создание окна конкретного блюда
    window = Toplevel(master=root)
    window.title(name)
    window.geometry("1800x1000")
    window.resizable(False, False)
    window.grab_set()

    dish_frame = ttk.Frame(master=window)
    dish_frame.pack(anchor=N, padx=315, side=TOP, fill=BOTH)
    photo_canvas = Canvas(master=dish_frame, width=290, height=290, highlightbackground="white")
    photo_canvas.grid(row=0, column=0, rowspan=4, padx=80, pady=100, sticky=N)
    name_label = ttk.Label(dish_frame, text="nullreference", font=("Arial", 32), background="white", wraplength=500)
    name_label.grid(row=0,column=1, sticky=W)
    price_weight_label = ttk.Label(dish_frame, text="0" + " рублей, " + "0" + " грамм", background="white", font=("Arial", 20), wraplength=400)
    price_weight_label.grid(row=1,column=1, sticky=NW)
    sostav = ttk.Label(dish_frame, text="Состав:", background="white", font=("Arial", 20))
    sostav.grid(row=2, column=1, sticky=NSEW)
    composition_label = ttk.Label(dish_frame, text="-\n-\n-\n-\n", background="white", font=("Arial", 20))
    composition_label.grid(row=3, column=1, sticky=NSEW)
    back_btn = ttk.Button(master=dish_frame, text="Назад", command= lambda: RestartRootWindow(window))
    back_btn.grid(row=4, column=0, sticky=SW, padx=30, pady=20)
    order_btn = ttk.Button(master=dish_frame, text="Заказать")
    order_btn.grid(row=4, column=1, sticky=SE, padx=30, pady=20)
    return window

def DishCardClick(event): # событие клика на карточку блюда
    DishWindowCreate("nullreference")

def BrightlessUp(event):
    more_bright = user_color
    canvas.itemconfigure("weakbutton", fill=more_bright)
def BrightlessDown(event): canvas.itemconfigure("weakbutton", fill=user_color);
user_canvas = Canvas(upper_frame, background="white", highlightthickness=0, height=60, width=60)
user_canvas.pack(anchor=NE, side=RIGHT)
idOval = user_canvas.create_oval(2, 2, 58, 58, fill=user_color, outline=user_color, tags=["clickable", "weakbutton"])
user_first_letter = user.name.upper
user_letter_text = user_canvas.create_text(30.5, 30, text=user.name[0], fill="white", font=("Arial", 20))
user_canvas.itemconfigure(user_letter_text, text=user.name[0])
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

main_canvas = Canvas(root, scrollregion=(0, 0, 5000, 5000)) # главный фрейм первого окна
scrollbar = ttk.Scrollbar(main_canvas, orient="vertical", command=canvas.yview)
main_frame = ttk.Frame(main_canvas)

def CreateDishWidget(dish): # функция создания карточек блююда
    element = ttk.Frame(master=main_frame, height=400, width=362, borderwidth=1, relief=SOLID)
    element.pack_propagate(False)
    photo = dish.photo
    photo_canvas = Canvas(element, width=290, height=290, highlightbackground="white")
    photo_canvas.pack(pady=20)
    photo_canvas.create_image(145, 145, image=photo)
    photo_canvas.bind('<ButtonPress-1>', DishCardClick)
    name_label = ttk.Label(master=element, text=dish.name, font=("Arial", 16), background="white")
    name_label.pack(anchor=NW, padx=8, pady=4)
    price_label = ttk.Label(master=element, text=str(dish.price) + "₽", font=("Arial", 12), foreground="#AAAAAA", background="white")
    price_label.pack(anchor=W, padx=8, pady=5)
    price_label.bind('<ButtonPress-1>', DishCardClick)
    name_label.bind('<ButtonPress-1>', DishCardClick)
    element.bind('<ButtonPress-1>', DishCardClick)
    return element
incr = 0
for i in range(3):
    for j in range(3):
        element = CreateDishWidget(dish=dishes[incr])
        element.grid(row=i, column=j, padx=5, pady=5, ipadx=6, ipady=6, sticky= EW)
        incr += 1

scrollbar = ttk.Scrollbar(main_canvas, orient="vertical", command=main_canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
main_frame.pack(fill=Y)
main_canvas.pack(fill=Y)
main_canvas["yscrollcommand"] = scrollbar.set


root.mainloop()