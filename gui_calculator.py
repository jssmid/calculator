from tkinter import *
from  tkinter import messagebox


#MAIN APP WINDOW
app = Tk()


#THE TITLE OF THE WINDOW
app.title("GUI Calculator")


#THE WIDTH AND HEIGHT OF THE WINDOW
app.geometry("340x308")


#THE ENTRY SECTION
the_text = Entry(app, width=55, borderwidth=6)
the_text.grid(row=0, column=0, columnspan=7)


#THE FUNCTIONS
def click(number):
    current = the_text.get()
    the_text.delete(0,END)
    the_text.insert(0,str(current) + str(number))
    

def clear():
    the_text.delete(0,END)


def add():
    global op
    op = "+"
    first_num = the_text.get()
    global num1
    num1 = int(first_num)
    the_text.delete(0, END)
    

def minus():
    global op
    op = "-"
    first_num = the_text.get()
    global num1
    num1 = int(first_num)
    the_text.delete(0, END)


def divi():
    global op
    op = "/"
    first_num = the_text.get()
    global num1
    num1 = int(first_num)
    the_text.delete(0, END)


def multi():
    global op
    op = "*"
    first_num = the_text.get()
    global num1
    num1 = int(first_num)
    the_text.delete(0, END)


def square():
    first_num = the_text.get()
    the_text.delete(0, END)
    the_text.insert(0, int(first_num)**2)
    

def multi_of():
    global op
    op = "**"
    first_num = the_text.get()
    global num1
    num1 = int(first_num)
    the_text.delete(0, END)
    

def equall():
    global op
    global num1
    num2 = int(the_text.get())
    the_text.delete(0, END)
    
    if op == "+":
        the_text.insert(0,num1 + num2)
    elif op == "-":
        the_text.insert(0,num1 - num2)
    elif op == "/":
        num1 = float(num1)
        num2 = float(num2)
        the_text.insert(0,num1 / num2)
    elif op == "x":
        the_text.insert(0,num1 * num2)
    elif op == "**":
        the_text.insert(0, num1**num2)


#THE BUTTONS
btn_1 = Button(app, text="1" , padx=30, pady=10,bg="#FFFFFF",font="arial 15 bold",borderwidth=0,activebackground="#CAD8DE", command=lambda : click(1))
btn_2 = Button(app, text="2" , padx=30, pady=10,bg="#FFFFFF",font="arial 15 bold",borderwidth=0, activebackground="#CAD8DE",command=lambda : click(2))
btn_2 = Button(app, text="2" , padx=30, pady=10,bg="#FFFFFF",font="arial 15 bold",borderwidth=0, activebackground="#CAD8DE",command=lambda : click(2))
btn_3 = Button(app, text="3" , padx=30, pady=10,bg="#FFFFFF",font="arial 15 bold",borderwidth=0, activebackground="#CAD8DE",command=lambda : click(3))
btn_4 = Button(app, text="4" , padx=30, pady=10,bg="#FFFFFF",font="arial 15 bold",borderwidth=0, activebackground="#CAD8DE",command=lambda : click(4))
btn_5 = Button(app, text="5" , padx=30, pady=10,bg="#FFFFFF",font="arial 15 bold",borderwidth=0, activebackground="#CAD8DE",command=lambda : click(5))
btn_6 = Button(app, text="6" , padx=30, pady=10,bg="#FFFFFF",font="arial 15 bold",borderwidth=0, activebackground="#CAD8DE",command=lambda : click(6))
btn_7 = Button(app, text="7" , padx=30, pady=10,bg="#FFFFFF",font="arial 15 bold",borderwidth=0, activebackground="#CAD8DE",command=lambda : click(7))
btn_8 = Button(app, text="8" , padx=30, pady=10,bg="#FFFFFF",font="arial 15 bold",borderwidth=0, activebackground="#CAD8DE",command=lambda : click(8))
btn_9 = Button(app, text="9" , padx=30, pady=10,bg="#FFFFFF",font="arial 15 bold",borderwidth=0, activebackground="#CAD8DE",command=lambda : click(9))
btn_0 = Button(app, text="0" , padx=30, pady=10,bg="#FFFFFF",font="arial 15 bold",borderwidth=0, activebackground="#CAD8DE",command=lambda : click(0))

clear_btn = Button(app, text="C", padx=35, pady=17, bg="#D0EAE0", activebackground="#C7DCD4",borderwidth=0,command=clear)
plus_btn = Button(app, text="+", padx=35, pady=17, bg="#D0EAE0", activebackground="#C7DCD4",borderwidth=0, command=add)
minus_btn = Button(app, text="-", padx=36, pady=17, bg="#D0EAE0", activebackground="#C7DCD4",borderwidth=0, command=minus)
division_btn = Button(app, text="/", padx=36, pady=17, bg="#D0EAE0", activebackground="#C7DCD4",borderwidth=0, command=divi)
multi_btn = Button(app, text="x", padx=35, pady=17, bg="#D0EAE0", activebackground="#C7DCD4",borderwidth=0, command=multi)
equal_btn = Button(app, text="=", padx=123, pady=17, bg="#D0E3EA", activebackground="#A4CFE4",borderwidth=0, command=equall)
square_btn = Button(app, text="x²", padx=37, pady=17, bg="#D0EAE0", activebackground="#C7DCD4",borderwidth=0, command=square)
factorial_btn = Button(app, text="xʸ", padx=35, pady=17, bg="#D0EAE0", activebackground="#C7DCD4",borderwidth=0, command=multi_of)


#THE POSITION OF THE BUTTONS
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)


btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)


btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
clear_btn.grid(row=1,column=3)


plus_btn.grid(row=2, column=3)
minus_btn.grid(row=3, column=3)
division_btn.grid(row=4, column=3)
multi_btn.grid(row=5,column=3)


square_btn.grid(row=4,column=0)
btn_0.grid(row=4, column=0,columnspan=3)
factorial_btn.grid(row=4,column=2)
equal_btn.grid(row=5, column=0,columnspan=3)


#MAINLOOP
app.mainloop()
