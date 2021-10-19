import tkinter as tk
import tkinter_renderers as tkrd
import os

#init y config del mainframe
mf = tk.Tk()
mf.geometry("1000x600")
mf.title("Pregunta2")
mf.resizable(0, 0)
mf.config(bg=tkrd.bgcol)
mf.columnconfigure((0, 1), weight=1)
mf.rowconfigure((0, 1), weight=1)

idir = os.getcwd() + r"\Proyecto-pregunta2\resources\ffsfinal.xbm"
fondo = tk.Image(file=idir, imgtype="bitmap")
fondo_lbl = tk.Label(mf, image=fondo)
fondo_lbl.place(x=-2, y=-2)

#main loop
tkrd.frame_call(0, mf)
mf.mainloop()

print("Fin render")
