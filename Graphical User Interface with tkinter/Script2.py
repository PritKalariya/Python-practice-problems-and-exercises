from tkinter import *

window = Tk()

def conertor():
    grams = float(input_value.get())*1000  
    pounds = float(input_value.get())*2.20462    
    ounces = float(input_value.get())*35.274

    t1.delete("1.0", END) 
    t1.insert(END,grams)

    t2.delete("1.0", END)
    t2.insert(END,pounds)

    t3.delete("1.0", END)
    t3.insert(END,ounces)


e1=Label(window,text="Kg")
e1.grid(row = 0,column = 0)

input_value = StringVar()
input = Entry(window, textvariable = input_value)
input.grid(row = 0, column = 1)

button = Button(window, text = "Convert", command = conertor)
button.grid(row = 0, column = 2)

#grams
t1 = Text(window, height = 1, width = 20)
t1.grid(row = 1, column = 0)

#pounds
t2 = Text(window, height = 1, width = 20)
t2.grid(row = 1, column = 1)

#ounces
t3 = Text(window, height = 1, width = 20)
t3.grid(row = 1, column = 2)

window.mainloop()