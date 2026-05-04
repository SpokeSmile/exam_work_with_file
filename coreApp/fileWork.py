import tkinter.filedialog as tkfd


def open_file() -> str:
    file_path = tkfd.askopenfilename()
    with open(file_path, 'r') as file:
        return file.read()
    

def menu_open_file(content_text):
    content_text.insert(0, open_file())
