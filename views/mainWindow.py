import tkinter as tk
from coreApp import fileWork as fw

window = tk.Tk()
window.config(width=600,height=600)



content = tk.Text(window)
content.place(x=0,y=0, relwidth=1,relheight=1)



main_menu = tk.Menu(window)

file_menu = tk.Menu(main_menu)
file_menu.add_command(label="Открыть файл", command=lambda text=content: fw.menu_open_file(text))




main_menu.add_cascade(label='Файл', menu=file_menu)
window.config(menu=main_menu)


window.mainloop()
