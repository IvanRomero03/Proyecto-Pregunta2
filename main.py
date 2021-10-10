import tkinter as tk
import tkinter_renderers as tkrd

# reads archivos y declaraciones
win = tk.Tk()
win.geometry("600x600")
win.config(bg="#7BD09E")

# inicializar en el menu inicial
menuinicial = tkrd.do_menu(win)
menuinicial.pack()

# funciones


def juego():
    on_game = True
    while on_game:
        print("ongame")
        a = int(input())
        if a == 2:
            on_game = not on_game
        print("")


def sw_fr1():
    for ele in win.winfo_children():
        ele.destroy()
    f1 = tkrd.do_menu(win)
    f1.pack()


def sw_fr2():
    for ele in win.winfo_children():
        ele.destroy()
    f2 = tkrd.do_game(win)
    f2.pack()


# but = tk.Button(win, text="F1", font=('Helvetica bold', 40),fg="#FF0000", command=sw_fr1)
# but.pack()

# but2 = tk.Button(win, text="F2", font=('Helvetica bold', 40),fg="#FF0000", command=sw_fr2)
# but2.pack()

# call_renderers
sw = 0

# main loop
win.mainloop()
print("Fin render")
