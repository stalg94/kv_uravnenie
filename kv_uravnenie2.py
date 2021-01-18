from tkinter import*
import tkinter as tk
from PIL import ImageTk, Image
from math import*
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def uravnenie(a,b,c):
    D=b**2-4*a*c
    if D>0:
        x1=(-b+sqrt(D))/(2*a)
        x2=(-b-sqrt(D))/(2*a)
        text=(f'уравнение имеет 2 корня: Х1 = {round(x1,1)} и Х2 = {round(x2,1)}')
    elif D==0:
        x=(-b)/(2*a)
        text=(f'уравнение имеет один корень = {x}' )
    else:
        text=('решения нет')
    return text

def vstavka(value):
    otvet.delete(0,END)
    otvet.insert(END,value)

def rewenie():
    try:
        a_val = int(a.get())
        b_val = int(b.get())
        c_val = int(c.get())
        vstavka(uravnenie(a_val, b_val, c_val))
    except TypeError:
        vstavka('вводить только числа')

def rewenie2():
    try:
        a_val = int(a.get())
        b_val = int(b.get())
        c_val = int(c.get())
        x1_val=int(otrezok1.get())
        x2_val=int(otrezok2.get())
        vstavka(grafik(a_val, b_val, c_val,x1_val,x2_val))
    except TypeError:
        vstavka('вводить только числа')

def grafik(a,b,c,x1,x2):
    x = np.arange(x1,x2,0.5)  # x - массив np.array
    y1 = a*x**2 + b*x +c
    plt.subplots()
    plt.title(f"y = {a}x^2 + {b}*x + {c}")
    plt.xlabel("Ось абсцисс")
    plt.ylabel("Ось ординат")
    plt.xticks(np.arange(x1, x2, 1))
    plt.grid(True)# Отображение сетки на координатной плоскости
    plt.plot(x,y1 ,'--r',linewidth=5,label="Парабола")# График красного цвета
    plt.savefig("my_image.png")  # Сохранение изображения или
    plt.show()
    return

win1=Tk()
win1.title('Решаем квадратное уравнение!')
win1.geometry('600x500')
photo=tk.PhotoImage(file=r'C:\Users\stalg\source\repos\tkinter1\kv_urav1.png')
win1.iconphoto(False,photo)
win1.config(bg='#D83131')
win1.minsize(300,400)
win1.maxsize(700,700)

a=Entry(win1)
a.grid(row=1,column=0,padx=(10,0))
lbl1=Label(win1,text='X^2 + ',bg='#D83131',fg='white').grid(row=1,column=1,stick='w')
b=Entry(win1)
b.grid(row=1,column=2)
lbl1=Label(win1,text='X + ',bg='#D83131',fg='white').grid(row=1,column=3,stick='w')
c=Entry(win1)
c.grid(row=1,column=4)
lbl1=Label(win1,text=' = 0',bg='#D83131',fg='white').grid(row=1,column=6)
btn1=Button(win1,text='Arvuta!',command=rewenie).grid(row=2,column=2,stick='we',pady=10)
lbl_graf=Label(win1, text='график функции',font='Arial 18',height=3,bg='#D83131',fg='white').grid(row=4, column=0,columnspan=5,stick='we')
lbl=Label(win1,text='AX^2+BX+C=0',font='bold',height=3,bg='#D83131',fg='white').grid(row=0, column=0,columnspan=5,stick='we')
otvet=Entry(win1,font='Arial 11',width=10,bg='#E2BD28')
otvet.grid(row=3,column=0,columnspan=5,stick='we',padx=10, pady=10)
otrezok1=Entry(win1)
otrezok2=Entry(win1)
otrezok1.grid(row=5,column=0,padx=10)
otrezok2.grid(row=6,column=0,padx=10,pady=10)
lbl_x1=Label(win1,text='интервал Х1',bg='#D83131',fg='white').grid(row=5,column=1)
lbl_x2=Label(win1,text='интервал Х2',bg='#D83131',fg='white').grid(row=6,column=1)
btn_grafik=Button(win1,text='Построить!',command=rewenie2)
btn_grafik.grid(row=5,column=2,rowspan=2,stick='ns')
win1.mainloop()

