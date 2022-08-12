from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('Digital Clock')

def update_time():
    main_text.config(text=(strftime('%H:%M:%S %p')))
    main_text.after(1000, update_time)

main_text = Label(root, font=('consolas', 40, 'bold'), foreground='cyan')
main_text.pack(anchor=CENTER, padx=20, pady=20)

update_time()

root.mainloop()