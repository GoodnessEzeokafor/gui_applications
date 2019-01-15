from tkinter import *
import os
import tkinter.filedialog
import tkinter.messagebox as tmb


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
PROGRAM_NAME = " Gudnex Editor"
FILE_NAME = None

#callbacks functions
def cut():
    ''' cut functinoality'''
    content_text.event_generate("<<Cut>>")

def paste():
    ''' Paste functionality'''
    content_text.event_generate("<<Paste>>")

def redo(event=None):
    content_text.event_generate("<<Redo>>")
    return 'break'


def select_all(event=None):
    '''Highlights'''
    content_text.tag_add('sel', '1.0', 'end')
    return "break"

def search_output(needle, if_ignore_case, content_text, search_toplevel, search_box):
    content_text.tag_remove('match', '1.0', END)
    matches_found = 0
    if needle:
        start_pos = '1.0'
        while True:
            start_pos = content_text.search(needle, start_pos, nocase=if_ignore_case, stopindex=END)
            if not start_pos:
                break
            end_pos = '{}+{}c'.format(start_pos, len(needle))
            content_text.tag_add('match', start_pos, end_pos)
            matches_found += 1
            start_pos = end_pos
        content_text.tag_config(
            'match', foreground='red', background='yellow'
        )
    search_box.focus_set()
    search_toplevel.title('{} matches found'.format(matches_found))


def find_text(event=None):
    search_toplevel = Toplevel(root)
    search_toplevel.title("Find Text")
    search_toplevel.transient(root)
    search_toplevel.resizable(False, False)
    Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')
    search_entry_widget=Entry(search_toplevel, width=25)
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
    search_entry_widget.focus_set()
    ignore_case_value = IntVar()
    Checkbutton(search_toplevel,
     text="Ignore Case", 
     variable=ignore_case_value).grid(row=1, column=1,sticky='e',padx=2,pady=2)
    Button(
        search_toplevel, 
        text="Find All",
        underline=0,
        command= lambda: search_output(
            search_entry_widget.get(),
            ignore_case_value.get(),
            content_text, search_toplevel, search_entry_widget)
    ).grid(row=0, column=2, sticky='e' + 'w', padx=2, pady=2)

def close_search_window():
    content_text.tag_remove('match', '1.0', END)
    search_toplevel.destroy()
    search_toplevel.protocol("WM_DELETE_WINDOW", close_search_window)
    return "break"


def write_to_file(FILE_NAME):
    try:
        content = content_text.get(1.0, 'end')
        with open(FILE_NAME, 'w') as the_file:
            the_file.write(content)
    except IOError:
        pass

def open_file(event=None):
    input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".py",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if input_file_name:
        global FILE_NAME
        FILE_NAME = input_file_name
        root.title('{} - {}'.format(os.path.basename(FILE_NAME), PROGRAM_NAME))
        content_text.delete(1.0, END)
        with open(FILE_NAME) as _file:
            content_text.insert(1.0, _file.read())

def save_as(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if input_file_name:
        global FILE_NAME
        FILE_NAME = input_file_name
        write_to_file(FILE_NAME)
        root.title("{} - {}".format(os.path.basename(FILE_NAME), PROGRAM_NAME))
    return "break"

def save(event=None):
    global FILE_NAME
    if not FILE_NAME:
        save_as()
    else:
        write_to_file(FILE_NAME)
    return "break"

def new_file(event=None):
    root.title("Untitled")
    global FILE_NAME
    FILE_NAME = None
    content_text.delete(1.0, END)

def display_about_messagebox(event=None):
    tkinter.messagebox.showinfo(
        "About", "{}{}".format(PROGRAM_NAME, "\nGudnex Development Application Editor")
    )

def display_help_messagebox(event=None):
    tkinter.messagebox.showinfo(
        "Help", "Help Book: \nGudnex Development Application Editor"
    )
def exit_editor(event=None):
    if tkinter.messagebox.askokcancel("Quit?", "Really quiz?"):
        root.destroy()

def close_editor(event=None):
    root.protocol('WM_DELETE_WINDOW', exit_editor)

def on_content_changed(event=None):
    update_line_numbers()
def update_line_numbers():
    line_numbers = get_line_numbers()
    line_number_bar.config(state="normal")
    line_number_bar.delete('1.0', 'end')
    line_number_bar.insert('1.0', line_numbers)
    line_number_bar.config(state='disabled')

def get_line_numbers():
    output = ''
    if show_line_number.get():
        row,col = content_text.index("end").split("-")
        for i in range(1, int(row)):
            output += str(i) + "\n"
    return output

def highlight_line(interval=100):
    content_text.tag_remove("active_line", 1.0, "end")
    content_text.tag_add("active_line", "insert linestart", "insert lineend+1c")
    content_text.after(interval, toggle_highlight)

def undo_highlight():
    content_text.tag_remove("active_line", 1.0, "end")
def toggle_highlight(event=None):
    if to_highlight_line.get():
        highlight_line()
    else:
        undo_highlight()
    

root = Tk()
root.title(PROGRAM_NAME)  # sets the title of the gui app
#adding menu in the widget
menu_bar = Menu(root)



to_highlight_line = BooleanVar()
show_line_number = IntVar()
show_line_number.set(1)

#File Menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(
    label="New File",
    accelerator="Ctrl+N",
    compound="left",
    command=new_file
)
file_menu.add_command(label="New Window", accelerator="Ctrl+Shift+N",compound="left")
file_menu.add_separator()
file_menu.add_command(
    label="Open File", 
    accelerator="Ctrl+O",
    compound="left",
    command=open_file
)
file_menu.add_command(
    label="Save",
    accelerator="Ctrl+S",
    compound="left",
    command=save)
