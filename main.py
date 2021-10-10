import tkinter as tk
import tkinter_renderers as tkrd

#init y config del mainframe
win = tk.Tk()
win.geometry("600x600")
win.title("Pregunta2")
win.resizable(0, 0)
win.config(bg=tkrd.bgcol)
win.columnconfigure(0, weight=1)
win.rowconfigure(0, weight=1)

#Array de frames
fr_game = tkrd.do_game(win)
fr_credits = tkrd.do_credits(win)
fr_menu = tkrd.do_menu(win)
frames = [fr_game, fr_credits, fr_menu]

def frame_call(frame_index):
    for i in range(len(frames)):
        if i == frame_index:
            frames[i].grid()
        else:
            ele_list = frames[i].winfo_children()
            for x in range(len(ele_list)):
                ele_list[x].grid_forget()

#main loop

#Ivan, cambia el indice en frame_call pa que se vean las distintas pantallas

frame_call(0)
win.mainloop()
print("Fin render")
