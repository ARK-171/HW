from sqlite3 import *
import tkinter as tk
from tkinter import ttk

def insert():
    conn = connect('рабочие.db')
    cursor = conn.cursor()
    ins = 'insert into рабочие values(' + "'" + nt1.get() + "'" + ',' + "'" + nt2.get() + "'" + ')'
    cursor.execute(ins)
    conn.commit()
    nt1.delete(0, tk.END)
    nt2.delete(0, tk.END)

def show():
    conn = connect('рабочие.db')
    cursor = conn.cursor()
    sql = 'select фамилия, имя from рабочие'
    cursor.execute(sql)
    for i in cursor.fetchall():
        lb.insert(tk.END, str(i[0])+' '+str(i[1]))

def delete():
    lb.delete(0, tk.END)

def find():
    conn = connect('рабочие.db')
    cursor = conn.cursor()
    ins = 'select * from рабочие where ' + ' ' + 'имя' + ' ' + 'like' + ' ' + str(nt3.get()) + ' ' + 'or' + ' ' + 'фамилия' + ' ' + 'like' + ' ' + str(nt3.get()) + ' ' + 'or' + ' ' + 'отчество' + ' ' + 'like' + ' ' + str(nt3.get()) + ' ' + 'or' + ' ' + 'должность' + ' ' + 'like' + ' ' + str(nt3.get()) + ' ' + 'or' + ' ' + 'телефон' + ' ' + 'like' + ' ' + str(nt3.get()) + ' ' + 'or' + ' ' + 'зарплата' + ' ' + '=' + str(nt3.get())
    cursor.execute(ins)
    for l in cursor.fetchall():
        lb2.insert(tk.END, str(l))


win = tk.Tk()

style = ttk.Style(win)
style.configure('uptab.TNotebook', tabposition = 'ws')

ntbook = ttk.Notebook(win, style = 'lefttab.TNotebook')
f1 = tk.Frame(ntbook, width=200, height=200)
f2 = tk.Frame(ntbook, width=200, height=200)
f3 = tk.Frame(ntbook, width=200, height=200)

ntbook.add(f1, text='Добавить')
ntbook.add(f2, text='Просмотр')
ntbook.add(f3, text='Поиск')
ntbook.pack()

lb = tk.Listbox(f2, width=30)
lb2 = tk.Listbox(f3, width=30)

scb = tk.Scrollbar(f2)
scb.config(command = lb.yview)
scb.pack(side=tk.RIGHT, fill=tk.Y)
scb2 = tk.Scrollbar(f3)
scb2.config(command = lb2.yview)
scb2.pack(side=tk.RIGHT, fill=tk.Y)
scb3 = tk.Scrollbar(f3)
scb3.config(command = lb2.xview)
scb3.pack(side=tk.BOTTOM, fill=tk.X)

lb2.pack(side=tk.BOTTOM, fill=tk.BOTH)
lb.pack(side=tk.RIGHT, fill=tk.BOTH)

fr = tk.Frame(f2)
fr.pack(side=tk.LEFT)
fr2 = tk.Frame(f3)
fr2.pack(side=tk.TOP)

txt1 = tk.Label(f1, text='Имя', font='Arial 10')
txt2 = tk.Label(f1, text='Фамилия', font='Arial 10')
nt1 = tk.Entry(f1)
nt2 = tk.Entry(f1)
nt3 = tk.Entry(f3)
bt1 = tk.Button(f1, text='Добавить', font='Arial 10', command = insert)
bt2 = tk.Button(fr, text='Показать', font='Arial 10', command = show)
bt2.pack(side=tk.BOTTOM)
bt3 = tk.Button(fr, text='Удалить', font='Arial 10', command = delete)
bt3.pack(side=tk.BOTTOM)
bt4 = tk.Button(f3, text='Найти', font='Arial 10', command = find)
nt3.pack(side=tk.RIGHT)
bt4.pack(side=tk.RIGHT)

txt1.grid(row=0, column=0)
txt2.grid(row=1, column=0)
nt1.grid(row=0, column=1)
nt2.grid(row=1, column=1)
bt1.grid(row=2, column=1, sticky=tk.E)

win.mainloop()
