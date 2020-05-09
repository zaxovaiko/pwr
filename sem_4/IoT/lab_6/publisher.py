"""
RPi (publisher) -> PC
This is publisher file. Belongs to Raspberry Pi with connected RFID.
"""
import time
import sys
import paho.mqtt.client as mqtt
import tkinter as tk


def run():
    # Main function
    broker = 'localhost'
    terminal = 'Terminal 1'

    window = tk.Tk()
    window.title('Publisher')
    window.resizable(False, False)

    terminal_label = tk.Label(window, text='Terminal is not connected yet.')
    terminal_label.grid(column=0, row=0, columnspan=6, pady=(15, 5), padx=15)

    card_id_textfield = tk.Entry(window)
    card_id_textfield.grid(column=1, row=1, columnspan=5, pady=(5, 10), padx=(0, 15))

    def publish():
        # Send data (card_id) to the broker validating it before.
        card_id = card_id_textfield.get()
        if card_id.isdigit():
            client.publish("worker/test", int(card_id))
            terminal_label.config(text='Card ID was sent.')
        else:
            terminal_label.config(text='Card ID must be a number.')

    def stop():
        # Stops all loops. Stop executing the program.
        client.loop_stop()
        client.disconnect()
        sys.exit(0)

    tk.Label(window, text='Card ID').grid(column=0, row=1, columnspan=1, padx=(15, 5))
    tk.Button(window, text="Check card", command=publish).grid(column=1, row=2, columnspan=3, pady=(5, 15))
    tk.Button(window, text="Stop", command=stop).grid(column=4, row=2, columnspan=2, pady=(5, 15))

    def on_connect(client, ud, flags, rc):
        # Callback function on connect action
        terminal_label.config(text=f'{terminal}: {mqtt.connack_string(rc)}')

    client = mqtt.Client(terminal)
    client.on_connect = on_connect

    # Check for connection every 3 seconds until success
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
