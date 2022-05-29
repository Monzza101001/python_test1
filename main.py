from tkinter import *

main = Tk()


def button_clicked():
    text = Label(main, text='The button has been clicked')
    text.pack()


button_one = Button(main, text='click me', fg='violet', bg='black', command=button_clicked)

button_one.pack()

button_two = Button(main, text='click me', fg='red', bg='white', command=button_clicked)

button_two.pack(padx=50, pady=50)

main.mainloop()
