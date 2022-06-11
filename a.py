# from tkinter import *
# from PIL import Image ,ImageTk
# window =Tk()
# window.title("Login")

# my_image= ImageTk.PhotoImage(Image.open("C:\\Users\\User\\OneDrive\\Desktop\\python\\125.png"))

# my_lable= Label(window,image=my_image)
# my_lable.pack()

# button_quit= Button(window,text="exit",command=window.quit,width=20)
# button_quit.pack()
# window.mainloop()

# from tkinter import*
# window =Tk()
# window.geometry('800x500')
# bg =PhotoImage(file="125.png")
# my_label= Label(window,image=bg)
# my_label.pack()

# window.mainloop()












from tkinter import *

root = Tk()
root.title('Simple calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+ str(number))

def button_clear(): 
    e.delete(0, END)    

def button_add():
    first_number = e.get()
    global a
    a = "add"
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global a
    a = "subtract"
    global f_num
    f_num = int(first_number)
    e.delete(0,END)

def button_division():
    first_number = e.get()
    global a
    a = "division"
    global f_num
    f_num = int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global a
    a = "multiply"
    global f_num
    f_num = int(first_number)
    e.delete(0,END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if a == "add":
        e.insert(0, f_num + int(second_number))
    elif a == "subtract":
        e.insert(0, f_num - int(second_number))
    elif a == "multiply":
        e.insert(0, f_num * int(second_number))
    else:
        e.insert(0, f_num / int(second_number))

# Defining the buttons
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text='+', padx=39, pady=20, command=button_add)
button_equal = Button(root, text='=', padx=91, pady=20, command=button_equal)
button_subtract = Button(root, text='-', padx=55, pady=20, command=button_subtract)
button_multiply = Button(root, text='*', padx=43, pady=20, command=button_multiply)
button_division = Button(root, text='/', padx=45, pady=20, command=button_division)
button_clear = Button(root, text='Clear', padx=79, pady=20, command=button_clear)



# putting the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=1)
button_multiply.grid(row=6, column=2)
button_division.grid(row=6, column=0)
button_equal.grid(row=5, column=1, columnspan=2)


root.mainloop()

 