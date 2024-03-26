
from tkinter import * #графические интерфейсы

from math import * #математические функции

def solve_quadratic():# коэффициенты квадратного уравнения a, b и c, вычисляет его дискриминант
    a_val = a.get() #get -возврат текста который ввел пользователь в Entry
    b_val = b.get()
    c_val = c.get()

    if a_val and b_val and c_val:
        a_val = float(a_val)
        b_val = float(b_val)
        c_val = float(c_val)

        discriminant = b_val**2 - 4*a_val*c_val

        if discriminant > 0:
            x1 = (-b_val + sqrt(discriminant)) / (2*a_val)
            x2 = (-b_val - sqrt(discriminant)) / (2*a_val)
            result = f"D = {round(discriminant, 2)}\nx1 = {round(x1, 2)}\nx2 = {round(x2, 2)}"
        elif discriminant == 0:
            x = -b_val / (2*a_val)
            result = f"D = {round(discriminant, 2)}\nОдин корень: x = {round(x, 2)}"
        else:
            result = "Нет действительных корней"

        output.config(text=result)
    else:
        output.config(text="Поля должны быть заполнены")
        if not a_val:
            a.configure(bg="red")
        if not b_val:
            b.configure(bg="red")
        if not c_val:
            c.configure(bg="red")


root = Tk() #Создает главное окно приложения
root.geometry("600x500")#Задает размеры главного окна приложения
root.title("Квадратные уравнения")#Устанавливает заголовок для главного окна
root.iconbitmap("travel.ico")#Устанавливает иконку для главного окна приложения

f = Frame(root, border=50, height=50, width=600)# Создает рамку в главном окне приложения
f_all = Frame(root, border=50, height=200, width=600)#Создает еще одну рамку в главном окне
#Label - отображает текст или изображение на экране
t = "Решение квадратного уравнения"
l = Label(root, text=t, bg="#99c2e8", fg="#008000", font="Arial 16", height=3, width=len(t))
l.pack()

t_top = Frame(root)#Создает рамку  в верхней части главного окна.
t_top.pack()

a = Entry(t_top, width=5, bg="#99c2e8", font="Arial 15")# вводить текст с клавиатуры. 
a.pack(side=LEFT, padx=0, pady=0)

b_lab = Label(t_top, text="x**2 +", fg="#008000", font="Arial 15")
b_lab.pack(side=LEFT, padx=10, pady=10)
b = Entry(t_top, width=5, bg="#99c2e8", font="Arial 15")
b.pack(side=LEFT, padx=10, pady=10)

c_lab = Label(t_top, text="x +", fg="#008000", font="Arial 15")
c_lab.pack(side=LEFT, pady=10)
c = Entry(t_top, width=5, bg="#99c2e8", font="Arial 15")
c.pack(side=LEFT, padx=10, pady=10)

d_lab = Label(t_top, text="=0", fg="#008000", font="Arial 15")
d = Entry(t_top, width=5, bg="#99c2e8", font="Arial 15")
d_lab.pack(side=LEFT, padx=10, pady=10)

btn = Button(t_top, text="Решить", font="Arial 12 bold", bg="#008000", command=solve_quadratic)
btn.pack(side=RIGHT, padx=10, pady=10)

output_lab_bottom = Label(root, text="...", font="Arial 12 bold", width=5)
output_lab_bottom.pack(side='bottom')

output = Button(root, text=" ", font="Arial 12 bold", bg="yellow", width=40)
output.pack(fill='y')

root.mainloop()#Запускает цикл обработки событий

