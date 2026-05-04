import tkinter.filedialog as tkfd


def open_file() -> str:
    file_path = tkfd.askopenfilename()
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    

def menu_open_file(content_text):
    content_text.insert(1.0, open_file())
