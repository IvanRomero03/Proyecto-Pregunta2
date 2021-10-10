import tkinter as tk


def do_menu(win):

    menu_fr = tk.Frame(win, bg="#7BD09E")
    menu_fr.pack()

    texo2 = tk.StringVar()
    texo2.set("Pregunta2")
    texto = tk.Label(menu_fr, textvariable=texo2, font=(
        'Helvetica bold', 60), background="#7BD09E")
    texto.pack()

    ltext = tk.StringVar()
    ltext.set("Menu")
    tit = tk.Label(menu_fr, textvariable=ltext, font=(
        'Helvetica bold', 40), background="#7BD09E")
    tit.pack()

    but1 = tk.Button(menu_fr, text="Iniciar juego",
                     font=('Helvetica bold', 40), fg="#FF0000")
    but1.pack()
    BotonQuitar = tk.Button(menu_fr, text="Salir",
                            font=('Helvetica bold', 40), fg="#FF0000", command=win.destroy)
    BotonQuitar.pack()
    return menu_fr


def do_game(win):

    game_fr = tk.Frame(win, bg="#7BD09E")
    game_fr.pack()

    resp = ["27", "59", "34", "82"]

    for i in range(4):
        ltext = tk.StringVar()
        ltext.set(resp[i])
        tit = tk.Label(game_fr, textvariable=ltext,
                       font=('Helvetica bold', 40))
        tit.pack()

    return game_fr
