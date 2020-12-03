from tkinter import * 
from v1 import proceed_arguments
from utils import read_data_as_list

data = read_data_as_list('Covid_.txt')

def search():
  try:
    area.config(text=proceed_arguments(search_query.get(), data, int(days_input.get()) if days_input.get().isnumeric() else 10))
  except Exception as err:
    area.config(text=err)

root = Tk()
root.title('Covid')
root.geometry('700x400')

font = ('Consolas', 16)

frame = Frame(root)
frame.pack(pady=20)

search_query = StringVar(root)
days_input = StringVar(root)

inp = Entry(frame, textvariable=search_query, font=font, width=35)
inp.pack(side=LEFT, fill='x')

days = Entry(frame, textvariable=days_input, font=font, width=5)
days.pack(side=LEFT)

btn = Button(frame, text='Search', command=search, font=font)
btn.pack(side=LEFT)

area = Label(text='Nothing to show', font=('Arial', 13), justify=LEFT)
area.pack(fill=Y, expand=1)

root.mainloop()