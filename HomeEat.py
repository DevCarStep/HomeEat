from tkinter import *
 
root = Tk()     # создаем корневой объект - окно
root.title("HomeEat")     # устанавливаем заголовок окна
root.geometry("1800x1000")    # устанавливаем размеры окна
root.resizable(False, True)
 
label = Label(text="Добро пожаловать в HomeEat!") # создаем текстовую метку
label.pack()    # размещаем метку в окне
 
root.mainloop()