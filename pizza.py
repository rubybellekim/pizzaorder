#!/usr/local/bin/python3

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()

#configure
#screen size
window.geometry('300x420')
window.title('Pizza Day')

window.minsize(width=300, height=420)
window.maxsize(width=300, height=420)

#labels
lbl_top = ttk.Label(window, text="Build your own pizza!", font=("Arial Bold", 13), foreground="green")
lbl_size = ttk.Label(window, text="Choose size", font=("Arial Bold", 9))
lbl_topping = ttk.Label(window, text="Choose toppings", font=("Arial Bold", 9))

lbl_top.place(x=60, y=20)
lbl_size.place(x=15, y=80)
lbl_topping.place(x=15, y=180)

#combobox for size
size = ('small (+$9)', 'medium (+$12.50)', 'large (+$15)', 'extra-large (+$17.50)')
combo_size = ttk.Combobox(window, values=size, width=20)
combo_size.current(0)
combo_size.place(x=15, y=115)

#checkbox for toppings
checkVar1 = StringVar()
check1 = Checkbutton(window, text="Pepperoni ($1)", variable=checkVar1)
check1.deselect()

checkVar2 = StringVar()
check2 = Checkbutton(window, text="Cheese ($0)", variable=checkVar2)
check2.select()

checkVar3 = StringVar()
check3 = Checkbutton(window, text="Olive ($1)", variable=checkVar3)
check3.deselect()

checkVar4 = StringVar()
check4 = Checkbutton(window, text="Pineapple ($1)", variable=checkVar4)
check4.deselect()

checkVar5 = StringVar()
check5 = Checkbutton(window, text="Ham ($1)", variable=checkVar5)
check5.deselect()

check1.place(x=15, y=215)
check2.place(x=150, y=215)
check3.place(x=15, y=255)
check4.place(x=150, y=255)
check5.place(x=15, y=295)


#function to check user's choice
def checkTotal():
    totalPrice = 0
    topping_list = []

    if checkVar1.get() == '1':
        totalPrice += 1
        topping_list.append('Pepperoni')

    if checkVar2.get() == '1':
        totalPrice += 0
        topping_list.append('Cheese')

    if checkVar3.get() == '1':
        totalPrice += 1
        topping_list.append('Olive')

    if checkVar4.get() == '1':
        totalPrice += 1
        topping_list.append('Pineapple')

    if checkVar5.get() == '1':
        totalPrice += 1
        topping_list.append('Ham')

#pizza size price add
    if combo_size.get() == 'extra-large (+$17.50)':
        totalPrice += 17.50
    elif combo_size.get() == 'large (+$15)':
        totalPrice += 15
    elif combo_size.get() == 'medium (+$12.50)':
        totalPrice += 12.50
    else:
        totalPrice += 9

#message alert showing total order
    msg = "You choose " + combo_size.get() + " size with\n ", topping_list, "\nYour total price is $" + str(totalPrice)
    messagebox.showinfo('Price', msg)
    

#buttons
btn_order = Button(window, text="Order Now", command=checkTotal)
btn_order.place(x=70, y=365, width=150, height=25)



window.mainloop()