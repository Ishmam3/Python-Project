from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser

#def for filemenu
def openfile():
    file = filedialog.askopenfilename()
    fileopen = open(file, "r")
    print(fileopen.read())
    fileopen.close()

def savefile():
    filepath = filedialog.asksaveasfile(filetypes=[
        ("Text file", ".txt"),
        ("Html file", ".html"),
        ("Allfile", "*.*")    
        ])
    file = textarea.get(1.0, END)
    filepath.write(file)
    filepath.close()
#End

#def for editmenu
def cut():
    pass

def copy():
    pass

def paste():
    pass

def fcolor():
    color = colorchooser.askcolor()
    colorhx = color[1]
    textarea.config(fg=colorhx)
#end

#def for formatmenu
def wordwarp():
    pass

def font():
    pass
#End

window = Tk()
window.title("Notepad by Ishmam")
menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)
editmenu.add_command(label="Choice color", command=fcolor)

formatmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Format", menu=formatmenu)
formatmenu.add_command(label="Word Warp", command=wordwarp)
formatmenu.add_command(label="Font...", command=font)

textarea = Text(window, font=("Arial"))
textarea.pack()

window.mainloop()