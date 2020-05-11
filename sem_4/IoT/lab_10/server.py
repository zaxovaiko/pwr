import sqlite3
import sys
import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt
from datetime import datetime
import csv
import time
import re
import os
from dotenv import load_dotenv


def run_server():
    def on_message(client, userdata, message):
        topic = message.topic
        payload = message.payload.decode("utf-8")

        if topic == os.getenv('TOPIC_CARD') and payload.isdigit():
            user = con.cursor().execute(f'SELECT * FROM workers WHERE card_id = {payload}').fetchall()
            con.execute('INSERT INTO records (card_id, worker_id) VALUES ({}, {})'
                        .format(payload, user[0][0] if len(user) != 0 else "NULL"))
            con.commit()
            print('Card ID_' + payload + ' time: ' + datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
        elif topic == os.getenv('TOPIC_AUTH'):
            user = payload.split(',')
            client.publish(
                os.getenv('TOPIC_RES'),
                'Success' if user[0] == os.getenv('USER') and user[1] == os.getenv('PASS') else 'Error')

    window = tk.Tk()
    window.title('Server')
    window.resizable(False, False)

    terminal_label = tk.Label(window, text='Terminal is not connected yet.')
    terminal_label.grid(column=0, row=0, columnspan=6, padx=15, sticky='nsew', pady=15)

    def add_worker():
        subwindow = tk.Tk()
        subwindow.title('Add worker')
        subwindow.resizable(False, False)

        worker_name_textfield = tk.Entry(subwindow)
        worker_name_textfield.grid(column=3, row=1, columnspan=3, padx=(0, 15), pady=(15, 5), sticky='news')
        tk.Label(subwindow, text='Worker Name').grid(column=1, row=1, columnspan=1, padx=(15, 5), pady=(15, 5))

        def check_fields():
            worker_name = worker_name_textfield.get()
            if worker_name != '':
                con.execute(f'INSERT INTO workers (name) VALUES ("{worker_name}")')
                con.commit()
                terminal_label.config(text='Worker was added.')
            else:
                terminal_label.config(text='Name can not be empty.')
            subwindow.destroy()

        tk.Button(subwindow, text='Add worker', command=check_fields).grid(column=3, row=4, columnspan=5, pady=(5, 15))
        subwindow.mainloop()

    def remove_worker():
        subwindow = tk.Tk()
        subwindow.title('Remove worker')
        subwindow.resizable(False, False)

        workers = list(
            map(lambda x: f'ID={x[0]}, {x[1]}', con.execute('SELECT * FROM workers ORDER BY name').fetchall()))
        workers_combobox = ttk.Combobox(subwindow, values=workers)
        workers_combobox.grid(column=3, row=1, columnspan=3, padx=(0, 15), pady=(15, 5), sticky='news')

        tk.Label(subwindow, text='Worker').grid(column=1, row=1, columnspan=1, padx=(15, 5), pady=(15, 5))

        def check_field():
            worker_id = list(map(int, re.findall(r'\d+', workers_combobox.get().split(',')[0])))[0]
            con.execute(f'DELETE FROM workers WHERE id = {worker_id}')
            con.commit()
            terminal_label.config(text='Worker was removed.')
            subwindow.destroy()

        tk.Button(subwindow, text='Remove worker', command=check_field).grid(column=4, row=4, pady=(5, 15))
        subwindow.mainloop()

    def pin_card():
        subwindow = tk.Tk()
        subwindow.title('Pin card')
        subwindow.resizable(False, False)

        workers = list(map(lambda x: f'ID={x[0]}, {x[1]}',
                           con.execute('SELECT * FROM workers WHERE card_id IS NULL ORDER BY name').fetchall()))
        workers_combobox = ttk.Combobox(subwindow, values=workers)
        workers_combobox.grid(column=3, row=1, columnspan=3, padx=(0, 15), pady=(15, 5), sticky='news')

        cards = list(map(lambda x: f'ID={x[0]}, {x[1]}',
                         con.execute('SELECT * FROM cards WHERE worker_id IS NULL ORDER BY id').fetchall()))
        cards_combobox = ttk.Combobox(subwindow, values=cards)
        cards_combobox.grid(column=3, row=2, columnspan=3, padx=(0, 15), pady=(15, 5), sticky='news')

        tk.Label(subwindow, text='Worker').grid(column=1, row=1, columnspan=1, padx=(15, 5), pady=(15, 5))
        tk.Label(subwindow, text='Card').grid(column=1, row=2, columnspan=1, padx=(15, 5), pady=(15, 5))

        def check_field():
            worker_id = list(map(int, re.findall(r'\d+', workers_combobox.get().split(',')[0])))[0]
            card_id = list(map(int, re.findall(r'\d+', cards_combobox.get().split(',')[0])))[0]
            con.execute(f'UPDATE workers SET card_id = {card_id} WHERE id = {worker_id}')
            con.execute(f'UPDATE cards SET worker_id = {worker_id} WHERE id = {card_id}')
            con.commit()
            terminal_label.config(text='Card was pinned.')
            subwindow.destroy()

        tk.Button(subwindow, text='Pin card to worker', command=check_field).grid(column=4, row=3, pady=(5, 15))
        subwindow.mainloop()

    def unpin_card():
        subwindow = tk.Tk()
        subwindow.title('Unpin card')
        subwindow.resizable(False, False)

        workers = list(
            map(lambda x: f'ID={x[0]}, {x[1]}', con.execute('SELECT * FROM workers ORDER BY name').fetchall()))
        workers_combobox = ttk.Combobox(subwindow, values=workers)
        workers_combobox.grid(column=3, row=1, columnspan=3, padx=(0, 15), pady=(15, 5), sticky='news')

        tk.Label(subwindow, text='Worker').grid(column=1, row=1, columnspan=1, padx=(15, 5), pady=(15, 5))

        def check_field():
            worker_id = list(map(int, re.findall(r'\d+', workers_combobox.get().split(',')[0])))[0]
            con.execute(f'UPDATE workers SET card_id = NULL WHERE id = {worker_id}')
            con.commit()
            terminal_label.config(text='Card was unpinned.')
            subwindow.destroy()

        tk.Button(subwindow, text='Unpin card', command=check_field).grid(column=4, row=4, pady=(5, 15))
        subwindow.mainloop()

    def make_report():
        records = con.cursor().execute('SELECT * FROM records').fetchall()
        print('Report was made.')
        with open('report.csv', 'w', newline='') as f:
            wr = csv.DictWriter(f, fieldnames=['id', 'card_id', 'user_id', 'timestamp'])
            wr.writeheader()
            for record in records:
                wr.writerow({
                    "id": record[0],
                    "card_id": record[1],
                    "user_id": record[2] if record[2] else 'Anonymous',
                    "timestamp": record[3]
                })
            terminal_label.config(text='Report was created.')

    def stop():
        client.loop_stop()
        client.disconnect()
        con.close()
        sys.exit(0)

    tk.Button(window, text='Add worker', command=add_worker).grid(column=0, row=1, sticky='nsew', padx=(15, 0))
    tk.Button(window, text='Remove worker', command=remove_worker).grid(column=1, row=1, sticky='nsew', padx=(0, 15))
    tk.Button(window, text='Pin card', command=pin_card).grid(column=0, row=2, sticky='nsew', padx=(15, 0))
    tk.Button(window, text='Unpin card', command=unpin_card).grid(column=1, row=2, sticky='nsew', padx=(0, 15))
    tk.Button(window, text='Make report', command=make_report).grid(column=0, row=3, sticky='nsew', padx=(15, 0),
                                                                    pady=(0, 15))
    tk.Button(window, text='Stop', command=stop).grid(column=1, row=3, sticky='nsew', pady=(0, 15), padx=(0, 15))

    def on_connect(client, ud, flags, rc):
        terminal_label.config(text=mqtt.connack_string(rc))

    client = mqtt.Client()
    client.tls_set(os.getenv('CERTIFICATE'))
    client.username_pw_set(username=os.getenv('SERVER_USER'), password=os.getenv('SERVER_PASS'))
    client.on_connect = on_connect
    client.on_message = on_message

    con = sqlite3.connect(os.getenv('DB_NAME'), check_same_thread=False)

    while True:
        try:
            client.connect(os.getenv('BROKER'), int(os.getenv('PORT')))
            break
        except ConnectionRefusedError:
            print('Connection error.')
        time.sleep(1)

    client.loop_start()
    client.subscribe(os.getenv('TOPIC_CARD'))
    client.subscribe(os.getenv('TOPIC_AUTH'))

    window.mainloop()


if __name__ == '__main__':
    load_dotenv()
    run_server()
