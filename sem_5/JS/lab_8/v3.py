from tkinter import * 
from v1 import proceed_arguments
from utils import read_data_as_list

data = read_data_as_list('Covid_.txt')

def search():
  try:
    area.config(text=proceed_arguments(search_query.get(), data))
  except Exception as err:
    area.config(text=err)

root = Tk()
root.title('Covid')
root.geometry('700x400')

font = ('Consolas', 16)

frame = Frame(root)
frame.pack(pady=20)

# Search query input
search_query = StringVar(root)
inp = Entry(frame, textvariable=search_query, font=font)
inp.pack(side=LEFT, fill='x')

# Search btn
btn = Button(frame, text='Search', command=search, font=font)
btn.pack(side=LEFT)

# Area to insert result
area = Label(text='Nothing to show', font=('Arial', 13), justify=LEFT)
area.pack(fill=Y, expand=1)

root.mainloop()