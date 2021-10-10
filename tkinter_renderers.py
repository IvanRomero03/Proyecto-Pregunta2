import tkinter as tk

bgcol = "#7BD09E"
btbgcol = "#6BC08E"

def parse_preg(file, pos, n, concat):
    vsenten_arr = []
    file.seek(pos)
    for i in range(n):
        vsenten = file.read(i)
        vsenten_arr.append(vsenten)
    if concat == 'l':
        vconcat_arr = []
        for i in range(len(vsenten_arr)):
            vconcat_arr.append(vsenten_arr[i] + "\n")
        return vconcat_arr
    elif concat == 's':
        vconcat_arr = []
        for i in range(len(vsenten_arr)):
            vconcat_arr.append(vsenten_arr[i] + " ")
        return vconcat_arr
    elif concat == 'w':
        return vsenten_arr

def do_game(win):

    win.rowconfigure(0, weight=2)
    win.rowconfigure((1, 2, 3, 4), weight=1)
    win.columnconfigure((0, 1, 2), weight=1)

    numpr = 1

    numpr_str = tk.StringVar()
    numpr_str.set("Pregunta " + str(numpr))
    gtit = tk.Label(win, textvariable=numpr_str, font=('Helvetica bold', 30))
    gtit.grid(column=1, row=0)


def do_credits(win):

    win.rowconfigure(0, weight=1)
    win.rowconfigure(1, weight=5)
    win.columnconfigure(0, weight=1)

    namelbl = tk.Label(win, text="nombres",
                       font=("Copperplate", 10))

    namelbl.grid(row=1, column=0)


def do_menu(win):

    win.columnconfigure((0, 1), weight=1)
    win.rowconfigure((2, 3), weight=2)
    win.rowconfigure((0, 1, 4, 5), weight=1)

    tit = tk.Label(win, text="Pregunta2\nTec", font=('Copperplate', 30), bg=bgcol)
    tit.grid(column=0, row=0, columnspan="2", rowspan="2")

    but = tk.Button(win, text="Iniciar juego", font=('Helvetica bold', 20),
                    bg=btbgcol)
    but.grid(column=0, row=2, columnspan="2")

    but = tk.Button(win, text="Créditos", font=('Helvetica bold', 20), bg=btbgcol)
    but.grid(column=0, row=3, columnspan="2", sticky=tk.N)

    but2 = tk.Button(win, text="Salir", font=('Helvetica bold', 20),
                     fg="#FF0000", command=lambda: win.destroy())
    but2.grid(column=1, row=4, rowspan="2")
