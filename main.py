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

def frame_call(frame_index):
    ele_list = mf.winfo_children()
    for x in range(len(ele_list)):
        ele_list[x].grid_forget()
    if frame_index == 0:
        tkrd.do_menu(mf)
    elif frame_index == 1:
        tkrd.do_game(mf)
    elif frame_index == 2:
        tkrd.do_credits(mf)

#main loop
#Ivan, cambia el indice en frame_call pa que se vean las distintas pantallas

frame_call(1)
mf.mainloop()
print("Fin render")
