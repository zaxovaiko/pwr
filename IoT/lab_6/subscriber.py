import sqlite3
import sys
import tkinter as tk
import paho.mqtt.client as mqtt
from datetime import datetime
import csv

# PC (broker + saver to DB) - This is publisher file. Belongs to Raspberry Pi with RFID.


def run():
    broker = 'localhost'

    def on_connect(client, ud, flags, rc):
        terminal_label.config(text=mqtt.connack_string(rc))

    def on_message(client, ud, m):
        # here we get message from publisher
        card_id = m.payload.decode("utf-8")
        user = con.cursor().execute(f'SELECT * FROM workers WHERE card_id = {card_id}').fetchall()[0]
        con.execute(f'INSERT INTO records (CARD_ID, USER_ID) VALUES ({card_id}, {user[0]})')
        print('Card ID_' + m.payload.decode('utf-8') + ' time: ' + datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
        con.commit()

    window = tk.Tk()
    window.title('Subscriber')
    window.resizable(False, False)

    terminal_label = tk.Label(window, text='Terminal is not connected yet.')
    terminal_label.grid(column=0, row=0, columnspan=6, padx=15, sticky='nsew', pady=15)

    def add_worker():
        pass

    def remove_worker():
        pass

    def pin_card():
        pass

    def unpin_card():
        pass

    def make_report():
        records = con.cursor().execute('SELECT * FROM records').fetchall()
        with open('report.csv', 'w', newline='') as f:
            wr = csv.DictWriter(f, fieldnames=['id', 'card_id', 'user_id', 'timestamp'])
            wr.writeheader()
            for record in records:
                wr.writerow({
                    "id": record[0],
                    "card_id": record[1],
                    "user_id": record[2],
                    "timestamp": record[3]
                })
            terminal_label.config(text='Report was created.')

    add_worker_btn = tk.Button(window, text='Add worker', command=add_worker)
    add_worker_btn.grid(column=0, row=1, sticky='nsew', padx=(15, 0))

    remove_worker_btn = tk.Button(window, text='Remove worker', command=remove_worker)
    remove_worker_btn.grid(column=1, row=1, sticky='nsew', padx=(0, 15))

    pin_card_btn = tk.Button(window, text='Pin card', command=pin_card)
    pin_card_btn.grid(column=0, row=2, sticky='nsew', padx=(15, 0))

    unpin_card_btn = tk.Button(window, text='Unpin card', command=unpin_card)
    unpin_card_btn.grid(column=1, row=2, sticky='nsew', padx=(0, 15))

    make_report_btn = tk.Button(window, text='Make report', command=make_report)
    make_report_btn.grid(column=0, row=3, sticky='nsew', padx=(15, 0), pady=(0, 15))

    def stop():
        client.loop_stop()
        client.disconnect()
        con.close()
        sys.exit(0)

    stop_btn = tk.Button(window, text='Stop', command=stop)
    stop_btn.grid(column=1, row=3, sticky='nsew', pady=(0, 15), padx=(0, 15))

    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message

    con = sqlite3.connect('records.db')

    # Check for connection every tick until success
    while True:
        try:
            client.connect(broker)
            break
        except ConnectionRefusedError:
            print('Connection error.')

    client.loop_start()
    client.subscribe("worker/test")

    window.mainloop()


if __name__ == '__main__':
    run()
