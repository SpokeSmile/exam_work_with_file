import tkinter as tk


window = tk.Tk()

content = tk.Text(window)
content.place(relx=1,rely=1)



main_menu = tk.Menu(window)

file_menu = tk.Menu(main_menu)
file_menu.add_command(label="Открыть файл")




main_menu.add_cascade(label='Файл', menu=file_menu)
window.config(menu=main_menu)


window.mainloop()
