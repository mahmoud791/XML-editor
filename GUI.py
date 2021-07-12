from os import path
from validate import validate
from Convert import*
from tkinter import*
from formate import*



def check_consistency():
    path = pathentry.get()
    validate(s=path)

def Convert_to_JSON():
    path = pathentry.get()
    convert(s=path)

def prettify():
    path = pathentry.get()
    formate(s=path)



window = Tk()

window.title("XML Editor")
window.geometry('250x300')

lbl = Label(window, text="Path: ")
lbl.grid(column=0, row=0)

pathentry = Entry(window,width=30)
pathentry.grid(row=0,column=1)

validate_button = Button(window, text='check consistensy',width=15,command=check_consistency)
validate_button.grid(row=1,column=1)


prettify_Button = Button(window, text='Prettify',width=15,command=prettify)
prettify_Button.grid(row=2,column=1)


Convert_to_JSON = Button(window, text='convert to JSON',width=15,command=Convert_to_JSON)
Convert_to_JSON.grid(row=3,column=1)

minify_Button = Button(window, text='Minify',width=15)
minify_Button.grid(row=4,column=1)

compress_Button = Button(window, text='Compress',width=15)
compress_Button.grid(row=5,column=1)





window.mainloop()