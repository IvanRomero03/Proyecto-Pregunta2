import tkinter as tk
import tkinter_renderers as tkrd

#init y config del mainframe
mf = tk.Tk()
mf.geometry("600x600")
mf.title("Pregunta2")
mf.resizable(0, 0)
mf.config(bg=tkrd.bgcol)
mf.columnconfigure((0, 1), weight=1)
mf.rowconfigure((0, 1), weight=1)

#main loop
tkrd.frame_call(0, mf)
mf.mainloop()

print("Fin render")
