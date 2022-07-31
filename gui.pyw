from tkinter import * 
import ctypes
import sys
from tray import AlunnaCam
import asyncio

myappid="Daniel.Kenan.Slinda"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
window = Tk()
window.resizable(False,False)
screenSIze  = "665x200"
window.geometry(screenSIze)
favicon = sys.path[0] + "\\favicon.ico"
window.iconbitmap(favicon)
window.title("AlunnoCam")
window.config(bg="#ffbd59")


def src(name):
    relative_path = 'images\\' +name+ ".png"
    return PhotoImage(file=relative_path)

DIV_BTN = Frame(window, bg="#ffbd59" , pady = 10)
DIV_BTN.pack()

def control(img, command , column = None , asvariable = False):
    row = horizontal = 0
    BTN = Button(DIV_BTN, image=img, borderwidth = 0, command=command, cursor="hand2", bg="#B08373")
    if asvariable == False:
        BTN.grid(row=row, column=column,padx=0, pady=10)
    else :return BTN
    
FILES ,VIDEOS ,SETTINGS , INFO = src('images'),src('videos'),src('settings'),src('info')
def _():pass
control( img= FILES, command=_ , column  = 0)
control( img= VIDEOS, command=_ , column= 1)
control( img= SETTINGS, command =_ ,  column= 2)
control( img= INFO, command =_ ,  column= 3)

app = AlunnaCam()
window.mainloop()
# def background():     
#      app.tray.run()
#      return window.iconify()

# window.protocol("WM_DELETE_WINDOW",background)

# async def tray():await app.tray.run()
# async def appwindow(): await window.mainloop()

# async def main():   
#     screenWindow = asyncio.create_task(tray())
#     window.mainloop()
#     await screenWindow

# asyncio.run(main())

# asyncio.run( tray())
    
