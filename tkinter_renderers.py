import tkinter as tk
from str_src import wd
from lorddanlib import parse_string_to_list as p_str

bgcol = "#7BD09E"
btbgcol = "#6BC08E"

def frame_call(frame_index, win):
    ele_list = win.winfo_children()
    for x in range(len(ele_list)):
        ele_list[x].grid_forget()

    if frame_index == 0:
        do_menu(win)
    elif frame_index == 1:
        do_game(win)
    elif frame_index == 2:
        do_credits(win)

def do_game(win):

    win.columnconfigure((0, 1, 2), weight=1)
    win.rowconfigure(0, weight=2)
    win.rowconfigure((1, 2, 3, 4, 5), weight=1)

    numpr = 1

    dict_str = "Pregunta " + str(numpr)
    preg_src = p_str(wd[dict_str], "$")

    preglbl = tk.Label(win, text=preg_src[0], font=('Helvetica bold', 30), bg=bgcol)
    preglbl.grid(column=0, row=0, columnspan=3)

    for i in range(4):
        vbut = tk.Button(win, text=preg_src[i + 1], font=('Helvetica bold', 20), bg=btbgcol)
        vbut.grid(column=0, row=i + 1, columnspan=3)

    but2 = tk.Button(win, text="Salir", font=('Helvetica bold', 20),
                     fg="#FF0000", command=lambda: win.destroy(), bg=btbgcol)
    but2.grid(column=2, row=5)


def do_credits(win):

    win.columnconfigure((0, 2), weight=1)
    win.columnconfigure(1, weight=3)
    win.rowconfigure((0, 2, 3), weight=1)
    win.rowconfigure(1, weight=3)

    namelbl = tk.Label(win, text=wd["nombres"],
                       font=("Copperplate", 15), bg=bgcol)

    namelbl.grid(row=1, column=1)

    ret_but = tk.Button(win, text="Regresar al menu", font=('Helvetica bold', 20),
                        bg=btbgcol, command=lambda: frame_call(0, win))
    ret_but.grid(row=2, column=1)


def do_menu(win):

    win.columnconfigure((0, 1, 2), weight=1)
    win.rowconfigure(1, weight=2)
    win.rowconfigure((0, 2, 3, 4), weight=1)

    tit = tk.Label(win, text="Pregunta2\nTec", font=('Copperplate', 30), bg=bgcol)
    tit.grid(column=0, row=1, columnspan=3)

    game_but = tk.Button(win, text="Iniciar juego", font=('Helvetica bold', 20),
                         bg=btbgcol, command=lambda: frame_call(1, win))
    game_but.grid(column=0, row=2, columnspan=3)

    cred_but = tk.Button(win, text="Créditos", font=('Helvetica bold', 20),
                         bg=btbgcol, command=lambda: frame_call(2, win))
    cred_but.grid(column=0, row=3, sticky=tk.N, columnspan=3)

    but2 = tk.Button(win, text="Salir", font=('Helvetica bold', 20),
                     fg="#FF0000", command=lambda: win.destroy(), bg=btbgcol)
    but2.grid(column=2, row=4)