file_menu.add_command(
    label="Save as",
    accelerator="Shift+Ctrl+S",
    compound="left",
    command=save_as)
        
file_menu.add_separator()
file_menu.add_command(
    label="Exit",
    accelerator="Ctrl+Q",
    compound="left",
    command=exit_editor
)


#Edit Menu

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", compound="left")
edit_menu.add_command(
    label="Redo",
    accelerator="Ctrl+Y",
    compound="left",
    command=redo
)
edit_menu.add_separator()
edit_menu.add_command(
        label="Cut", 
        accelerator="Ctrl+X",
        compound="left",
        command=cut
)
edit_menu.add_command(label="Copy", accelerator="Ctrl+C",compound="left")
edit_menu.add_command(
    label="Paste", 
    accelerator="Ctrl+V",
    compound="left",
    command=paste
)
edit_menu.add_separator()
edit_menu.add_command(
    label="Find",
    accelerator="Ctrl+F",
    compound="left",
    command=find_text
)
edit_menu.add_separator()
edit_menu.add_command(
    label="Select All", 
    accelerator="Ctrl+A",
    compound="left", 
    underline=7,
    command=select_all
)

#View Menu
view_menu = Menu(menu_bar, tearoff=0)
view_menu.add_checkbutton(
    label="Show Line Number")
view_menu.add_checkbutton(
    label="Highlight Current Number",
    variable = to_highlight_line,
    onvalue=1,
    offvalue=0,
    command=toggle_highlight
)
view_menu.add_checkbutton(label="Show Line Number", variable=show_line_number)

# view_menu.add_cascade(label="Themes", menu=themes_menu)
# themes_menu.add_radiobutton(label="Default", variable=theme_name)

#About Menu
about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(
    label="About",
    compound="left",
    command=display_about_messagebox)
    
about_menu.add_command(
    label="Help",
    compound="left",
    command=display_help_messagebox
)

#all ile menu-items will be added here next
menu_bar.add_cascade(label="File", menu=file_menu) # file menu
menu_bar.add_cascade(label="Edit", menu=edit_menu) # Edit menu
menu_bar.add_cascade(label="View", menu=view_menu) # view menu
menu_bar.add_cascade(label="About", menu=about_menu) # about menu


#shortcut bar
shortcut_bar = Frame(root, height=25, background='grey')
shortcut_bar.pack(expand='no', fill='x')
line_number_bar = Text(
    root,
    width=4, 
    padx=3,
    takefocus=0, 
    border=0,
    state="disabled",
    background='grey'
)
line_number_bar.pack(side='left', fill='y')
content_text = Text(root, wrap='word', undo=1)
content_text.pack(expand='yes', fill='both')
content_text.bind("<Control-y>", redo) # binds the redo
content_text.bind("<Control-Y>", redo)
content_text.bind("<Control-A>", select_all)
content_text.bind("<Control-a>", select_all)
content_text.bind("<Control-f>", find_text)
content_text.bind("<Control-F>", find_text)
content_text.bind("<Control-O>", open_file)
content_text.bind("<Control-o>", open_file)
content_text.bind("<Control-N>", new_file)
content_text.bind("<Control-n>", new_file)
content_text.bind("<Control-S>", save)
content_text.bind("<Control-s>", save)
content_text.bind("<KeyPress-F1>", display_help_messagebox)
content_text.bind("<Any-KeyPress>", on_content_changed)
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')

root.config(menu=menu_bar)



root.mainloop()