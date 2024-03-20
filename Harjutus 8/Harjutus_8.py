
from tkinter import *

root = Tk()  # Окно
root.geometry("600x800")  # Размер окна
root.title("Квадратные уравнения")  # Заголовок
root.iconbitmap("travel.ico")  # Иконка окна (книга) - 248

f = Frame(root, border=50, height=50, width=600)  # Рамка
f_all = Frame(root, border=50, height=200, width=600)  # Нижняя рамка
t = "Решение квадратного уравнения"
l = Label(f, text=t, bg="#99c2e8", fg="#008000", font="Arial 16", height=3, width=len(t))  # Надпись

t_top = Frame(root)  # Верхняя рамка
t_button = Frame(root)  # Рамка для кнопок
t_bot = Frame(root)  # Нижняя рамка  

a = Entry(t_top, width=5, bg="#99c2e8", font="Arial 15")  # Поле для ввода коэффициента перед x^2
a.pack(side=LEFT, padx=0, pady=0)

b_lab = Label(t_top, text="x**2 +",fg="#008000", font="Arial 15")  # Метка для ввода x**2
b_lab.pack(side=LEFT, padx=10, pady=10)
b = Entry(t_top, width=5, bg="#99c2e8", font="Arial 15")  # Поле для ввода коэффициента перед x^2
b.pack(side=LEFT, padx=10, pady=10)


c_lab = Label(t_top, text="x +", fg="#008000",font="Arial 15")  # Метка для ввода b
c_lab.pack(side=LEFT,pady=10)
c = Entry(t_top, width=5, bg="#99c2e8", font="Arial 15")  # Поле для ввода коэффициента перед x^2
c.pack(side=LEFT, padx=10, pady=10)

d_lab = Label(t_top, text="=0",fg="#008000", font="Arial 15")  # Метка для ввода c
d = Entry(t_top, width=5, bg="#99c2e8", font="Arial 15")
d_lab.pack(side=LEFT, padx=10, pady=10)


btn = Button(t_top, text="Решить", font="Arial 12 bold", bg="#008000") # Кнопка для решения уравнения
btn.pack(side=RIGHT, padx=10, pady=10)

##output.geometry("600x800")  # Размер окна
##output = Text(t_bot, bg="yellow", fg="black", font="Arial 10")  # Вывод
##output.pack(expand=1, fill=BOTH, side=LEFT)  # Размещение текстового поля по центру
#output = Text(root, bg="yellow", fg="black", font="Arial 10", width=5, height=5)  # Вывод, размеры 600x800
#output.pack(expand=1, fill=BOTH)  # Размещение текстового поля на всю доступную область


f.pack()  # Упаковка рамки
l.pack()  # Упаковка надписи в заголовке 

t_top.pack()  # Упаковка верхней рамки
t_button.pack() # Упаковка рамки для кнопок
t_bot.pack()  # Упаковка нижней рамки

root.mainloop()  # Главный цикл программы