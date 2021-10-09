import tkinter as tk

#reads archivos y declaraciones
win = tk.Tk()
win.geometry("600x600")
#menu
ltext = tk.StringVar()
def juego():
    ltext.set("Pregunta 1")

ltext.set("Menu")
tit = tk.Label(win, textvariable=ltext, font=('Helvetica bold',40))
but1 = tk.Button(win, text="Iniciar juego", command=juego, font=('Helvetica bold',40), fg="#FF0000")
#main loop
tit.pack()
but1.pack()
win.mainloop()
print("Prueba")
