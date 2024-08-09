from tkinter import *
from tkinter import ttk

GUI = Tk()
w = 700
h = 500

ws = GUI.winfo_screenwidth() #screen width
hs = GUI.winfo_screenheight() #screen height

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y+20:.0f}')
GUI.title('Uncle Flashcard by Uncle Engineer')

L = ttk.Label(GUI,text='Uncle Flashcard by Uncle Engineer',font=(None,20))
L.pack(pady=100)

GUI.mainloop()