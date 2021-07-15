from os import path
from validate import validate
from Convert import*
from tkinter import*
from formate import*
from Minify import*
from Comperssion import*


def check_consistency(outText):
    outText.delete('1.0',END)
    path = pathentry.get()
    output = validate(s=path)
    if(len(output)):
        for i in range(len(output)):
            outText.insert(END,output[i]+'\n')
    else:
        outText.insert(END,'this file has no errors')

def Convert_to_JSON():
    path = pathentry.get()
    convert(s=path)

def prettify(outText):
    outText.delete('1.0',END)
    path = pathentry.get()
    outText.insert(END,' "Formatted.txt" is being created .... \n')
    formate(s=path)
    outText.insert(END,' "Formatted.txt" is  created successfully \n\n')
    file = open('Formatted.txt','r')
    file = file.readlines()
    for i in range(20):
        outText.insert(END,file[i])


def Minify(outText):
    outText.delete('1.0',END)
    path = pathentry.get()
    outText.insert(END,' "Minified.txt" is being created .... \n')
    reduce(s=path)
    outText.insert(END,' "Minified.txt" is  created successfully \n\n')

def compress():
    path = pathentry.get()
    getHuffmanCode(s=path)


window = Tk()

window.title("XML Editor")
window.geometry('800x600')



lbl = Label(window, text="Path:")
lbl.grid(column=0, row=0)

pathentry = Entry(window,width=100)
pathentry.grid(row=0,column=1)

validate_button = Button(window, text='Validate',width=10,command= lambda : check_consistency(outText=outText))
validate_button.grid(row=1,column=2)


prettify_Button = Button(window, text='Prettify',width=10,command=lambda : prettify(outText=outText))
prettify_Button.grid(row=2,column=2)


Convert_to_JSON = Button(window, text='JSON',width=10,command=Convert_to_JSON)
Convert_to_JSON.grid(row=3,column=2)

minify_Button = Button(window, text='Minify',width=10,command=lambda : Minify(outText=outText))
minify_Button.grid(row=4,column=2)

compress_Button = Button(window, text='Compress',width=10,command=compress)
compress_Button.grid(row=5,column=2)

outText = Text(master=window)
outText.grid(row=7,column=1)




window.mainloop()