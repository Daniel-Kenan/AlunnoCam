from tkinter import * 
import ctypes
import sys

myappid="Daniel.Kenan.Slinda"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
window = Tk()
window.resizable(False,False)
window.geometry("700x250")
favicon = sys.path[0] + "\\favicon.ico"
window.iconbitmap(favicon)
window.title("Wink")
window.mainloop()
