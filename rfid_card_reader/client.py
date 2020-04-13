import sys
import time
import paho.mqtt.client as mqtt
import tkinter as tk
from config import CONFIG


def run():
    broker = CONFIG['BROKER']
    terminal = 'Terminal_1'

    window = tk.Tk()
    window.title('Client')
    window.resizable(False, False)

    terminal_label = tk.Label(window, text='Terminal is not connected yet.')
    terminal_label.grid(column=0, row=0, columnspan=6, pady=(15, 5), padx=15)

    card_id_textfield = tk.Entry(window).grid(column=1, row=1, columnspan=5, pady=(5, 10), padx=(0, 15))

    def publish():
        card_id = card_id_textfield.get()
        if card_id.isdigit():
            client.publish("worker/test", int(card_id))

    def stop():
        client.loop_stop()
        client.disconnect()
        sys.exit(0)

    tk.Label(window, text='Card ID').grid(column=0, row=1, columnspan=1)
    tk.Button(window, text="Check card", command=publish).grid(column=1, row=2, columnspan=3, pady=(5, 15))
    tk.Button(window, text="Stop", command=stop).grid(column=4, row=2, columnspan=2, pady=(5, 15))

    def on_connect(client, ud, flags, rc):
        terminal_label.config(text=f'{terminal}: {mqtt.connack_string(rc)}')

    client = mqtt.Client(terminal)
    client.on_connect = on_connect

    while True:
        try:
            client.connect(broker)
            break
        except ConnectionRefusedError:
            print('Connection error.')
            time.sleep(3)

    client.loop_start()
    window.mainloop()


if __name__ == '__main__':
    run()
