from tkinter import *
from tkinter import filedialog, messagebox
from datetime import datetime
import os
from helpers.proceed_query import proceed_arguments


def read_actions_from_file(filename):
    try:
        return open(filename).read().split('\n')
    except Exception:
        return []


def write_actions_to_file(filename, actions):
    file = open(filename, 'w')
    file.write('\n'.join(actions))


def execute_find():
    if len(content) == 0:
        messagebox.showerror('File was not chosen',
                             'You need to read file first.')
        return logs_box.insert(logs_box.size(), make_log_string('File was not chosen.'))

    if type(content) != list:
        messagebox.showerror('Wrong file',
                             'Choose another file or check this one.')
        return logs_box.insert(logs_box.size(), make_log_string('Choose another file or check this one.'))

    try:
        query = query_entry.get()
        actions.append(query)
        write_actions_to_file(ACTIONS_FILENAME, actions)
        logs_box.insert(logs_box.size(), make_log_string(f'Typed: {query}'))
        actions_box.insert(actions_box.size(), query)
        res = proceed_arguments(query, content)
        output.config(text=res)
    except Exception as e:
        messagebox.showerror('Error has occured', e)
        logs_box.insert(logs_box.size(), make_log_string(e))


def get_current_time():
    return datetime.now().strftime("%H:%M:%S")


def make_log_string(s):
    return '[{}] {}'.format(get_current_time(), s)


def get_file_content():
    file = filedialog.askopenfile(parent=root, initialdir=os.getcwd(
    ), title="Please select a file:", filetypes=[('all files', '.*'), ('text files', '.txt')])

    global content
    content = list(map(lambda x: x.split('\t'), file.read().split('\n')[1:]))
    logs_box.insert(logs_box.size(), make_log_string(
        f'File {file.name} was chosen.'))


def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


def show_help():
    messagebox.showinfo(
        "Help information", "Use: <kraj|kontynent|swiat> <zgony|zachorowania> <dzien|miesiac|wszystkie>, <days>")


def show_about():
    messagebox.showinfo(
        "About program", "Author - Volodymyr Zakhovaiko\nLab 11")


def use_selected_action():
    try:
        query = actions[actions_box.curselection()[0]]
        query_entry_text.set(query)
        logs_box.insert(logs_box.size(), make_log_string(
            f'Query "{query}" were used'))
    except Exception:
        messagebox.showerror('Error has occured',
                             'You did not choose any query')
        logs_box.insert(logs_box.size(), make_log_string(
            'You did not choose any query'))


def remove_selected_action():
    try:
        idx = actions_box.curselection()[0]
        ans = messagebox.askyesno(
            'Remove query', 'Do you want to remove query from the list?')
        if ans:
            action = actions.pop(idx)
            actions_box.delete(idx)
            logs_box.insert(logs_box.size(), make_log_string(
                f'Query "{action}" were removed'))
            write_actions_to_file(ACTIONS_FILENAME, actions)
    except Exception:
        messagebox.showerror('Error has occured',
                             'You did not choose any query')
        logs_box.insert(logs_box.size(), make_log_string(
            'You did not choose any query'))


if __name__ == '__main__':
    ACTIONS_FILENAME = 'actions.txt'

    root = Tk()
    root.title('Lab 11')
    root.geometry('600x400')

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=get_file_content)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Use", command=use_selected_action)
    editmenu.add_command(label="Remove", command=remove_selected_action)
    menubar.add_cascade(label="Query", menu=editmenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help", command=show_help)
    helpmenu.add_command(label="About", command=show_about)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)

    # Main frames
    left_frame = Frame(root)
    left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    right_frame = Frame(root)
    right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=2)
    root.grid_rowconfigure(0, weight=1)

    # Left frame
    actions_box = Listbox(left_frame)
    actions_box.grid(row=0, column=0, columnspan=2,
                     sticky='nsew', padx=5, pady=5)

    logs_box = Listbox(left_frame)
    logs_box.grid(row=2, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)

    useBtn = Button(left_frame, text='Use', command=use_selected_action)
    useBtn.grid(row=1, column=0, sticky='nsew', padx=5)

    removeBtn = Button(left_frame, text='Remove',
                       command=remove_selected_action)
    removeBtn.grid(row=1, column=1, sticky='nsew', padx=5)

    left_frame.grid_columnconfigure(0, weight=1)
    left_frame.grid_columnconfigure(1, weight=1)
    left_frame.grid_rowconfigure(0, weight=1)
    left_frame.grid_rowconfigure(1, weight=0)
    left_frame.grid_rowconfigure(2, weight=1)

    # Right frame
    output = Label(right_frame)
    output.config(text='Start typing...')
    output.grid(row=0, column=0, columnspan=2,  sticky='nsew')

    query_entry_text = StringVar()
    query_entry = Entry(right_frame, textvariable=query_entry_text)
    query_entry.grid(row=1, column=0, sticky='nsew', pady=5)

    query_find_btn = Button(right_frame, text='Find',
                            width=10, pady=5, command=execute_find)
    query_find_btn.grid(row=1, column=1, sticky='sw')

    right_frame.grid_columnconfigure(0, weight=1)
    right_frame.grid_rowconfigure(0, weight=1)
    right_frame.grid_rowconfigure(1, weight=0)

    content = ''
    actions = read_actions_from_file(ACTIONS_FILENAME)
    [actions_box.insert(i, a) for i, a in enumerate(actions)]

    root.mainloop()
